from collections import defaultdict


def _lzw_encode(message):
    dictionary = defaultdict(int)
    max_code = 128
    encoded_message = []
    current_code = ''

    # Step 1: Initialize the dictionary with all single characters
    for i in range(256):
        dictionary[chr(i)] = i

    # Step 2: Encode the message using LZW algorithm
    for char in message:
        current_code += char
        if current_code not in dictionary:
            encoded_message.append(dictionary[current_code[:-1]])
            dictionary[current_code] = max_code + 1
            max_code += 1
            current_code = char

    encoded_message.append(dictionary[current_code])

    # Calculate average length
    original_length = len(message)
    encoded_length = len(encoded_message)
    average_length = encoded_length / original_length
    # Calculate the efficiency
    efficiency = ((original_length - encoded_length) / original_length) * 100

    return encoded_message, average_length, efficiency


def lzw_encode(message, ch_probability):
    # LZW Encoding
    lzw_encoded_message, average_length_lzw, efficiency_lzw = _lzw_encode(
        message)
    # Calculate statistics for LZW encoding
    lzw_bits_before = len(message) * 8
    lzw_bits_after = len(lzw_encoded_message) * \
        (len(bin(max(lzw_encoded_message))) - 2)
    lzw_compression_ratio = (lzw_bits_before / lzw_bits_after)
    lzw_average_length = average_length_lzw
    lzw_efficiency = efficiency_lzw

    return {
        'name': "LZW",
        'bits_after_compression': lzw_bits_after,
        'compression_ratio': lzw_compression_ratio,
        'average_length': lzw_average_length,
        'efficiency': lzw_efficiency
    }
