import subprocess
import pandas as pd

# Function to interact with a model in Ollama and get paraphrased output
def run_model(model_name, input_text):
    process = subprocess.Popen(
        ["ollama", "run", model_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    stdout, stderr = process.communicate(input=input_text)
    if stderr:
        print(f"Error in model {model_name}: {stderr}")
    return stdout.strip()

# Path to the input CSV file
csv_path = r'C:\Users\Hp\Downloads\feedback\sample - Sheet1 - sample - Sheet1.csv.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# List of models to use in round-robin order
models = ["falcon", "mistral"]

# Process each row in the dataframe
for index, row in df.iterrows():
    # Convert feedback list to string if it's in list format
    feedback_list = eval(row['feedback']) if isinstance(row['feedback'], str) and row['feedback'].startswith('[') else row['feedback']
    feedback = " ".join(feedback_list) if isinstance(feedback_list, list) else feedback_list

    # Construct the feedback prompts based on posture, execution, and preparation only
    long_feedback_prompt = (
        f"Provide a concise feedback summary on the player's preparation, posture, and execution. "
        f"Feedback: {feedback}. Include brief suggestions."
    )
    short_feedback_prompt = (
        f"Provide a concise feedback summary on the player's preparation, posture, and execution. "
        f"Feedback: {feedback}. Include brief suggestions."
    )

    # Run the model to get the paraphrased feedback
    long_paraphrased_feedback = run_model(models[0], long_feedback_prompt)
    short_paraphrased_feedback = run_model(models[1], short_feedback_prompt)

    # Save results to new columns in the DataFrame
    df.at[index, 'long_paraphrased'] = long_paraphrased_feedback
    df.at[index, 'short_paraphrased'] = short_paraphrased_feedback

    # Save the DataFrame back to the CSV after each row
    df.to_csv(csv_path, index=False)
    print(f"Processed row {index + 1}/{len(df)}: Saved long and short paraphrased feedback.")

print(f"All feedback updated and saved to {csv_path}")
