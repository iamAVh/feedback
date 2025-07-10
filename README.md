# Feedback Paraphrasing using Ollama Models

This project uses Ollama language models to generate paraphrased feedback summaries from player feedback data stored in a CSV file. It processes each feedback entry, sends prompts to multiple Ollama models in round-robin fashion, and saves the paraphrased outputs back to the CSV.

---

## 📋 Project Overview

- Reads a CSV file containing player feedback
- For each feedback entry, extracts relevant information about preparation, posture, and execution
- Sends the feedback to two different Ollama models (`falcon` and `mistral`) to generate paraphrased summaries
- Stores both long and short paraphrased feedback back into new columns in the CSV file
- Updates the CSV file incrementally after processing each row

---

## ⚙️ How It Works

1. The script reads input feedback data from a CSV file specified by the `csv_path` variable.
2. It iterates over each row in the dataset.
3. For each row, it constructs prompt strings focusing on the player's preparation, posture, and execution.
4. These prompts are sent to two Ollama models using the command-line interface via Python's `subprocess` module.
5. The returned paraphrased feedback is stored in new columns: `long_paraphrased` and `short_paraphrased`.
6. The CSV file is saved after each row is processed to preserve progress.

---

## 🛠 Prerequisites

- Python 3.x  
- [Ollama CLI](https://ollama.com/) installed and configured with models named `falcon` and `mistral`  
- Required Python packages:  
  - pandas

Install pandas via pip if you don't have it already:

