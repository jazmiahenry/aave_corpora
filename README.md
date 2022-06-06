# AAVE Corpus Dataset Information

## Welcome to the AAVE Corpus. 

- This dataset was created by AAVE speakers for AAVE speakers and the engineers, academics, researchers, and builders that endeavor to create NLP models that represent the beauty and complexity of the AAVE sociolect. 

### Dataset Formation

The AAVE corpora collection is Python friendly though it can be manipulated using SQL, R, and JavaScript. There are four collections: Lyric, Leadership, Book, and Social Media and each collection can be called on as a package extension meaning each package can be called using the import function and the specific collection from the AAVE corpora. It would look like this:

```
    from aave import  #for all
    from aave import aave_lyrics  #for lyrics collection
```
 
 
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

#### Leadership Collection
The Leadership collection is a collection of speeches by prolific Black leaders from Fredrick Douglass to Sojourner Truth to Martin Luther King to Ketanji Brown Jackson and many Black political leaders in between. This collection is heavily skewed male and has a heavy education bias as the majority of speakers in this collection have at least a college degree. Geographically the dataset heavily favors speakers from the South and many states, such as Washington state, are not represented as a place of origin for any of the collected speakers. Read below for the analytical breakdown:

> Most speeches in the leadership collection are speeches by former President Barack Obama (29 present speeches).

#### Book Collection
The Book collection was the most difficult collection to augment. African Americans have been grossly underrepresented from the literary cannon and as a result selecting only the few to have been admitted into the Ivory tower would lend itself to self selection bias. Due to this, I worked to include works from Historically Black Book archive collections from universities. The University of Kansas has such an archive that I heavily powered from. The additions in this sample, though, are not as representative of the community as the other collections and is in need of open source contributions to truly capture the diversity of Black thought and AAVE use. 

> This was the hardest collection to source due to copyright standards. There are 54 books in this collection and growing.

Source: University of Kansas

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


**This repo is actively being updated, reconfigured, and refreshed for an official June 15 release. Email me at jazmia.henry@gmail.com for feedback, questions, and requests.**
