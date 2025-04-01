import re
import heapq

def summarize_text(text, num_sentences=3):
    sentences = re.split(r'(?<=[.!?]) +', text)

    word_frequencies = {}
    for word in re.findall(r'\w+', text.lower()):
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.lower().split():
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return " ".join(summary_sentences)
