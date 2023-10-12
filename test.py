import multiprocessing, time

# Function to process a chunk of work
def process_chunk(chunk):
    results = []
    for item in chunk:
        # Perform processing on each item in the chunk
        # and append the result to the results list
        # This is where you would have your nested loop logic
        result = item * 2  # Replace this with your actual processing logic
        results.append(result)
    return results

# Main function to split the work and use multiprocessing
def main():
    num_processes = 4  # Number of parallel processes
    total_work_items = 1000  # Total number of work items
    chunk_size = total_work_items // num_processes  # Chunk size per process

    # Generate the work items (replace this with your actual data)
    work_items = [i for i in range(total_work_items)]

    # Split the work into chunks
    chunks = [work_items[i:i + chunk_size] for i in range(0, total_work_items, chunk_size)]
    start = time.time()
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Map the process_chunk function to the chunks and execute in parallel
        results = pool.map(process_chunk, chunks)

    # Flatten the results and aggregate them
    final_result = [item for sublist in results for item in sublist]
    print(f"Time to run {time.time() - start} Multi processing")
    
if __name__ == "__main__":
    main()