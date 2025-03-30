import string

def censor(words):
    words_to_censor = {'beach', 'peach', 'ginger'}
    new_words = words.split()
    censored_text = []

    for word in new_words:
        cleared_word = word.strip(string.punctuation)
        if cleared_word.lower() in words_to_censor:
            censored_text.append(len(cleared_word) * '*')
        else:
            censored_text.append(word)
    return ' '.join(censored_text)

