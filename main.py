from trivium import *


def main():
    # Take Key & IV as input
    key_hex = input("KEY (in hex): ")
    iv_hex = input("IV (in hex): ")
    # Clean the input
    key = clean_hex_input(key_hex)
    iv = clean_hex_input(iv_hex)
    # Convert to bits
    KEY = hex_to_bits(key)[::-1]
    IV = hex_to_bits(iv)[::-1]
    # Initialize Trivium with the given key and IV
    trivium = Trivium(KEY, IV)
    # Generate 512 bits (to match the provided keystream length)
    keystream = trivium.keystream(512)
    # Convert keystream to hex
    keystream = bits_to_hex(keystream)
    # Format and print the keystreams
    print("Keystream: ", format_hex_output(keystream))



if __name__ == "__main__":
    main()