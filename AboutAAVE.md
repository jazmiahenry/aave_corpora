# Introduction

“What would America be like if we loved black people as much as we love black culture?” mused an erudite 16-year old that had her own fair share of hate and discrimination on social media for her performance of the fan favorite, Rue, on the box-office hit “Hunger Games”. This question rises to a crescendo as digital blackface and the use of AAVE amongst non-black people online increases along with hostility toward pro-black organizations, artists, and political expression. Downstream NLP tasks such as Sentiment Analysis Systems finds itself wedged squarely within this conflict when it attempts to quantitatively measure sentiment of text while simultaneously applying negative sentiment to black speakers, black speech, and black expression disproportionately. 

This led me to my main question:
How would Natural Language Processing downstream tasks perform if it were trained on a corpora that contained a more representative sample of AAVE used by Black speakers?

Conversations about AAVE being a language are not new. For decades, mainstream linguistic scholars have argued that AAVE is a subset of the English language- more of a sociolect or dialect than a language of its own. This conclusion also comes paired with the insidious association of the use of “Ebonics”- as it was once referred - and less education amongst the population of people that use it. With the rise of social media, non-black people have embraced the use of AAVE while still associating those who use it in everyday speech as being uneducated. These negative associations have bled into downstream NLP tasks, particularly sentiment analysis and next word generation. I will not write about the many examples of "NLP gone wrong" for Black people in this paper, but I will share a list of sources that provide strong evidence at the article's conclusion. Instead, I will focus on my corpora and the work that went into the compilation of what I consider to be step one of many. If researchers seek to perform non-biased analysis on Black speakers, they must address racial bias in word association and the first step to doing this is to give AAVE its due respect in linguistics and natural language processing by way of a corpora that fairly and accurately represents Black speech. 


# Method

African American Vernacular English, or as referred to in this paper AAVE, is a manifestation of uplift and survival through oppression spoken by millions of Black Americans. Geneva Smitherman defines AAVE as "the language and discourse patterns of African slave descendants in the United States, which reflect the survival of African languages in the English used by these descendants” (Smitherman 2015: 547) Through decades of debate around its status as a dialect or language, one thing remains resoundly clear, AAVE is a rule-bound language with systematic grammatical features that characterize it as being distinct from American English. (Language Jones) This distinction has led to centuries of denigration and opression of AAVE speakers with people both within and outside of the Black community looking down on the use of AAVE as being a sign of a lack of intelligence. (DeBose) Sociolinguists, however, have proven the exact opposite to be true: AAVE is used by Black Americans across classes, throughout regional differences, and across all ages. (Britt, Weldon) 

Despite the acknowledgment of AAVE's importance in the Black community, little has been done representatively to spread instances of AAVE widely. This under-represenation of AAVE negatively effects Natural Language Processing models that rely heavily on four sources for data collection: 1) Newspapers, 2) Books, 3) Wikipedia 4) Open Sourced contributions. When I began collecting sources for the AAVE corpus, I had a similar idea in mind: find books of major academic note, popular newspapers by American Black people, and, to truly capture the dynamic of AAVE, scrape content from Black associated Hashtags on Twitter. Thankfully, I learned that this approach would do very little to fix the underlying issue of AAVE under-representation and erasure. While there are many prolific and historically significant Afircan Americans that have work that has been preserved in the American literary canon, there are not nearly as many as white white writers and when we add the additional condition of using AAVE in print, the numbers of available works that fit the criterion dwindle quickly. 

To find enough instances of AAVE that both positively reflects the use and intent of AAVE while being a robust sample, I decided to think outside of the box and use these four sources for my dataset instead: 

1) Song Lyrics including the lyrics of Negro Spirituals, 

2) Collections of Speeches from Black American leaders and Civil Rights Leaders, 

3) Collections of Books written by Black Authors that use AAVE, 
 
4) Social Media. 
 
Sources: I used the Genuis API for Song Lyrics and Song Lyric Meanings, collected speeches from historic archives, found books from historic collections including the historic manuscript collection from the Library of Congress, and used YouTube and Twitter to find instances of AAVE in spoken and written form. For the sake of this corpora, I transcribed all spoken word into written form for ease of analysis. 


# References
[1] Rickford, John R. 1999. African American Vernacular English: Features, Evolution, and Educational Implications. Malden, MA: Blackwell.


[2] Alim, H. Samy, and Geneva Smitherman. 2012. Articulate While Black: Barack Obama, Language, and Race in the U.S. Oxford, UK: Oxford University Press.


[3] Bell, Alan. 1984. Language Style as Audience Design. Language in Society, 13 (2): 145–204.


[4] Britt, Erica, and Tracey L. Weldon. 2015. African American English in the Middle Class. In Sonja Lanehart (ed). The Oxford Handbook of African American Language. New York: Oxford University Press. 800-816.


[5] Chambers, Jack. 2009. Sociolinguistic Theory, Revised Edition. Malden, MA: Blackwell.


[6] Craig, Holly K., and Julie Washington. 2006. Malik goes to school: Examining the language skills of African American students from preschool-5th grade. Mahwah, NJ: Erlbaum.

[7] Debose, Charles. 1992. Codeswitching: Black English and Standard English in the African‐American Linguistic Repertoire. Journal of Multilingual and Multicultural Development, 13 (2): 157-167.


[8] Debose, Charles. 2015. The Systematic Marking of Tense, Modality, and Aspect in African American Language. In Sonja Lanehart (ed). The Oxford Handbook of African American Language. New York: Oxford University Press.


[9] https://www.languagejones.com/blog-1/2014/6/8/what-is-aave#:~:text=AAVE%20is%20a%20dialect%20of,than%20other%20dialects%20of%20English.


[10] https://time.com/6092078/artificial-intelligence-play/


[11] Bender, E. M., Gebru, T., McMillan-Major, A., &amp; Shmitchell, S. (2021). On the dangers of stochastic parrots. Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency. https://doi.org/10.1145/3442188.3445922

