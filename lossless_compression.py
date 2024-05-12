from arithmetic_encode import arithmetic_encode
from golomb_encode import golomb_encode
from helper import calculate_entropy, calculate_probabilities
from huffman_encode import huffman_encode
from lzw_encode import lzw_encode
from run_length_encode import run_length_encode


def lossless_compression(message):
    # Calculate probabilities
    ch_probability = calculate_probabilities(message)

    results = {
        "analysis": {
            'probabilities': ch_probability,
            'entropy': calculate_entropy(ch_probability),


        },
        "compressions": [
            run_length_encode(message),
            arithmetic_encode(message, ch_probability),
            huffman_encode(message, ch_probability),
            lzw_encode(message, ch_probability)

        ],
        #    "compressions": {'RLE': run_length_encode(message),
        #     'Arithmetic':arithmetic_encode(message,ch_probability),
        #     'Huffman':huffman_encode(message,ch_probability),
        #     'LZW': lzw_encode(message,ch_probability)
        #     }
    }
    # Define the list of algorithms with their compression ratios
    algorithms = [
        {
            'name': 'RLE',
            'compression_ratio': run_length_encode(message)['compression_ratio']
        },
        {
            'name': 'LZW',
            'compression_ratio': lzw_encode(message, ch_probability)['compression_ratio']
        },
        {
            'name': 'Huffman',
            'compression_ratio': huffman_encode(message, ch_probability)['compression_ratio']
        },
        {
            'name': 'Arithmetic',
            'compression_ratio': arithmetic_encode(message, ch_probability)['compression_ratio']
        },
    ]

    # Add Golomb encoding if the input is an integer
    if message.isdigit():
        algorithms.append({
            'name': 'Golomb',
            # Add the Golomb compression ratio here
            'compression_ratio': golomb_encode(message)['compression_ratio']
        })
        results['compressions'].append(golomb_encode(message))
    else:
        results['analysis'].update({"bits": len(message)*8})

    # Sort the algorithms by compression ratio in descending order
    algorithms.sort(key=lambda x: x['compression_ratio'], reverse=True)

    # Determine the algorithm with the best compression ratio
    best_algorithm = algorithms[0]['name']

    results.update({'best_algorithm': best_algorithm})

    return results
