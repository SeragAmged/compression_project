from collections import defaultdict
from math import log2, sqrt, ceil, floor
import heapq
import math

from helper import calculate_average_length, calculate_efficiency, calculate_entropy


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# Building the Huffman Tree


def build_huffman_tree(probabilities):
    heap = []

    for char, freq in probabilities.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_frequency = left_node.frequency + right_node.frequency
        merged_node = HuffmanNode(None, merged_frequency)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    return heap[0]

# Assigning the codes for huffman algorithm


def build_huffman_codes(node, current_code, codes):
    if node.char is not None:
        codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)

# Encoding the message using Huffman algorithm


def _huffman_encode(message, probabilities):
    huffman_tree = build_huffman_tree(probabilities)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    encoded_message = ""

    for char in message:
        encoded_message += huffman_codes[char]

    return encoded_message, huffman_codes


def huffman_encode(message, ch_probability):
    # Huffman Encoding
    huffman_encoded_message, huffman_codes = _huffman_encode(
        message, ch_probability)

    # Calculate statistics for Huffman encoding
    huffman_bits_before = len(message) * 8
    huffman_bits_after = len(huffman_encoded_message)
    huffman_compression_ratio = (huffman_bits_before / huffman_bits_after)
    huffman_entropy = calculate_entropy(ch_probability)
    huffman_average_length = calculate_average_length(
        ch_probability, huffman_codes)
    huffman_efficiency = calculate_efficiency(
        huffman_entropy, huffman_average_length)

    return {
        "name": "Huffman",
        'bits_after_compression': huffman_bits_after,
        'compression_ratio': huffman_compression_ratio,
        'average_length': huffman_average_length,
        'efficiency': huffman_efficiency
    }
