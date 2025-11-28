# Import necessary libraries
import random
import math
from collections import defaultdict

# Training corpus
sentences = [
    "<s> the cat sat on the mat </s>",
    "<s> it rained heavily last night </s>",
    "<s> flowers bloom in the spring </s>",
    "<s> birds fly over the green valley </s>",
    "<s> she sings beautifully in the choir </s>",
    "<s> he reads a book about the stars </s>",
    "<s> children love to play in the park </s>",
    "<s> they watched a movie last night </s>",
    "<s> music makes people happy </s>"
]

# Build a bigram frequency model
bigrams = defaultdict(lambda: defaultdict(int))

for sentence in sentences:
    words = sentence.split()
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        bigrams[w1][w2] += 1

# Step 3: Convert frequency counts to probabilities
for w1 in bigrams:
    total = float(sum(bigrams[w1].values()))
    for w2 in bigrams[w1]:
        bigrams[w1][w2] /= total


# Step 4: Generate a random sentence using Bigram model
def generate_sentence():
    word = "<s>"
    result = [word]

    while True:
        next_words = list(bigrams[word].keys())
        probabilities = list(bigrams[word].values())

        if not next_words:
            break

        word = random.choices(next_words, weights=probabilities)[0]

        if word == "</s>":
            result.append(word)
            break

        result.append(word)

    return " ".join(result)


# Compute average bigram probability of sentence
def avg_bigram_prob(sentence):
    words = sentence.split()
    probs = []

    for w1, w2 in zip(words[:-1], words[1:]):
        prob = bigrams[w1].get(w2, 0)
        probs.append(prob)

    if len(probs) == 0:
        return 0

    return sum(probs) / len(probs)


# Generate and print 3 random sentences
for i in range(3):
    sent = generate_sentence()
    quality = avg_bigram_prob("<s> " + sent + " </s>")
    print(f"\nSentence {i+1}: {sent}")
    print(f"Average Bigram Probability: {quality:.6f}")
