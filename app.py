from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

# Store URLs in memory (simple for learning)
url_database = {}

def generate_short_code():
    """Generate random 6 character code"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def home():
    return '''
    <h1>URL Shortener</h1>
    <form action="/shorten" method="post">
        <input type="text" name="url" placeholder="Enter long URL" size="50">
        <button type="submit">Shorten</button>
    </form>
    '''

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_code = generate_short_code()
    url_database[short_code] = long_url
    short_url = f"http://localhost:5000/{short_code}"
    return f'<h2>Short URL: <a href="{short_url}">{short_url}</a></h2>'

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    return '<h2>URL not found!</h2>', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
