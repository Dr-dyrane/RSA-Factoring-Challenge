# RSA Factoring Challenge

This repository contains solutions to the RSA Factoring Challenge. The challenge involves factorizing natural numbers into a product of two smaller numbers. The goal is to find the factors within a time limit of 5 seconds.

## Files

- `factors.py`: This script takes a file as input and factors each number into two smaller numbers. The factors don't have to be prime numbers.

- `rsa.py`: This script is a modified version of `factors.py` specifically for the RSA Factoring Challenge. It factors a given RSA number into two prime numbers.

## Usage

To use the scripts, follow the instructions below:

1. Clone the repository:

   ```
   git clone https://github.com/Dr-dyrane/RSA-Factoring-Challenge.git
   ```

2. Change into the repository directory:

   ```
   cd RSA-Factoring-Challenge
   ```

3. Run the `factors.py` script with a file containing natural numbers to factorize:

   ```
   python factors.py <file>
   ```

   Replace `<file>` with the path to the file containing the numbers. The script will output the factorization for each number.

4. Run the `rsa.py` script with a file containing RSA numbers:

   ```
   python rsa.py <file>
   ```

   Replace `<file>` with the path to the file containing the RSA numbers. The script will output the factorization, ensuring that the factors are prime numbers.

## Example

For example, if you have a file named `numbers.txt` containing the following numbers:

```
6
77
239821585064027
```

You can run the `rsa.py` script as follows:

```
python rsa.py numbers.txt
```

The script will output:

```
6=2*3
77=7*11
239821585064027=15485867*15486481
```

## Limitations

Please note that the provided scripts use simple factorization algorithms and may not be optimized for larger numbers. While they should work within the given time limit, extremely large numbers may require more efficient algorithms for factorization.
