from collections import defaultdict
from math import log2, sqrt, ceil, floor


def _golomb_encode(n, m):
    # Step 1: Calculate quotient (q) and remainder (r)
    q = n // m
    r = n - q * m

    # Step 2: Represent q in unary code
    quotient_code = '1' * q + '0'

    # Step 3: Representation of r
    if is_power_of_two(m):
        # If m is a power of 2, represent r using log2(m) bits
        remainder_code = format(r, '0' + str(ceil(log2(m))) + 'b')
    else:
        # If m is not a power of 2
        if r < (2 ** ceil(log2(m))) - m:
            # For the first 2^ceil(log2(m)) - m values, use floor(log2(m)) bits
            remainder_code = format(r, '0' + str(floor(log2(m))) + 'b')
        else:
            # For the rest of the values, use log2(m) bits
            remainder_code = format(
                r + (2 ** ceil(log2(m))) - m, '0' + str(ceil(log2(m))) + 'b')

    # Step 4: Codeword generation
    codeword = quotient_code + remainder_code

    return codeword


def is_power_of_two(num):
    return num != 0 and ((num & (num - 1)) == 0)

# ****************************************************** Calculating the Statistics ************************************************

# Calculate statistics for Golomb encoding


def calculate_golomb_statistics(n, m, golomb_encoded):
    # Number of bits in the original integer
    bits_before_compression = len(bin(n)) - 2
    # Number of bits in the Golomb encoded message
    bits_after_compression = len(golomb_encoded)

    compression_ratio = bits_before_compression / bits_after_compression
    efficiency = bits_after_compression / bits_before_compression

    return bits_before_compression, bits_after_compression, compression_ratio, efficiency


def golomb_encode(message):
    # Convert to integer
    n = int(message)

    # Check if the input is binary
    if set(message) <= {'0', '1'}:
        # Convert binary to decimal
        n = int(message, 2)

    # Calculate m as the rounded square root of n
    m = round(sqrt(n))
    # Encode using Golomb coding
    golomb_encoded = _golomb_encode(n, m)
    # print("Golomb code for n =", n, "with m =", m, "is:", golomb_encoded)

    # Calculate statistics for Golomb encoding
    golomb_bits_before, golomb_bits_after, golomb_compression_ratio, golomb_efficiency = calculate_golomb_statistics(
        n, m, golomb_encoded)
    # print("Bits before encoding:", golomb_bits_before)
    # print("Bits after encoding:", golomb_bits_after)
    # print("compression_ratio:", golomb_compression_ratio)
    # print("Efficiency:", golomb_efficiency)

    # return {
    #     'Hi':"world",
    #     'compression_ratio':golomb_compression_ratio,
    # }

    return {
        "name": "Golomb",
        'n': n,
        'm': m,
        'golomb_encoded': golomb_encoded,
        'bits_before_compression': golomb_bits_before,
        'bits_after_compression': golomb_bits_after,
        'compression_ratio': golomb_compression_ratio,
        'efficiency': golomb_efficiency,
    }
