from flask import Flask, render_template, request, jsonify
import json
from llamaapi import LlamaAPI  # Replace with correct import if necessary

# Initialize the LlamaAPI (replace with your key)
llama = LlamaAPI("LA-b98613d185b84e70949e3ece3a460d5f1d5f5403d07a492793b6c2e648c69682")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_instructions', methods=['POST'])
def get_instructions():
    if request.method == 'POST':
        form_data = request.form
        medication_name = form_data.get('medicationName')
        dosage_form = form_data.get('dosageForm')
        body_weight = form_data.get('bodyWeight')
        age = form_data.get('age')

        # Build the LlamaAPI request
        api_request_json = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Provide medication instructions and possible side effects for {medication_name} in the form {dosage_form} for a person weighing {body_weight} kg and aged {age} years."
                }
            ],
            "stream": False
        }

        try:
            # Send request to LlamaAPI
            api_response = llama.run(api_request_json)
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
