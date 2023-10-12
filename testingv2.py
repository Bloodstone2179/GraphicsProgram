import numpy as np
import multiprocessing
def hexify(hexString : int, prefix : bool):
    if prefix == True:
        return "0x{:02x}".format(hexString)
    if prefix == False:
        return "0x{:02x}".format(hexString).removeprefix("0x")
# Function to process a chunk of work (a row in this example)
def process_row(row):
    string = b""
    # Convert each element in the row (y-axis data) to a binary string
    for x in row:
        for y in x:
              # Convert each element to a binary string
            string += y[0] + y[1] + y[2]
    print(string)
    return string

# Main function to split the work and use multiprocessing
def main():
    num_processes = 50  # Number of parallel processes
    rows, cols = 200, 200  # Size of the 2D array

    # Generate a sample 2D array (replace this with your actual data)
    array = np.array([[[bytes.fromhex(hexify(255, False)),bytes.fromhex(hexify(255, False)), bytes.fromhex(hexify(255, False))]] * rows] * cols, dtype=object)

    # Split the work into rows
    chunks = np.array_split(array, num_processes, axis=0)

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Map the process_row function to the chunks (rows) and execute in parallel
        results = pool.map(process_row, chunks)

    # Concatenate the results to form the final 2D list of binary strings
    final_result = results  # Flatten the list
    open("output.txt", "wb").write(results[0])
    print("Sample processed row:", final_result[0])  # Print a sample processed row

if __name__ == "__main__":
    main()