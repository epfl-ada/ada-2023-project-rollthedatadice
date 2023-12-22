# Unveiling Character Dynamics: A Quantitative Exploration of Movie Narratives
Let's RollTheDataDice!
See our website here:  https://epfl-ada.github.io/ada-2023-project-rollthedatadice/
The overall workflow notebook is in `data_analysis.ipynb`


## Table of Contents
- [Structure of this repository](#structure-of-this-repository)
- [Abstract](#abstract)
- [Research Questions](#research-questions)
- [Methodologys](#methodology)
- [Initial Analysis](#initial-analysis)
- [Schedule](#timeline)
- [Team Collaboration](#team-collaboration)



## Abstract
Our project aims to address the critical gap in film analysis by quantitatively investigating character dynamics based on our dataset. We focus on identifying prevalent patterns among main and side characters, dissecting gender dynamics, and possibly exploring psychoanalytic dimensions. Further, after extracting the semantic character network for each film, we endeavor to reveal recurring themes, archetypes, and behavioral patterns that construct these character networks to discern genre-specific tropes. By unraveling the intricate relationships between characters, we hope to provide insights to better understand the craft of storytelling in the ever-evolving landscape of cinema. 


## Research Questions
For our analytical framework, we first extract three main factors from movie metadata that might influence the character dynamics:  temporal, geographical, and genre-related ones.
### Single character
To start with, we'd like to probe into single characters.
- **Main characters**
1. What are the most common behavioral and personality patterns exhibited by main characters? Do they reflect anything about the public psychology?
2. More specifically, how do these patterns evolve over time and differ across regions and genres? Are there any cultural or social implications behind?
- **Side characters**
3. Similarly, what are the most common behavioral and personality patterns exhibited by side characters?
4. Again, how do these patterns evolve over time and differ across regions and genres?
### Character network
Then, we get the semantic character network graph from each movie, in which every node represents a character and the edges represent the events (verbs) linking the characters.
- **Character interactions**
5. What are the common interaction patterns and relationships that unfold among main characters?
6. How do main characters typically engage with side characters, and what roles do side characters play in influencing the storyline?
7. Are there distinctive patterns in the portrayal of relationships between characters in movies of different times, and from different regions?
- **Gender dynamics**
8. What are the most prevalent interaction patterns between characters of the same gender, and how do these patterns vary across genres? Could we uncover any clues about gender politics embodied in the movies?
9. What is the distribution of male and female characters in main/side roles across different movie genres, and are there notable disparities?
10. Are there specific genres where the dynamics of male main/side characters significantly contrast with those of female main/side characters, and vice versa?


## Methodology

Our idea involves many steps.
1. Implementation of the pipeline outlined in the "Learning Latent Personas of Film Characters" paper
2. Qualitative labelling of the personas
3. Generation of character dynamics networks for each film
4. Extraction of character adjectives
5. Identification of main and side characters
6. Semantic character network comparison
7. Final analysis on characters and networks

**1. Implementation of the pipeline outlined in the "Learning Latent Personas of Film Characters" paper**

Our goal for this step is to obtain the persona and the corresponding distributions of topics associated with each character. To do this, we plan to run the entire pipeline of [this repository](https://github.com/dbamman/ACL2013_Personas/tree/master). 
We are aware it's heavy computationally, we plan to make it by next week.

**2. Qualitative labelling of the personas**

When we get our list of classes from the previous step, we will qualitatively label these classes. We will take in consideration which assumptions we take in this step for the further analyses.

**3. Generation of character dynamics networks for each film**

In this phase we have to perform different tasks:
1. We start by identifying the characthers in our plot by using Spacy library and process them for entity disambiguation (e.g. name & surname).
2. (Optional) For the pronouns we can use NER techniques to infer to which character the pronoun is referring to.
3. Extract the edges between our characters. This could involve techniques ranging from co-occurrence in one sentence or a more strict pattern as "character-verb-character". We already started to test different methods.

**4. Extraction of character adjectives**

To find adjectives, we use the Spacy library and perform text processing on the syntactic structure provided by the dependency tree to find words that are labeled as amod (adjectival modifier), acomp (adjectival complement) or others that are connected to the character.

**5. Identification of main and side characters**

To define main and side characters we could look at two things:
1. Frequency of the characters
2. Node-Related Measures such as degree, PageRank, Betweennesscentrality.

**6. Semantic character network comparison**

We define our character network as $G = (V, E)$, where the vertices represent the characters in the plot and the edges represent the interaction between the two characters. After constructing this network, we map each character to specific personas, as depicted in the diagram below.

![Persona mapping.png](./generated/images/persona_mapping.png)


**7. Final analysis on characters and networks**
For our final analysis we will perform many visualizations such as bar plots, histograms, wordclouds and mainly network visualization to explore the research questions we have.



## Timeline
| Time         | Task                   | Status  |
|--------------|----------------------- |---------|
| 17, Nov      | EDA, Proposal writing  |✅       |
| 24, Nov      | Run the persona pipeline, qualitative label, network pipeline    | ✅        |
| 31, Nov      | Main & side characters     | ✅        |
| 7, Dec       | Analysis of character interactions & gender dynamics     | ✅        |
| 14, Dec      | Network comparision & Final data visualizations      |   ✅      |
| 21, Dec      | Finalize the story     |   ✅      |

## Team organization

| Member       | Tasks                 |
|--------------|-----------------------|
| Mehdi        | Build the network & adjective extraction & SVO interaction creation     |
| Yanzi        | Character dynamics, pipeline running, persona mapping         |
| Jiaming      | Gender dynamics, personal analysis, website    |
| David        | Main & side characters, clustering on interactions   |
| Ke           | Coref-resolution, website, LDAs     |




