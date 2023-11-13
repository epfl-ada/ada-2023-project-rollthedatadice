# ada-2023-project-rollthedatadice
ada-2023-project-rollthedatadice created by GitHub Classroom
## Table of Contents
- [Structure of this repository](#structure-of-this-repository)
- [Abstract](#abstract)
- [Research Questions](#research-questions)
- [Methods](#methods)
- [Initial Analysis](#initial-analysis)

## Structure of this repository
```
+---data
|   \---corenlp_plot_summaries
+---generated
+---src
\---temp
```
## Abstract
## Research Questions
## Methods
## Initial analysis







Analyzing tropes from plot summaries.

Context: Assuming a great majority of the screenwriting (especially for those feature films) is essentially generated with basic narrative elements, their variations, and combinations (we can refer to Robert McKee’s Story, which is a classic guidebook for Hollywood playwrights), we have good reasons to believe it is possible and also interesting to decompose the films through analyzing the plot summaries, to identify those “tropes” and further to investigate the cultural implications behind.

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


