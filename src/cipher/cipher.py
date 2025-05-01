#!/usr/bin/env python3

"""
    cipher.py

    A super simple encode/decode Caesar Cipher with a 3-left shift
"""

import argparse
import string

def caesar_cipher(text: str, shift: int) -> str:
    """
    Applies a Caesar Cipher to the given text with the specified shift.
    Positive shift encodes, negative shift decodes.
    """
    # Create lists of uppercase and lowercase letters
    uppercase = string.ascii_uppercase  # 'A' to 'Z'
    lowercase = string.ascii_lowercase  # 'a' to 'z'
    
    result = []
    
    for char in text:
        # Encode uppercase letters
        if char in uppercase:
            # Find original position, apply shift, wrap around using modulo
            original_pos = uppercase.index(char)
            shifted_pos = (original_pos + shift) % 26
            result.append(uppercase[shifted_pos])
        # Encode lowercase letters
        elif char in lowercase:
            original_pos = lowercase.index(char)
            shifted_pos = (original_pos + shift) % 26
            result.append(lowercase[shifted_pos])
        else:
            # Non-alphabetical characters are not changed
            result.append(char)
    
    return ''.join(result)

def main():
    parser = argparse.ArgumentParser(description="Encode or decode using a Caesar Cipher.")
    parser.add_argument(
        "mode",
        choices=["encode", "decode"],
        help="Mode: 'encode' or 'decode'.",
    )
    parser.add_argument(
        "text",
        help="The text you want to encode or decode."
    )
    
    args = parser.parse_args()
    
    # Shift of 3 for encoding, and -3 for decoding
    shift = 3 if args.mode == "encode" else -3
    
    # Perform the Caesar Cipher
    transformed_text = caesar_cipher(args.text, shift)
    
    # Print out the result
    print(transformed_text)

if __name__ == "__main__":
    main()