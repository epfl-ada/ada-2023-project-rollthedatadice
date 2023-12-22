
![Film Banner](./assets/img/banner.webp "film banner")

Welcome to the captivating world where stories unfold, emotions intertwine, and characters come to life on the silver screen! Our project sets out on a riveting journey through the heart of cinema, seeking to decode the intricate dance of characters within the vast tapestry of movie plot summaries.

In the grand tradition of narrative storytelling, characters serve as the beating heart of every cinematic masterpiece. Beyond their individual narratives, the dynamics between characters shape the essence of storytelling, steering plots towards climactic peaks, heartwarming resolutions, or tragic conclusions.

Why is understanding character dynamics so crucial? Well, as storytelling enthusiasts, filmmakers, and data enthusiasts alike, we believe that unraveling the patterns of character interactions unveils the very essence of cinematic storytelling. Characters are not mere entities; they are conduits through which narratives breathe, conveying emotions, conflicts, and resolutions.

Buckle up as we begin the odyssey through the realms of persona distributions, intricate character networks, and the pulsating rhythm of cinematic evolution! 🚀 Are you ready to peer into the soul of cinema and witness the magic that unfolds when characters take center stage? Let the curtain rise, and let the data story begin! 🌟


## <a id="section_1">Understanding Individual Characters</a>
### Peering into the Essence of Characters: A Journey into Personas

This is the beginning of our cinematic exploration, where characters reveal their individuality through distinct personas. Now, let's delve into the latent behavioral and personality patterns that define characters before walking along their narrative pathways.

#### What are Personas?

In movie plot summaries, personas serve as the key to understanding the potential and latent traits of characters. These personas represent behavioral archetypes, offering a glimpse into how characters might navigate the intricacies of their cinematic worlds.

<details>
  <summary>Show more</summary>
  
We get the personas by running the pipeline outlined in the "Learning Latent Personas of Film Characters" paper [Link](https://github.com/dbamman/ACL2013_Personas/tree/master?tab=readme-ov-file). 
   
</details>

We can take a look at the most associated words for each persona to get a basic impression.

{% include wordcloud_persona.html %}

Also, how each persona is linked to different genres:

{% include persona_genre_mapping.html %}

As we can see, persona 10 appears more in Romantic Comedy, Romance Film, Drama and Comedy; while persona 47 is more often seen in Thriller, Drama, Crime Fiction, Action.

#### Gendered Personas: Navigating Binary Essences

Our journey begins by dissecting the personas of characters based on gender. What are the most common behavioral archetypes for male and female characters? 

<details>
  <summary>Show more</summary>
  
Actually we don't really have gender information about the characters. We could only use the corresponding actor's gender instead, which might bring trivial error.
   
</details>

{% include gender_persona_percentage.html %}

We can see from the graph, the top 2 personas, 10 and 47, present a great gender discrepancy.

As the cinematic timeline unfolds, do we witness an evolution in these archetypes, reflecting changing societal norms?

{% include persona_gender_temporal.html %}

What can we learn from the graph? 【to be added】

Zooming in, we explore the nuances of personas within different genres. Does the stereotypical persona of a male or female character change when the stage is set in a romance, action, or sci-fi setting?

{% include female_genre_persona.html %}
{% include male_genre_persona.html %}

#### Character Type Personas: Main Stage vs. Side Story

As we shift our gaze to character types, the question arises: do main and side characters typically share similar personas, or do their behavioral archetypes diverge?

{% include chartype__persona.html %}

Does it vary over time?

{% include chartype__persona_temporal.html %}

From both graphs above, it seems there's no significant difference in main and side characters' personas.

<details>
  <summary>Show more</summary>
  
talk about whether there's a significant difference. T test?
   
</details>


#### Closing the Curtain: A Persona-Painted Prelude

As we draw the curtain on this first part of our data story, the personas of individual characters emerge as the backdrop, setting the stage for the intricate interactions that follow. Join us in the next act as we shift our focus from individual character nuances to the dynamic dance of personas in the realm of character interactions.


<br>

## <a id="section_2">Interaction Analysis by Gender</a>
###  Gendered Symphony of Character Interactions
### From Personas to Partnerships: Harmony and Discord on the Silver Screen

Having delved into the individual personas that shape the characters, we now turn our gaze towards the dynamic partnerships and interactions that unfold on the silver screen. In this chapter, we explore how the distinctive personas we unveiled in the previous act come to life in the intricate dance of gendered character interactions.

🌐 Mapping the Cinematic Web:
To unravel the secrets of character interactions, we build the movie networks. Each film's plot summary transforms into a complex tapestry of relationships, woven into a network graph. Characters become nodes, and their interactions form the connecting threads. This network allows us to visualize the intricate dynamics between characters, offering a unique lens through which we decode the gendered symphony of cinematic storytelling. Here we show an example.

{% include hunger_games_network.html %}

<details>
  <summary>Show more</summary>
  
We use SpaCy to get the NER tags in each sentence. Then we parse each sentence to get the get Subject-Verb-Object (SVO) triples. We use only keep the triples whose subject is a character and the object is also a character. We then use the subject and object as the nodes and the verb as the edge.

</details>
🌟 Unveiling the Gender Dynamics:
Picture this – a tapestry of character interactions where male and female protagonists engage in a harmonious ballet of emotions. Our analysis has unraveled the most common interactions between characters of the same gender. Do they share tender moments of camaraderie or clash in the tempest of conflicts?

#### The Male-Male Tapestry: Bonds Beyond Brotherhood
👬 Brotherhood and Beyond:
Behold the camaraderie, the alliances, and the conflicts as male characters forge connections that go beyond mere friendship. From shared goals to epic showdowns, the male-male tapestry is rich with the resonances of character interactions.

📈 Dynamic Evolution:
Explore how these interactions have evolved over time. Do modern bromances differ from those of classic cinema, reflecting the shifting tides of societal expectations?

#### Female-Female Symphony: Solidarity in Cinematic Sorority
👯‍♀️ Sisterhood in Action:
Delve into the world of female characters as they navigate the cinematic landscape together. Do they share secrets, conquer challenges, or perhaps engage in playful banter? The female-female symphony is a celebration of solidarity and strength.

📊 A Glimpse Through Time:
Trace the evolution of these relationships across different eras. How have on-screen female friendships mirrored the changing roles of women in society?

#### The Dance of Opposites: Male-Female Duets
💑 Romance, Conflict, or Both:
Witness the dance between male and female protagonists, where the sparks of romance, the fires of conflict, or a delicate balance of both come to life. The male-female duets are a captivating exploration of love, tension, and everything in between.

🔍 Genre-Specific Intricacies:
Zoom into different genres to unravel how the dynamics of male-female interactions vary. Is the romance in a comedy different from that in a drama?

As we peer into the kaleidoscope of gendered interactions, our data-driven journey promises to unveil the nuanced dynamics that underpin the relationships between characters on the silver screen. 🎭 Are you ready to decode the secrets of gendered storytelling in cinema? Join us as we navigate through the emotional landscapes of male-male, female-female, and male-female character interactions! 🍿✨


<details>
  <summary>Show more</summary>
  details
</details>

<br>

## <a id="section_3">Interaction Analysis by Character Type</a>
### **Interaction Analysis by Character Type: Main Characters and Side Characters Through Time and Genre**
Lights, camera, dimensions! In this segment of our cinematic odyssey, we journey through time and traverse the diverse landscapes of genres to uncover the secrets hidden within the dynamics between main and side characters.

🌟 Main-Main Connections:
As we step across cinematic eras, observe how the interactions between main characters have evolved over time. Do the romantic dialogues of yesteryear differ from the action-packed exchanges of the modern era? Time, it seems, leaves an indelible mark on the relationships between protagonists.

Academic Glimpse: 🎓 Channeling the insights of film historian David Bordwell, we contemplate the impact of changing film techniques and narrative structures on the dynamics between main characters across different cinematic periods.

👥 Side-Side Bonds:
Now, let's journey through genres, where the roles of side characters unfold against distinct backdrops. Are the side-side bonds of a classic film noir different from those in a contemporary romantic comedy? Immerse yourself in the genre-specific nuances that shape the interactions between supporting characters.

🌐 Main-Side Interactions:
Venture through time and genres as we unravel the intricate dance between main and side characters. Do these interactions adapt to the storytelling conventions of film noir, comedy, or science fiction? The evolution of character dynamics becomes even more pronounced as we navigate through both temporal and genre dimensions.

📈 Temporal Evolution and Genre Extravaganza: Beyond mere exploration, let's synchronize the ticking of the clock with the beats of different genres. How have the interactions between main and side characters changed over time within specific genres? Do certain genres dictate unique character dynamics that transcend temporal boundaries?

As we embark on this multidimensional exploration, the narrative unfolds, weaving together the threads of time and genre into a rich tapestry of character dynamics. 🌌 Join us on this immersive journey through cinematic eras and genre landscapes, where characters, both main and side, play their roles in the ever-evolving story of the silver screen! 🎭🍿

<details>
  <summary>Show more</summary>
  This score provides us with information about which users contribute to enriching the experience on the website, either because they rate beers that do not get much attention, or because they "introduce" new beers on the website by being the first people to rate those beers.
  
  A user $u$ is an explorer if, often enough, among the beers he rated, he/she was among the first 10 users to rate that beer. The score is, therefore: 

  $$XPL_u = \sum_{b \in B_u} \mathbb{1} [u \in U_{10}(b)]$$

  $B_u$ is the set of beers rated by user $u$.

  $U_{10}(b)$ is the set of at most 10 users that first rated the beer $b$.
  
</details>

<br>

## <a id="section_4">Intersectional Analysis</a>
### **Intersectional Analysis: Where Gender and Character Type Converge**
The stage is set for a detailed exploration of character dynamics as we unfold the intricacies of four key combinations: Male-Main, Male-Side, Female-Main, and Female-Side. Each combination tells a unique story, revealing the dynamics that underpin the interactions between characters of different genders and roles.

1. Male-Main Characters:
🎭 Behind the Masculine Lens

How many male main characters grace the cinematic canvas? Unveil the personas that embody the essence of the narrative.
Dive into the interactions between male main characters. Are they bound by shared pursuits, rivalries, or collaborations? Explore the emotional landscapes that unfold within this dynamic group.
2. Male-Side Characters:
🎬 Supporting Roles in Focus

Shine the spotlight on male side characters as they add depth and complexity to the narrative. How do their roles influence the overarching story?
Analyze the interactions between male side characters and other character types. Are they amplifying the journeys of the main characters or crafting unique subplots?
3. Female-Main Characters:
🌟 Leading Ladies in Action

Illuminate the screen with the presence of female main characters. What personas define their roles, and how do they shape the narrative arc?
Delve into the interactions between female main characters. Are their connections characterized by solidarity, competition, or a blend of both? Uncover the emotional layers that unfold within this ensemble.
4. Female-Side Characters:
🌈 Side Characters Stepping Forward

Acknowledge the roles played by female side characters, often the unsung heroes of the cinematic narrative. How do they contribute to the richness of the story?
Investigate the interactions between female side characters and other character types. Do they forge unique bonds or add intricate layers to the relationships within the narrative?
📊 Quantifying the Ensemble:
Before the characters take their places on the stage, let's quantify the ensemble. How many characters fall into each category? Are there notable trends or imbalances that catch the eye?

🌐 Temporal Evolution and Genre Dimensions: As we traverse through time and explore various genres, how have the numbers and interactions within each character category evolved? Does the cinematic landscape reflect changing societal norms and storytelling conventions?

As we unveil the personas and interactions within each character combination, a vivid narrative unfolds, shedding light on the intricate dance of characters within the intersectional realms of gender and roles. 🎥 Join us as we unravel the stories woven into Male-Main, Male-Side, Female-Main, and Female-Side character dynamics, where each combination contributes to the symphony of cinematic storytelling! 🍿🎶
<details>
  <summary>Show more</summary>
  
  A user $u$ is an adventurer if he/she often enough risks trying out beers that have a bad rating at the time at which they rate them (less than 3.25/5, knowing that the average is at $\approx$ 3.97/5). The corresponding score is the following:

  $$ADV_u = \sum_{b \in B_u} \mathbb{1} [\overline{r}_{u,b}(t_{u,b}) < T]$$

  $B_u$ is the set of beers rated by user $u$.

  Rating $\overline{r}_b(t_{u,b})$ is the average rating of beer $b$ at the time $t_{u,b}$ at which user $u$ rates beer $b$.

  $T=3.25$ is a cut-off determined empirically based on the data.
</details>

<br>


## <a id="section_takeaway">Takwaway</a>

