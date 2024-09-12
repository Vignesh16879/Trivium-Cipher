# Trivium Cipher Test Suite

This project implements a test suite for the Trivium stream cipher using Python. The test suite uses known test vectors and compares the generated keystream with expected values. It includes colorful output for better readability.

## Features:
- Trivium cipher implementation.
- Test suite using provided test vectors.
- Colorful terminal output using `colorama` for test results.

## Prerequisites

Before running the project, ensure you have the following installed:
- **Python 3.x**
- **colorama** package for colored output in the terminal.

You can install `colorama` using pip:
```bash
pip install colorama
```

## How to Run
1. Clone the repository to your local machine.
```bash
git clone https://github.com/Vignesh16879/Trivium-Cipher.git
```
2. Navigate to the project directory.
```bash
cd Trivium-Cipher
```
3. Run the tests using Python:
```bash
python3 test.py
```

## Expected Output
When running the test suite, you will see colored output that shows the generated keystream, the expected keystream, and whether the test passed or failed. Example:
```bash
Starting Trivium Cipher Tests
Running Test Vector 1...
Generated keystream:  0xFBE0 BF26 5859 051B 517A 2E4E 239F C97F ...
Expected keystream:   0xFBE0 BF26 5859 051B 517A 2E4E 239F C97F ...
Test passed!

Running Test Vector 2...
Generated keystream:  0x38EB 86FF 730D 7A9C AF8D F13A 4420 540D ...
Expected keystream:   0x38EB 86FF 730D 7A9C AF8D F13A 4420 540D ...
Test passed!
```

## Project Structure
- trivium.py: Contains the Trivium cipher implementation.
- main.py: Contains the manual input of key & iv for computing the cipher.
- test.py: Contains the test suite for the Trivium cipher.
- README.md: This file, providing instructions on how to set up and run the project.
