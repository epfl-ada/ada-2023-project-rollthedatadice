# Personas from the films
Let's RollTheDataDice!
## Table of Contents
- [Structure of this repository](#structure-of-this-repository)
- [Abstract](#abstract)
- [Research Questions](#research-questions)
- [Methods](#methods)
- [Initial Analysis](#initial-analysis)
- [Schedule](#schedule)
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
Assuming a great majority of the screenwriting (especially for those feature films) is essentially generated with basic narrative elements, their variations, and combinations (we can refer to Robert McKee’s Story, which is a classic guidebook for Hollywood playwrights), we have good reasons to believe it is possible and also interesting to decompose the films through analyzing the plot summaries, to identify those “tropes” and further to investigate the cultural implications behind.

## Research Questions
1. **Tropes over time**: Are some character tropes more or less popular through years?
2. **Genre tropes**: Which tropes are the most popular in each genre?
3. **Similar tropes:** Which curious associations between tropes (through the adjectives) can we find?
4. **Tropes and Box Office Success:** Which character tropes are associated with higher revenue of films?
5. **Cross-Genre Tropes:** Are there character tropes that are cross-genre?
6. **Combinations of tropes:** Are there specific combinations of tropes that tend to work well together or create interesting dynamics on screen?

## Methods
1. **Semantic Tagging**
This part has been done by [Stanford CoreNLP-processed summaries](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar). The tagged data is stored in XML format.
2. **Clustering**
Use unsupervised learning methods like LDA to get the clusters of the personas based on the descriptive words we get about the person from the parsed data.
3. **Network Analysis**
To be filled


## Initial analysis
See `movie_metadata_eda.ipynb` in the `src` folder.

## Schedule
| Time         | Task                   | Status  |
|--------------|----------------------- |---------|
| 17, Nov      | EDA, Proposal writing  |✅       |
| 24, Nov      | Parse the XML files    |         |
| 31, Nov      | Persona clustering     |         |
| 7, Dec       | Network analysis       |         |
| 14, Dec      | Build the network      |         |
| 21, Dec      | Finalize the story     |         |

## Team collaboration

| Member       | Task                  |
|--------------|-----------------------|
| Mehdi        | Buil the network      |
| Yanzi        | Crawl tropes          |
| Jiaming      | Metadata analysis     |
| David        | Tropes extraction     |
| Ke           | Metadata analysis     |





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


