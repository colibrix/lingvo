import shelve
import string
import nltk
from nltk import word_tokenize
from nltk.stem.snowball import PorterStemmer

# for initial forms
ps = PorterStemmer()
from nltk.stem.wordnet import WordNetLemmatizer

wnl = WordNetLemmatizer()


# SAVING MODE : FREQUENCY, TAG, INITIAL FORM
def create_small_dictionary(input_file):
    new_small_dictionary = {}
    textFile = open(input_file, 'r')
    text = textFile.read()
    textFile.close()

    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)

    for word, tag in tagged_words:
        word = word.lower()
        if word in new_small_dictionary:
            # recount frequency
            frequency = new_small_dictionary[word][0]
            frequency += 1
            new_small_dictionary[word][0] = frequency

            # tags of word
            current_tag_string = new_small_dictionary[word][1]
            current_tags = current_tag_string.split(' ')

            # add new tags, if it not in str
            if tag not in current_tags:
                current_tag_string += " " + tag
                new_small_dictionary[word][1] = current_tag_string

        else:   # add new word with frequency equals 1, current tag, initial form
            initialForm = wnl.lemmatize(word)
            new_small_dictionary[word] = [1, tag, initialForm]

    return new_small_dictionary


def create_small_dictionary_text(input_text):
    new_small_dictionary = {}
    text = input_text

    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)

    for word, tag in tagged_words:
        word = word.lower()
        if word in new_small_dictionary:
            # recount frequency
            frequency = new_small_dictionary[word][0]
            frequency += 1
            new_small_dictionary[word][0] = frequency

            # tags of word
            current_tag_string = new_small_dictionary[word][1]
            current_tags = current_tag_string.split(' ')

            # add new tags, if it not in str
            if tag not in current_tags:
                current_tag_string += " " + tag
                new_small_dictionary[word][1] = current_tag_string

        else:   # add new word with frequency equals 1, current tag, initial form
            initialForm = wnl.lemmatize(word)
            new_small_dictionary[word] = [1, tag, initialForm]

    return new_small_dictionary


def serialization(dictionary, output_file):
    serializer = shelve.open(output_file)
    for key in dictionary:
        serializer[key] = dictionary[key]


def deserialization(input_file):
    dictionary = shelve.open(input_file)
    return dictionary


def newTagString(current_tags, new_tags, new_tag_string):
    result_tag_string = new_tag_string
    for cur_tag in current_tags:
        if cur_tag not in new_tags:
            result_tag_string += " " + cur_tag

    return result_tag_string


def addTextInDictionary(current_dictionary, new_dictionary):
    for word in current_dictionary:
        word = word.lower()
        if word in new_dictionary:
            # frequency
            frequency = new_dictionary[word][0]
            frequency += current_dictionary[word][0]
            #new_dictionary[word][0] = frequency

            # tags
            current_tags = current_dictionary[word][1].split(' ')
            current_tag_string = new_dictionary[word][1]
            new_tags = current_tag_string.split(' ')

            new_tag_string2 = newTagString(current_tags, new_tags, current_tag_string)
            #new_dictionary[word][1] = new_tag_string2

            new_dictionary[word] = [frequency, new_tag_string2, new_dictionary[word][2]]
        else:
            new_dictionary[word] = [current_dictionary[word][0], current_dictionary[word][1],
                                    current_dictionary[word][2]]
    return new_dictionary
            # print("Adding of new text in dictionary was completed.")
