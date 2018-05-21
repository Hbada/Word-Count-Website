from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html') # second method I learned
# OMG it works, locally of course

# my own page creation, using the first method I learned
def nopage(request):
    return HttpResponse('<h1>This is a page-content experiment</h1>This page has content but no .html file. It is loaded straight from an HttpResponse.')

# HTML gets stored elsewhere as a template

# brief example of inserting Python code
def about(request):
    return render(request, 'about.html', {'job': 'I work at my own freelancing business', 'school': 'I graduated with a BA in 2009'})

# make home page submit button load count.html
def count(request):
    fulltext = request.GET['fulltext']
    # 'fulltext' refers to name assigned to textarea in home page form
    print(fulltext) # prints to terminal

    # count the words
    wordlist = fulltext.split() # split the data into list of words
    # now length of wordlist is the count

    # create dictionary with words and their counts
    worddictionary = {} # empty dictionary

    # count each word
    for word in wordlist:
        if word in worddictionary:
            # increase count for that word
            worddictionary[word] += 1 # increase by 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    # sort items before rendering each item
    # in reverse order & based on count using key=
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'counttotal':len(wordlist), 'worddictionary':sortedWords}) # .items() makes it a list for web page
    # 'fulltext' is a string for key, and fulltext is the variable
