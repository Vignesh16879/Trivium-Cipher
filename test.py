from trivium import *
from colorama import Fore, Style, init


init(autoreset=True)


def test_trivium(key_hex, iv_hex, expected_keystream_hex):
    print(Fore.YELLOW + "KEY: " + Fore.CYAN + f"{key_hex}" + Style.RESET_ALL)
    print(Fore.YELLOW + "IV:  " + Fore.CYAN + f"{iv_hex} " + Style.RESET_ALL)
    key = clean_hex_input(key_hex)
    iv = clean_hex_input(iv_hex)
    expected_keystream = clean_hex_input(expected_keystream_hex)
    # Convert to bits
    KEY = hex_to_bits(key)[::-1]
    IV = hex_to_bits(iv)[::-1]
    # Initialize Trivium with the given key and IV
    trivium = Trivium(KEY, IV)
    # Generate 512 bits (to match the provided keystream length)
    keystream = trivium.keystream(512)
    # Convert keystream to hex
    generated_keystream = bits_to_hex(keystream)
    # Format and print the keystreams with colors
    print(Fore.YELLOW + "Generated keystream:\n", Fore.CYAN + format_hex_output(generated_keystream))
    print(Fore.YELLOW + "Expected keystream:\n",  Fore.CYAN + expected_keystream_hex)
    
    # Check if the test passed
    if generated_keystream == expected_keystream:
        print(Fore.GREEN + "Test passed!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Test failed!" + Style.RESET_ALL)


def RunTest():
    print(Fore.MAGENTA + "Running Test Vector 1..." + Style.RESET_ALL)
    test_trivium(
        key_hex="0x0000 0000 0000 0000 0000",
        iv_hex="0x0000 0000 0000 0000 0000",
        expected_keystream_hex=
                "0xFBE0 BF26 5859 051B 517A 2E4E 239F C97F"
            +   " 5632 0316 1907 CF2D E7A8 790F A1B2 E9CD"
            +   " F752 9203 0268 B738 2B4C 1A75 9AA2 599A"
            +   " 2855 4998 6E74 8059 0380 1A4C B5A5 D4F2"
    )
    
    print(Fore.MAGENTA + "\nRunning Test Vector 2..." + Style.RESET_ALL)
    test_trivium(
        key_hex="0x8000 0000 0000 0000 0000",
        iv_hex="0x0000 0000 0000 0000 0000",
        expected_keystream_hex=
                "0x38EB 86FF 730D 7A9C AF8D F13A 4420 540D"
            +   " BB7B 6514 64C8 7501 5520 41C2 49F2 9A64"
            +   " D2FB F515 6109 21EB E06C 8F92 CECF 7F80"
            +   " 98FF 20CC CC6A 62B9 7BE8 EF74 54FC 80F9"
    )


def main():
    print(Fore.BLUE + Style.BRIGHT + "Starting Trivium Cipher Tests" + Style.RESET_ALL)
    RunTest()


if __name__ == "__main__":
    main()