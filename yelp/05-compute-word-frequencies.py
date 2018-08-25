from toolz.dicttoolz import assoc_in
from database import Review
from nltk.tokenize import word_tokenize
import json

def word_frequency(word, business_ids):
    reviews = Review.where_in('business_id', business_ids).lists('content')
    return len(
        list(
            filter(
                lambda r: word in word_tokenize(r),
                reviews
            )
        )
    )

def add_word_data(word, key, value):
    freq = word_frequency(word, value['business_ids'])
    return assoc_in(
        value,
        ['word_data', word],
        freq
    )

def add_word(word):
    old = json.loads(open('results/new_york.json').read())
    new = { key: add_word_data(word, key, value) for (key, value) in old.items() }
    with open('results/new_york.json', 'w') as outfile:
        json.dump(new, outfile)
