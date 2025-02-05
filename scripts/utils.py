import time
import csv
import os

def log_and_save_modular_exponentiation_approaches(func, approach, base, exponent, modulus, log_file=None):
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
    print(f"{approach}\n==================\nBase: {base}, Exponent: {exponent}, Modulus: {modulus}\nResult: {result}, Execution Time: {execution_time:.6f} seconds")


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
