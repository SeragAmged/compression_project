from collections import defaultdict
from math import log2,  ceil


from helper import calculate_efficiency, calculate_entropy


def _arithmetic_encode(sequence, probabilities):
    # Initialize low and high ranges
    low = 0.0
    high = 1.0
    range_size = 1.0

    # Initialize number of bits before encoding
    bits_before = len(sequence) * 8

    # Encode each symbol in the sequence
    for symbol in sequence:
        symbol_low = 0 if symbol == 'a' else sum(
            probabilities[s] for s in probabilities.keys() if ord(s) < ord(symbol))
        symbol_high = probabilities[symbol] + symbol_low

        # Update the range
        low += range_size * symbol_low
        high = low + range_size * (symbol_high - symbol_low)
        range_size *= (symbol_high - symbol_low)

    # Calculate the number of bits after encoding
    bits_after = ceil(-log2(range_size))

    # Return the average of low and high as the encoded value
    encoded_value = (low + high) / 2

    return encoded_value, bits_before, bits_after

# Calculating the Average Length for Arithmetic Encoding


def AR_average_length(sequence, probabilities):
    average_length = 0.0
    for symbol in sequence:
        # Calculate the length of encoded symbol
        symbol_low = 0 if symbol == 'a' else sum(
            probabilities[s] for s in probabilities.keys() if ord(s) < ord(symbol))
        symbol_high = probabilities[symbol] + symbol_low
        length = -log2(symbol_high - symbol_low)
        # Adding to the average length
        average_length += probabilities[symbol] * length

    return average_length


def arithmetic_encode(message, ch_probability):
    # Arithmetic Encoding
    encoded_value, bits_before, bits_after = _arithmetic_encode(
        message, ch_probability)

    # Calculate statistics for Arithmetic encoding
    compression_ratio = (bits_before / bits_after)
    arithmetic_entropy = calculate_entropy(ch_probability)
    average_length = AR_average_length(message, ch_probability)
    efficiency = calculate_efficiency(arithmetic_entropy, average_length)

    return {
        "name": "Arithmetic",
        'encoded_value': encoded_value,
        'bits_after_compression': bits_after,
        'compression_ratio': compression_ratio,
        'average_length': average_length,
        'efficiency': efficiency,
    }
