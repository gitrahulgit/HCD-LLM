import subprocess
import time

def execute_script(script_path, iterations, delay):
    """
    Execute a Python script multiple times with a delay between each run.

    Parameters:
        script_path (str): The path to the Python script to execute.
        iterations (int): Number of times to execute the script.
        delay (int): Delay in seconds between executions.
    """
    for i in range(iterations):
        print(f"Starting iteration {i + 1}...")
        try:
            subprocess.run(["python", script_path], check=True)
            print(f"Iteration {i + 1} completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during iteration {i + 1}: {e}")
        
        if i < iterations - 1:  # Delay only if it's not the last iteration
            print(f"Waiting for {delay} seconds before the next run...")
            time.sleep(delay)
    print("All iterations completed.")

if __name__ == "__main__":
    script_to_execute = r"D:\llm_exam\next_steps\LANGGRAPH\Complete\main_lg.py"  # Replace with the actual path to your script
    total_iterations = 4
    delay_between_runs = 30  # in seconds

    execute_script(script_to_execute, total_iterations, delay_between_runs)