import transformers
import torch

# Load the summarization model (assuming a Hugging Face model)
model_name = "t5-small"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_response(response):
    # Tokenize the response
    input_ids = tokenizer.encode(response, return_tensors="pt")

    # Generate the summarized response
    summary_ids = model.generate(input_ids, num_beams=4, max_length=50, early_stopping=True)
    summarized_response = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Return the summarized response
    return summarized_response
