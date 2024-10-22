# AAVE Corpus Dataset Information

## Welcome to the AAVE Corpus. 

This dataset was created by AAVE speakers for AAVE speakers and the engineers, academics, researchers, and builders that endeavor to create NLP models that represent the beauty and complexity of the AAVE sociolect. 

### Dataset Formation

The AAVE corpora collection is an open source data collection that uses json and txt files. There are four collections: Lyric, Leadership, Book, and Social Media and each collection can be accessed through this Git repo. This Git repo is protected by MIT License for research purposes only. This repo is only the beginning of the AAVE corpora and is used as a basis for futher research for Natural Language Data supplementation for downstream NLP tasks. Download the repo in a Zip file for access. Be aware that this repo is about 400 MB of unprocessed files with 231 items. Further processing each file will increase storage size. 
 
The specific compilation of each collection is different. Below I will describe the characteristics of each.

#### Lyric Collection
The Lyric Collection is a combination of json files by artist that contains the lyrics of up to 350 songs from their discography. I focused on compiling the names of the most popular and influential Black artists of the 20th and 21st century. The Lyric collection is skewed male with a heavier emphasis on Hip Hop. This is largely due to the prevalence of male Hip Hop artists in the music industry in the modern day and the relative ease of access to lyrics after the 1950s compared to before. The analytical breakdown of the corpora is below:

> There are 21 women and 39 men in this collection. 
> 
> There is an average of 250 songs per artist bringing the overall song lyric collection to ~15,000 songs.
> 
> The oldest song present was recorded in the 1930s. 
> 
> The newest song in the collection was recorded this year.

Source: Genius 

![Lyrics](corpora/lyrics_wordcloud.png)

#### Leadership Collection
The Leadership collection is a collection of speeches by prolific Black leaders from Fredrick Douglass to Sojourner Truth to Martin Luther King to Ketanji Brown Jackson and many Black political leaders in between. This collection is heavily skewed male and has a heavy education bias as the majority of speakers in this collection have at least a college degree. Geographically the dataset heavily favors speakers from the South and many states, such as Washington state, are not represented as a place of origin for any of the collected speakers. Read below for the analytical breakdown:

> 34 speeches from Black leaders. 
> Most speeches in the leadership collection are speeches by former President Barack Obama.

![Leadership](corpora/leadership_wordcloud.png)

#### Book Collection
The Book collection was the most difficult collection to augment. African Americans have been grossly underrepresented from the literary cannon and as a result selecting only the few to have been admitted into the Ivory tower would lend itself to self selection bias. Due to this, I worked to include works from Historically Black Book archive collections from universities. The University of Kansas has such an archive that I heavily powered from. The additions in this sample, though, are not as representative of the community as the other collections and is in need of open source contributions to truly capture the diversity of Black thought and AAVE use. 

> This was the hardest collection to source due to copyright standards. There are 54 books in this collection and growing.

Source: University of Kansas

![Literature](corpora/literature_wordcloud.png)

#### Social Media Collection
The Social Media Collection is my most robust and diverse collection of AAVE instances for modern day analysis. Included in this collection are json files of video transcripts, tweets, and blog posts from Black thought leaders that use AAVE prominently. 

I am a Twitter Developer Research API subscriber and have retrieved tweets using the third party Python packages Tweepy and SNScrape. The Tweet collection
information is as followed:

> Search Full Archive Tweets
> - #thanksgivingclapback  
     - Date: 11/16/2015 - 11/30/2015 Count: 500 
     - Date: 11//21/2016 - 11/30/2016 Count: 1000
     - Date: 11/20/2017 - 11/30/2017 Count: 1000
> - #OscarsSoWhite: 
     - Date: 01-14-2015 - 01-30-2015 Count: 500
> - #SayHerName 
     - Date: 02-01-2015 - 07-30-2015 Count: 500
> - #blackmoms 
     - Date: 06-28-2019 - 07-01-2019 Count: 500
> - #BlackLivesMatter 
     - Date: 05-25-2020 - 08-01-2020 Count: 5000

> Search 30 Day Tweets*
> - #blm 
     - Date: June 2022 Count: 2000
> - #BlackGirlMagic
     - Date: June 2022 Count: 100
> - #BlackTwitter
     - Date: June 2022 Count: 100
> - #SayHerName
     - Date: June 2022 Count: 100
> - LilNasX bet awards
     - Date: June 2022 Count:100

> Tweet Total: 11,400
Source: Twitter

![Social Media](corpora/social_media_wordcloud.png)

### Corpora

The corpora folder includes the processed .txt files of the AAVE corpora. There are 141341 words in this corpora as of June 9, 2022.

> social_media_corpora.txt is the processed .txt file of all of the tweets in this corpora. Here are the details:
>    - Emojis and hashtags are still in tweets for researchers to either remove or keep to their discretion
>    - All users and location information has been scrubbed to protect identity
>    - Tweets collected are not scrubbed of profanity. 

> leadership_corpora.txt is the processed .txt file of all speeches in this corpora.

> literature_corpora.txt is the processed .txt file of all books in this corpora. 

> lyrics_corpora.txt is the processed .txt file of all lyrics in this corpora.


![Corpora](corpora/corpora_wordcloud.png)






**This repo is actively being updated, reconfigured, and refreshed. Email me at jazmia.henry@gmail.com for feedback, questions, and requests.**
