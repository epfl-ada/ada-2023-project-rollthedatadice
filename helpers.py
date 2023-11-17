import spacy
from spacy.tokens import Token

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
                    sex=charSex.loc[charSex.index.str.contains(token.text)]["Actor gender"].values[0]
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

#function that returns every subject, verb, and object set if present
def get_subject_object(doc):
    interactions=[]
    for token in doc:
        if token.pos_=="VERB":
            subj=[child for child in token.children if child.dep_ == "nsubj" or child.dep_ == "nsubjpass"]
            subj=subj[0] if subj else None
            obj=[child for child in token.children if child.dep_ == "dobj" or child.dep_ == "pobj"]
            obj=obj[0] if obj else None
            if subj and obj:
                if subj.text in characters and obj.text in characters:
                    interactions.append([subj.text, token.lemma_, obj.text])
                elif subj._.ref:
                    for elem in subj._.ref:
                        if obj._.ref:
                            for elem2 in obj._.ref:
                                interactions.append([elem, token.lemma_, elem2])
                        else:
                            interactions.append([elem, token.lemma_, obj.text])
                elif obj._.ref:
                    for elem in obj._.ref:
                        interactions.append([subj.text, token.lemma_, elem])
    return interactions