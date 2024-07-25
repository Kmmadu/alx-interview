#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    
    Args:
    data (list): A list of integers representing the data bytes.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            while mask_byte & byte:
                number_bytes += 1
                mask_byte >>= 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        number_bytes -= 1

    return number_bytes == 0

