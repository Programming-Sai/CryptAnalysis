import time 
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Handle base greater than modulus

    while exponent > 0:
        # If exponent is odd, multiply the current base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Now exponent must be even, square the base and halve the exponent
        exponent = exponent // 2
        base = (base * base) % modulus

    return result
def modular_exponentiation1(base,exponent,modulus):
    print(f"To calculate the {base}^{exponent} mod {modulus}")
    starting_time= time.time()
    Direct_calculation_result = (base ** exponent)%modulus
    Terminating_time=  time.time()
    Direct_time_estimate = Terminating_time - starting_time
    print(f"Time it took for direct calculation:Output={Direct_calculation_result}, Time={Direct_time_estimate:.6f} seconds") 
    #Modular time calculation when function was used
    starting_time= time.time()
    Modular_calculation_result = modular_exponentiation(base,exponent,modulus)
    Terminating_time=  time.time()
    Modular_time_estimate = Terminating_time - starting_time
    print(f"Time it took for Modular exponentiation function calculation:Output ={Modular_calculation_result}, Time={Modular_time_estimate:.6f} seconds")
    #Using pythons built in %  function
    starting_time= time.time()
    Python_calculation_result = pow(base,exponent,modulus)
    Terminating_time=  time.time()
    Python_time_estimate = Terminating_time - starting_time
    print(f"Time it took for Modular exponentiation function calculation:Output ={Python_calculation_result}, Time={Python_time_estimate:.6f} seconds")
    return Direct_calculation_result,Modular_calculation_result,Python_calculation_result,Direct_time_estimate,Modular_time_estimate,Python_time_estimate

# Test the function for 3^644 mod 645
base = 3
exponent = 644
modulus = 645

result = modular_exponentiation(base, exponent, modulus)
print(f"3^644 mod 645 = {result}")
# Example for 7^121 mod 13
base = 7
exponent = 121
modulus =13
Direct_calculation_result,Modular_calculation_result,Python_calculation_result,Direct_time_estimate,Modular_time_estimate,Python_time_estimate = modular_exponentiation1(base,exponent,modulus)
# Checking to see if they all return the same answer
assert Direct_calculation_result == Modular_calculation_result == Python_calculation_result

#Displaying the speed of each of them
print("Speed:")
print(f"Direct_calculation:{Direct_time_estimate:6.f} seconds")
print(f"Modular_calculation:{Modular_time_estimate:6.f} seconds")
print(f"Python_calculation:{Python_time_estimate:6.f} seconds")
# Trying to figure out the slowest or greatest speed
if Direct_time_estimate > Modular_time_estimate and Python_time_estimate:
    print("Direct calulation is the slowest")
elif Modular_time_estimate > Python_time_estimate and Direct_time_estimate:
    print("Modular exponentiation formular is the slowest, hence its best to use that")
else:
    print("Python built in % modular is most efficient since it is the slowest ")



