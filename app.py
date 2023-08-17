from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def find_backlinks(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags
    anchor_tags = soup.find_all('a')

    backlinks = []

    # Extract the href attribute from each anchor tag
    for tag in anchor_tags:
        href = tag.get('href')
        if href and 'http' in href:
            backlinks.append(href)

    return backlinks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_backlinks', methods=['POST'])
def search():
    url = request.form['url']
    backlinks = find_backlinks(url)
    return render_template('results.html', url=url, backlinks=backlinks)

if __name__ == '__main__':
    app.run(debug=True)
