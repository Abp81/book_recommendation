from flask import Flask, request, jsonify, render_template
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load API key dari .env
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# LangChain LLM dengan API key OpenAI
llm = OpenAI(openai_api_key=openai_api_key)

# Fungsi untuk mendapatkan rekomendasi buku
def get_book_recommendation(age, hobby, job, book_genre):
    prompt = f"Recommend a book for a {age}-year-old who enjoys {hobby}, works as {job}, and prefers {book_genre} books. Include a brief synopsis."
    response = llm.invoke(prompt)
    return response

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk API rekomendasi buku
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    age = data.get('age')
    hobby = data.get('hobby')
    job = data.get('job')
    book_genre = data.get('book_genre')
    
    # Dapatkan rekomendasi buku
    recommendation = get_book_recommendation(age, hobby, job, book_genre)
    
    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True)

