import pandas as pd
import numpy as np
from urllib.parse import urlparse
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import math
import spacy
from spacy.tokens import Token
from spacy import displacy

from wikidataintegrator.wdi_core import WDItemEngine

def convert_freebase_id_to_entity(freebase_id):
    # if freebase_id is NaN，return NaN
    if pd.isnull(freebase_id):
        return np.nan

    # Define query
    sparql_query = f"""
    SELECT
        ?article
    WHERE 
    {{
        ?article schema:about ?item;
        schema:isPartOf <https://en.wikipedia.org/> .
        ?item wdt:P646 "{freebase_id}";
    }}
    """

    # Send the query request to WDQB
    results = WDItemEngine.execute_sparql_query(sparql_query)
    # If you query the result , return the entity name; 
    # otherwise the original freeBase ID will be returned
    if results['results']['bindings']:
        url = results['results']['bindings'][0]['article']['value']

        # Use urlparse to parse URL
        parsed_url = urlparse(url)

        # Extract the name
        article_name = parsed_url.path.split('/')[-1]

        return article_name
    else:
        return freebase_id


# function that given a personn returns the sentences where the person is cited
def get_sentences_with_person(person, doc):
    sentences = []
    for sent in doc.sents:
        if person in sent.text:
            sentences.append(sent.text)
    return sentences

#function that returns a list of unique characters
def get_characters(doc):
    characters = []
    for ent in doc.ents:
        if ent.label_ == "PERSON" and ent.text.istitle():
            characters.append(ent.text)
    return list(set(characters))

#function that cleans the chracter list returned by get_characters
def clean_character_list(character_list, doc):
    deleted_chars = []
    for i, character in enumerate(character_list):
        for chars2 in character_list[i+1:]:
            if character in chars2 or chars2 in character:
                if len(get_sentences_with_person(character, doc)) > len(get_sentences_with_person(chars2,doc)):
                    deleted_chars.append(chars2)
                else:
                    deleted_chars.append(character)
    return list(set(character_list) - set(deleted_chars))

#function that find which character the pronouns refer to
def replace_pronouns(doc, charSex, characters):
    Token.set_extension("ref", default=None, force=True)
    heStack = []
    sheStack = []
    theyStack = []
    neutralStack = []
    for sentence in doc.sents:
        for token in sentence:
            #detect personns and add them to the correct stack
            if token.text in characters :
                if token.nbor(1).pos_=="CCONJ":
                    if token.nbor(2).pos_ == "PROPN":
                        theyStack.append([token.text, token.nbor(2).text])
                        neutralStack.append([token.text, token.nbor(2).text])
                    elif token.nbor(3).pos_ == "PROPN":
                        theyStack.append([token.text, token.nbor(3).text])
                        neutralStack.append([token.text, token.nbor(3).text])
                elif any(charSex.index.str.contains(token.text)):
                    sex=charSex.loc[charSex.index.str.contains(token.text)]["actor_gender"].values[0]
                    if sex=="F":
                        sheStack.append(token.text)
                        neutralStack.append(token.text)
                    elif sex=="M":
                        heStack.append(token.text)
                        neutralStack.append(token.text)
                    else:
                        neutralStack.append(token.text)
            #replace pronouns
            if token.pos_ == "PRON":
                if token.text.lower() in ["he", "him", "his"] and (len(heStack) > 0):
                    token._.set("ref", [heStack[-1]])
                elif token.text.lower() in ["she", "her", "hers"] and (len(sheStack) > 0):
                    token._.set("ref", [sheStack[-1]])
                elif token.text.lower() in ["they", "them", "their", "theirs"] and (len(theyStack) > 0):
                    token._.set("ref", theyStack[-1])
                elif token.text.lower() in ["who"] and (len(neutralStack) > 0):
                    token._.set("ref", [neutralStack[-1]])
    return doc

#function that extracts the adjectives that describe a given character
def get_adjectives_for_character(character, doc):
    adjectives = []
    for token in doc:
        if (token.dep_ == "amod" or token.dep_ == "acomp" or token.dep_ == "compound") and token.text!=character :
            if token.head.text == character:
                adjectives.append(token.text)
            elif character in [child.text for child in token.head.children]:
                adjectives.append(token.text)
            elif token.pos_ == "PRON" and any([elem == character for elem in token._.ref]):
                adjectives.append(token.text)
    return adjectives

#function that given a sentence returns the subject, verb, and object if present
def get_subject_verb_object(sent):
    actions=[]
    for token in sent:
        if token.pos_ == "VERB" :  # Root verb (action)
            action = token.text
            subject = [child.text for child in token.children if child.dep_ == "nsubj" or child.dep_ == "nsubjpass"]
            object_ = [child.text for child in token.children if child.dep_ == "dobj"]
            if subject:
                actions.append((subject[0], action, object_[0] if object_ else None))
                return subject[0], action, object_[0] if object_ else None

def get_interaction(doc, nlp, characters):
    interactions=[]
    for character in characters:
        for sent in get_sentences_with_person(character, doc):
            for character2 in characters:
                if character2 != character and character2 in sent:
                    doc2=nlp(sent)
                    main_verb = [token.text for token in doc2 if (token.pos_ == "VERB") and (token.dep_ == "ROOT")]
                    if len(main_verb) > 0:
                        main_verb = main_verb[0]
                        if [character, main_verb, character2] not in interactions and [character2, main_verb, character] not in interactions:
                            interactions.append([character, main_verb, character2])
    return interactions

def edge_center_coordinates(edge, curvature, pos):
    start_x, start_y = pos[edge[0]]
    end_x, end_y = pos[edge[1]]
    # Calculate the control point coordinates for the curved edge
    control_x = 0.5 * (start_x + end_x) + curvature * (end_y - start_y)
    control_y = 0.5 * (start_y + end_y) - curvature * (end_x - start_x)
    # Calculate the Bezier curve parameters
    t = 0.5  # Midpoint of the curve
    bx = (1 - t)**2 * start_x + 2 * (1 - t) * t * control_x + t**2 * end_x
    by = (1 - t)**2 * start_y + 2 * (1 - t) * t * control_y + t**2 * end_y
    return bx, by

def graph_plot(data):
    G=nx.MultiDiGraph()
    plt.figure(figsize=(10,10))
    for subj in data["Char1"].unique():
        G.add_node(subj, color="lightblue")
        i=0
        for verb, obj in data[data["Char1"]==subj][["Verb", "Char2"]].itertuples(index=False):
            G.add_edge(subj, obj, label=verb, curvature=i/30)
            i+=2
    pos = nx.circular_layout(G)
    # Draw nodes separately
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
    # Draw node labels if needed
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
    # Draw the graph with curved edges based on the 'curvature' attribute
    for edge in G.edges(data=True):
        edge_data = edge[2]
        label = edge_data['label']
        curvature = edge_data.get('curvature', 0.1)  # Default curvature if 'curvature' is not present
        #draw edges
        nx.draw_networkx_edges(G, pos, edgelist=[(edge[0], edge[1])], connectionstyle=f'arc3,rad={curvature}', edge_color='black', width=2, alpha=0.7, label=label)
        center_coordinates = edge_center_coordinates(edge, curvature, pos)
        plt.text(center_coordinates[0], center_coordinates[1], label, color='red', fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    # Show the plot
    plt.show()