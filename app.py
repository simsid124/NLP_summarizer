from urllib.request import urlopen
from flask import Flask, redirect, url_for, render_template, request
from nltk_summarizer import summarize_article
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_article_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyse", methods=['GET', 'POST'])
def analyse():
    if request.method == 'POST':
        article_text = request.form['article_text']
        
        final_summary = summarize_article(article_text)

    return render_template("index.html", ctext = article_text, final_summary = final_summary)

@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():
	if request.method == 'POST':
		raw_url = request.form['raw_url']
		article_text = get_article_text(raw_url)
		final_summary = summarize_article(article_text)
	return render_template('index.html',ctext=article_text,final_summary=final_summary)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)