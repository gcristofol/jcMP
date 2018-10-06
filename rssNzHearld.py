import feedparser
from vaderSentiment import SentimentIntensityAnalyzer
import collections

d = feedparser.parse('http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000001.xml')
analyzer = SentimentIntensityAnalyzer()


if __name__ == '__main__':
    
    result = {}
    for post in d.entries:
        print ("\nAnalyze:", post.title)
        print ("Sentence:", post.description)
        vs = analyzer.polarity_scores(post.description)
        print("{:-<65} {}".format(post.title, str(vs)))
        print("Compound:", vs['compound'])
        result[vs['compound']] = post.title

    keylist = result.keys()
    keylist = sorted(result.keys())

    print ("\n %s: %s" % (keylist[0], result[keylist[0]]))
