from textblob import TextBlob
from typing import List

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(unsorted: List[int]):
    for i in range(len(unsorted)):
        changed = 0
        for j in range(len(unsorted)-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
                changed = 1
        if changed == 0:
            return unsorted
    return unsorted


