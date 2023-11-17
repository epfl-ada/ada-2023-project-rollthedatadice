# Personas from the films
Let's RollTheDataDice!
## Table of Contents
- [Structure of this repository](#structure-of-this-repository)
- [Abstract](#abstract)
- [Research Questions](#research-questions)
- [Additional dataset](#additional-datasets)
- [Methods](#methods)
- [Initial Analysis](#initial-analysis)
- [Schedule](#timeline)
- [Team Collaboration](#team-collaboration)

## Structure of this repository
```
+---data                               # Used to put the raw data
|   \---corenlp_plot_summaries         # Tagged data from Stanford CoreNLP-processed summaries
|   character.metadata.tsv
|   movie.metadata.tsv
|   name.clusters.txt
|   plot_summaries.txt

+---generated                          # Store the manipulated data
|   \images
|   \tropes                            # Crawled data from tvtropes

+---src                                # All the codes
|   movie_metadata_eda.ipynb           # Initial analysis on the movie_metadata.tsv

\---temp                               # Temporary files
```
## Abstract
Our project aims to address the critical gap in film analysis by quantitatively investigating character dynamics based on the dataset. We focus on identifying prevalent patterns among main and side characters, dissecting gender dynamics, and possibly exploring psychoanalytic dimensions. Further, we endeavor to reveal recurring themes, archetypes, and behavioral patterns that construct character networks to discern genre-specific tropes. By unraveling the intricate relationships between characters, we hope to provide insights to better understand the craft of storytelling in the dynamic landscape of cinema. 


## Research Questions
### Tropes
1. **Tropes over time**: Are some character tropes more or less popular through years?
2. **Genre tropes**: Which tropes are the most popular in each genre?
3. **Similar tropes:** Which curious associations between tropes (through the adjectives) can we find?
4. **Tropes and Box Office Success:** Which character tropes are associated with higher revenue of films?
5. **Cross-Genre Tropes:** Are there character tropes that are cross-genre?
6. **Combinations of tropes:** Are there specific combinations of tropes that tend to work well together or create interesting dynamics on screen?
### Network

## Additional datasets
We plan to extend our dataset by scraping the dataset of tropes associated to the characters from TVTropes. Here there is the character sheets for the [Live action](https://tvtropes.org/pmwiki/pmwiki.php/CharacterSheets/LiveActionFilms) films and the [Animation](https://tvtropes.org/pmwiki/pmwiki.php/CharacterSheets/AnimatedFilms) films. In these pages there are clear character-trope associations for 1000 films.


## Methods

Our idea involves many steps.
1. Extraction of character tropes for 1000 films from the website TVTropes
2. Execute the pipeline from the paper of the "Learning Latent Personas of Film Characters" paper
3. (Optional) Inference of character tropes for the rest of the films in the dataset through a classification model
4. Creation of character dynamics network for each film
5. Comparison and clustering of these networks
6. Final analysis on tropes and networks

#### 1.(Optional) Extraction of character tropes
Our first task would be scrape the website of the Character tropes, as described in the previous "Additional datasets" section. 
We would use libraries such as BeautifulSoup and Selenium.

#### 2. Execute the pipeline from the paper of the Character Personas
Our goal for this step is to obtain the adjectives/nouns list associated with each character. To do this, we plan to run the entire pipeline of [this repository](https://github.com/dbamman/ACL2013_Personas/tree/master). 
We are aware it's heavy computationally, we plan to make it by next week.
#### 3. (Optional) Inference of character tropes for the rest of the films in the dataset through a classification model

To address the limitation of tropes being available for only 1000 films we plan to design a classification model. 

The training data includes characters associated with tropes, which are then joined with "persona" classes. The objective is to predict character tropes for unlabeled data using the list of words associated with persona classes as features, treating it as a text classification problem. 

Techniques such as TF-IDF for numerical representation of adjectives and a language model like BERT are planned to be used. Potential challenges include class imbalance, especially with certain tropes, and concerns about the model's performance. 
If these challenges prove insurmountable, we may focus solely on the subset of 1000 films in the dataset.

#### 4. Creation of character dynamics network for each film

4.1. *Semantic Tagging*
This part has been done by [Stanford CoreNLP-processed summaries](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar). The tagged data is stored in XML format.

#### 5. Comparison and (optional) clustering of these networks
#### 6. Final analysis on tropes and networks



## Initial analysis
We did initial EDA for our movie dataset to understand in which decades the film were made, the genre distribution, country of origin and movie language.

Because of the strong bias towards american films in the dataset we discarded our idea about movies and cultures.
See `movie_metadata_eda.ipynb` in the `src` folder for more details.

## Timeline
| Time         | Task                   | Status  |
|--------------|----------------------- |---------|
| 17, Nov      | EDA, Proposal writing  |✅       |
| 24, Nov      | Parse the XML files    |         |
| 31, Nov      | Persona clustering     |         |
| 7, Dec       | Network analysis       |         |
| 14, Dec      | Build the network      |         |
| 21, Dec      | Finalize the story     |         |

## Team organization

| Member       | Tasks                 |
|--------------|-----------------------|
| Mehdi        | Build the network      |
| Yanzi        | Crawl tropes          |
| Jiaming      | Metadata analysis     |
| David        | Final data analysis   |
| Ke           | Metadata analysis     |



## Old stuff

Analyzing tropes from plot summaries.


For our project, we mainly focus on the “tropes” in these two categories: 

Persona trope

As is shown in the tropes.txt file, common persona tropes, for example, “brainless beauty”, and “arrogant kong-fu guy”, represent a certain kind of archetype in the films. For persona tropes, our first goal is to cluster the characters into existing persona tropes by semantic embedding and similarity calculation, etc. Then, we can do more extended analyses: 

In different film genres, are there different dominant persona tropes? In other words, would the protagonists in romcom and action movies be categorized into the same persona tropes? If not, does the difference reflect different expectations from their respective target audience? 

Within one genre, would the dominant persona tropes change over time? Why would it change? For example, what does it signify if recent years witnessed a decline in “brainless beauty” and an increase in “intelligent beauty” instead?

Taking the actors into account, are there some actors who always play roles of similar persona types? By contrast, maybe some actors are more diverse and perform well for a wide range of personas? We can calculate the “diversity score” for each actors based on the variance of the persona tropes of all the roles s/he once played.

Technical roadblocks:
persona clustering: new algorithm (entity recognition, coreference resolution, semantic distance between word vectors?)
more tropes need


Character dynamic/network trope

Character dynamic usually refers to how different characters in one film interact with each other, for example, Love Triangle, and Mentor-Student relationship. Yet we’d like to get something in a greater scale, i.e. the overall interpersonal relations in the film, which can be well illustrated in a network graph like: https://www.bing.com/images/search?view=detailV2&ccid=Ftt%2FqvLW&id=874EF44BAF686D8BDB8E89475498EF678F82E3B4&thid=OIP.Ftt_qvLW9uzGbcLzCK1I4QHaKe&mediaurl=https%3A%2F%2Finfographic.tv%2Fwp-content%2Fuploads%2F2019%2F05%2FInfographic-The-character-connections-from-Pride-and-Prejudice-OC-1152x1629.jpg&exph=1629&expw=1152&q=character+network+in+pride+and+prejudice&simid=607994518759938893&form=IRPRST&ck=BD7CC4BD78A1E4889CA3DD5916F8827A&selectedindex=1&ajaxhist=0&ajaxserp=0&vt=0&sim=11

But in our graph, each node representing a character would be linked with single or multiple edges representing the corresponding verbs. And we wonder:

in different genres, would the linking verbs have different distributions? That is to say, in violence films, the verbs are more likely to be of the “kill” “fight” clusters, whilst the verbs in romance films are more of “love” “envy” clusters? Then can we conclude the patterns?

what about different regions? for the same genre, would different regions prefer different character network tropes? How can we make sense of the difference?

Technical roadblock: 

graph comparison/clustering algorithm

    And apparently these two kinds of tropes are deeply intertwined with each other. To be continued


