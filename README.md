# 4chan-Sentiment-Alignment

Webscrape and analysis in Python using Requests, BeautifulSoup, Pandas, Matplotlibs, and Google Cloud's Natural Language API

![keyword]()
![keyword]()

### Goal

The goal of this program for me is to better understand webscraping and its practical uses. In this program, [4chan](http://www.4chan.org/) is webscraped in order to return an overall sentiment for uses in analysis or research. 

At its core, the program allows for the user to check the overall sentiment value of 4chan over the span of years provided that enough data has been collected over the time span.

### Concept

The program scrapes through all of 4chan's boards and cycles through the 1st 10 pages. Within each page, each post's text is scraped and is run through the natural language api to get its sentiment value. This results in getting an overall sentiment value from within the entirity of the forum.

All results are formatted into json to which an analyzer converts the output into pandas then through matplotlibs for a visual representation.

### Features

Research and analysis oriented

Formatted to JSON  
Plots provided by matplotlibs

### Reference

[Concept](https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/)
