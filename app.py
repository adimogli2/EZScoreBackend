from flask import Flask, request, jsonify, render_template, redirect, url_for
import openai

app = Flask(__name__)

# Set your API keys
openai.api_key = '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'

@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    #return render_template("index.html")
    return redirect("static/index.html")

@app.route('/grade', methods=['POST'])
def grade_paragraph():
    data = request.json
    paragraph = data['paragraph']
    rubric = data['rubric']

    prompt = f"Grade this paragraph on the following rubric: {paragraph} {rubric}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    openai_response = response.choices[0].message['content']

    return jsonify({'feedback': openai_response})

if __name__ == '__main__':
    app.run(debug=True)