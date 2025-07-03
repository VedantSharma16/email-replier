from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/reply', methods=['POST'])
def generate_reply():
    data = request.json
    email_content = data.get('email')

    if not email_content:
        return jsonify({"error": "Missing email content"}), 400

    prompt = f"You're a helpful professional assistant. Write a polite and smart reply to this email:\n\n{email_content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
