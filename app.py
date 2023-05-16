from flask import Flask, render_template, request
import openai


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    message = request.form['message']

    try:
        answer = get_chatgpt_response(message)
    except Exception as e:
        answer = f"There was an error: {e}"
    return render_template('results.html',message=message, answer=answer)

def get_chatgpt_response(prompt):
    openai.api_key =("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")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"What is your question? {prompt}\nAnswer:",
        temperature=0.5,
        max_tokens=2048,
        n=2,
        stop=None,
        timeout=10,
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
