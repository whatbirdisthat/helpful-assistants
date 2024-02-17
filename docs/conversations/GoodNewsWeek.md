# Good News Week
A composition of models processing the feeds of a set of news sources and summarizing the good news.

1. Retrieval of news articles from a set of news sources - wget, scraping, beautifulsoup etc
2. Summarization of the news articles - gensim, nltk etc
3. Classification of the news articles - sklearn, nltk etc
   4. Sentiment analysis of the news articles - sklearn, nltk etc
   5. Topic modeling of the news articles - gensim, nltk etc
4. Visualization of the news articles - matplotlib, seaborn etc ?
   5. Mood bias detection
   6. Topic bias detection
5. Presentation of the news articles - flask, django etc
6. Deployment of the system - heroku, aws etc
7. Monitoring of the system
8. Maintenance of the system
9. Testing of the good-news-week system
10. Evaluation of the news articles - engagement, traction, feedback etc

## 1. Retrieval of news articles from a set of news sources
Using APIs to pull news articles from a set of news sources where possible, otherwise using web scraping to pull
news articles from a set of news sources.

Finding a through-line in the set, a common theme, a common topic, a common sentiment, a common mood, a common bias.
Build the list of through-lines, summarize the through-lines, classify the through-lines, visualize the through-lines,
present the through-lines.

## 2. Summarization of the news articles
Building profiles of the articles that facilitate searching, grouping and mining. Storage mirrors in document
format, database format and vector format.
Using a two-layered storage approach, where the full document is linked to the summary.
Summaries using multiple sources to build extra points of view into the summary.

## 3. Classification of the news articles
Building sentiment profiles for articles, summaries etc as they are added to the system.
Each sentiment profile contains metadata about the associated aggregates of the time and/or place of the article.
Sentiment profiles are used to retrieve articles, summaries etc that match the sentiment profile.

## 4. Visualization of the news articles
By storing using "sentiment as key" and "summary as key" allows for the acquisition and visualization of the source
material using rich querying and grouping. The secret sauce is "show me a summary of all the good news stories"
and the machine knows the difference between good news and bad news.

## 5. Presentation of the news articles
BUT -- what if it isn't "the news" ?
WHAT IF -- it's early versions are a "smart feed reader" ?
Using a complicated plugin system to equip the system with the ability to prompt the model for function calls
which can do things like scrape reddit's front page for example.
A group of tiles, each tile is a feed, each feed is a set of articles, each article is a summary, each summary is
a sentiment, each sentiment is a mood, each mood has a bias, each topic has a bias, each topic has a sentiment

## 6. Deployment of the system

