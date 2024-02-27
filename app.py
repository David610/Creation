from flask import Flask, request, jsonify, render_template  # Added render_template here
from flask_socketio import SocketIO
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

app = Flask(__name__)
socketio = SocketIO(app)

# Set random seed for consistent results
set_seed(11111)

# Load tokenizer and model for 'distilgpt2'
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Ensure the model is in evaluation mode
model.eval()

# If CUDA is available, move the model to GPU
if torch.cuda.is_available():
    model.to("cuda")

@app.route('/')
def home():
    return render_template('index.html')  # Corrected this line

@socketio.on('connect', namespace='/ws')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/ws')
def handle_disconnect():
    print('Client disconnected')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')  # Safely get the prompt, default to empty string if not found
    
    if not prompt:
        return jsonify({'error': 'Empty prompt provided'}), 400
    
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Move inputs to the same device as model
    inputs = {key: value.to(model.device) for key, value in inputs.items()}
    
    outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(port=5500)  # Consider removing `debug=True` in production
