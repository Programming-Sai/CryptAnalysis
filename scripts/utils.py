import sympy
import random
import string
import math
import time
import csv
import os
import concurrent.futures



def run_modular_exponentiation_approaches_and_save_results(func, approach, base, exponent, modulus, log_file=None):
    """
    A general function to log the modular exponentiation results, time taken, and save it to a CSV file.
    
    Parameters:
    - func: The function to execute for modular exponentiation.
    - base: The base value for exponentiation.
    - exponent: The exponent value.
    - modulus: The modulus value.
    - log_file: The path to the CSV file where the logs will be saved.
    
    Returns:
    - None
    """
    
    # Default log file path if not provided
    if not log_file:
        log_file = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), 'modular_exponentiation_log.csv')
    
    # Record the start time
    start_time = time.time()

    try:
        # Execute the modular exponentiation function
        result = func(base, exponent, modulus)
    except Exception as e:
        print(f"Error executing the function: {e}")
        return

    # Calculate the time taken
    end_time = time.time()
    execution_time = end_time - start_time

    # Log the results (printing to console)
    with open(os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), "modular_exponentiation_output.txt"), "a") as f:
        print(f"{approach}\n==================\nBase: {base}, Exponent: {exponent}, Modulus: {modulus}\nResult: {result}, Execution Time: {execution_time:.6f} seconds\n\n")
        f.write(f"{approach}\n==================\nBase: {base}, Exponent: {exponent}, Modulus: {modulus}\nResult: {result}, Execution Time: {execution_time:.6f} seconds\n\n")



    # Save the results to a CSV file
    # Check if the log file exists, if not, create the file and write the header
    file_exists = False
    try:
        with open(log_file, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    # If file doesn't exist, create the file and add header
    if not file_exists:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Ensure the data directory exists
        with open(log_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Approach', 'Base', 'Exponent', 'Modulus', 'Result', 'Execution Time (seconds)'])

    # Append the result to the CSV file
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([approach, base, exponent, modulus, result, execution_time])



def run_rsa_decryption_and_save_results(func, label, p, q, e, filename=None):
    """
    Run the brute force calculation for d and save the results to a CSV file.
    This function calls brute_force_d, displays the result, and saves it.
    """
    # Call the brute_force_d function
    if not filename:
        filename = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), 'rsa_log.csv')
    
    d, elapsed_time = func(p, q, e)

    with open(os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), "rsa_output.txt"), "a") as f:
        print(f"{label}\n==================\np: {p}, q: {q}, e: {e}\nd: {d}, Execution Time: {elapsed_time:.6f} seconds\n\n")
        f.write(f"{label}\n==================\np: {p}, q: {q}, e: {e}\nd: {d}, Execution Time: {elapsed_time:.6f} seconds\n\n")

    file_exists = False
    try:
        with open(filename, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    # If file doesn't exist, create the file and add header
    if not file_exists:
        os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure the data directory exists
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['No of Digits', 'p', 'q', 'e', 'd', 'Execution Time (seconds)'])

    # Append the result to the CSV file
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([label, p, q, e, d, elapsed_time])







def is_prime(n):
    """Return True if n is prime (simple trial division)."""
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Compute the greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Return tuple (g, x, y) such that ax + by = g = gcd(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(e, phi):
    """Compute the modular inverse of e mod phi using the Extended Euclidean Algorithm."""
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def generate_prime(digits):
    """Generates a random prime number with the specified number of digits."""
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return sympy.randprime(lower, upper)


def convurrent_running():
    prime_pairs = {
        "2-digit": (43, 59),
        "4-digit": (1009, 1013),
        # "6-digit": (100003, 100019),
        # "8-digit": (10000019, 10000079),
        # "10-digit": (1000000007, 1000000009)
    }
    
    e_val = 13
    filename = os.path.join(os.getcwd(), 'rsa_log.csv')

    
    print("Starting brute-force d computation in parallel...")

    # Use ThreadPoolExecutor to run in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(run_rsa_decryption_and_save_results, label, p, q, e_val, filename): label
            for label, (p, q) in prime_pairs.items()
        }
        
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Ensure completion before exiting




def generate_random_code(length: int, alphanumeric=False):
    characters = string.digits if not alphanumeric else string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))



def run_brute_force_password_cracking_tests_and_save_results(func, label, code, length, save_path=None):

    if not save_path:
        save_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), f'{length}_character_password_cracking_log.csv')
    
    elapsed_time = func(code, length)
    
    with open(os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data')), f'{length}_character_password_cracking_log.txt'), "a") as f:
        print(f"{label}\n==================\ncode: {code}, length: {length}, Execution Time: {elapsed_time:.6f} seconds\n\n")
        f.write(f"{label}\n==================\ncode: {code}, length: {length}, Execution Time: {elapsed_time:.6f} seconds\n\n")


    file_exists = False
    try:
        with open(save_path, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    if not file_exists:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure the data directory exists
        with open(save_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Length', 'Type', 'Code', 'Time (seconds)'])


    with open(save_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([length, label, code, elapsed_time])
    
    print(f"Results saved to {save_path}")

