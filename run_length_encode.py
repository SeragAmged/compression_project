from collections import defaultdict
from math import log2, sqrt, ceil, floor
import heapq
import math

# ****************************************** Run Length Algorithm **************************************************************


def _run_length_encode(message):
    encoded = ''
    count = 1
    prev_char = message[0]

    for char in message[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded += str(count) + prev_char
            count = 1
            prev_char = char

    encoded += str(count) + prev_char
    return encoded


def calculate_statistics(original_message, encoded_message):
    bits_before_compression = len(
        original_message) * 8  # Each character is 8 bits
    # Number of unique characters in encoded data * bits needed to represent them
    bits_after_compression = len(encoded_message) * \
        ceil(log2(len(set(encoded_message))))

    compression_ratio = bits_before_compression / bits_after_compression
    efficiency = bits_after_compression / bits_before_compression

    # Calculate entropy
    frequencies = defaultdict(int)
    for char in original_message:
        frequencies[char] += 1
    entropy = sum((freq / len(original_message)) * log2(freq /
                  len(original_message)) for freq in frequencies.values())
    entropy *= -1

    # Average length
    average_length = bits_after_compression / len(original_message)

    return bits_after_compression, compression_ratio, efficiency, average_length


def run_length_encode(message):
    # Run Length Encoding
    rl_encoded = _run_length_encode(message)
    bits_after_compression, compression_ratio, efficiency, average_length = calculate_statistics(
        message, rl_encoded)

    return {
        'name': 'RLE',
        'encoded_message': rl_encoded,
        'bits_after_compression': bits_after_compression,
        'compression_ratio': compression_ratio,
        'average_length': average_length,
        'efficiency': efficiency,
    }
