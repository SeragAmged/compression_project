from collections import defaultdict
from math import log2


# (1) Calculating the Entropy
def calculate_entropy(probabilities):
    entropy = 0
    for prob in probabilities.values():
        entropy += prob * (-(log2(prob)))
    return entropy

# (2) Calculating the Average Length


def calculate_average_length(probabilities, codes):
    average_length = 0
    for char, prob in probabilities.items():
        average_length += len(codes[char]) * prob
    return average_length

# (3) Calculating the Efficiency


def calculate_efficiency(entropy, average_length):
    return (entropy / average_length) * 100


# Calculating Probabilities
def calculate_probabilities(sequence):
    # Count occurrences of each symbol in the sequence
    symbol_count = defaultdict(int)
    for symbol in sequence:
        symbol_count[symbol] += 1

    # Calculate probabilities
    total_symbols = len(sequence)
    probabilities = {symbol: count / total_symbols for symbol,
                     count in symbol_count.items()}

    return probabilities
