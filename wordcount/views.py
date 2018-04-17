from django.http import HttpResponse
from django.shortcuts import render # this is for calling the "templates" folder and the HTMLs inside it
import operator

def homepage(request):
    #return HttpResponse('Hello')
    #return render(request, 'home.html') # the "request" object and send back the home.html page
    return render(request, 'home.html', {'hithere':'This is me'}) # putting a dictionary (passing a custom information)

# def eggs(request):
#     return HttpResponse('<h1>Eggs are great!</h1>')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext) # for printing in the terminal
    # return render(request, 'count.html')

    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    # We use .items() for converting a dictionary into a list.
    # We say with this "key = operator.itemgetter(1)" look at the count which if
    # we are going from zero based counting like 0 1 it's saying look at the values
    # that are inside of there. Other resource, look in the title "Answer for Python beginners" in
    # the link= https://stackoverflow.com/questions/18595686/how-does-operator-itemgetter-and-sort-work-in-python
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)

    # Below, instead of "'worddictionary':worddictionary.items" we can put directly this "'worddictionary':worddictionary"
    # or with paranthesis, ".items()". But, if we want to work the next code (for loop) that is for the code in the count.html file:
    # <h2> Another way for WORD COUNT </h2>    we need to put ".items" without parenthesis "'worddictionary':worddictionary.items".
    # return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items})
    # another way:
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
