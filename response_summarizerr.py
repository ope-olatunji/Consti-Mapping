from flask import Flask, request, jsonify
import sqlite3
import transformers
import torch

# Load the summarization model (assuming a Hugging Face model)
model_name = "t5-small"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Connect to the database
conn = sqlite3.connect('myapp.db')
c = conn.cursor()

# Initialize the Flask app
app = Flask(__name__)

# Define the command endpoint
@app.route('/command', methods=['POST'])
def command():
    # Get the command from the request
    command = request.form['command']

    # Search the database for the response
    c.execute("SELECT * FROM my_table WHERE command=?", (command,))
    result = c.fetchone()

    # If the command is not found, return a default response
    if not result:
        return "Sorry, I didn't understand your command."

    # Get the response from the database and summarize it using the model
    response = result[1]
    summarized_response = summarize_response(response)

    # Return the summarized response as a JSON object
    return jsonify({'response': summarized_response})

def summarize_response(response):
    # Tokenize the response
    input_ids = tokenizer.encode(response, return_tensors="pt")

    # Generate the summarized response
    summary_ids = model.generate(input_ids, num_beams=4, max_length=50, early_stopping=True)
    summarized_response = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Return the summarized response
    return summarized_response

# Run the Flask app
if __name__ == '__main__':
    app.run()
