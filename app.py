from flask import Flask, render_template, request, url_for
import nltk
nltk.download('punkt')
nltk.download('stopswords')
from emot.emo_unicode import UNICODE_EMOJI
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import re
import joblib

app = Flask(__name__)

# Function for converting emojis into word
def convert_emojis(text):
    for emot in UNICODE_EMOJI:
        text = text.replace(emot, "_".join(UNICODE_EMOJI[emot].replace(",","").replace(":","").split()))
    return text

def remove_punct(x):
    import string
    punct_tag=set(string.punctuation)
    t=[i for i in x if i not in punct_tag]
    return t

def tokenize(x):
    return word_tokenize(x)

def whites(x):
    w={' '}
    x=[i for i in x if i not in w]
    return x

def re_stop(x):
    nltk_stopwords = nltk.corpus.stopwords.words("english")
    return [ token for token in x if token not in nltk_stopwords]

def remove_num(data):
    data=' '.join(data)
    tag=re.compile(r'[0-9]+')
    data=tag.sub(r' ',data)
    return data

def remove_roman(data):
    en_tag =re.compile(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    data=en_tag.sub(r' ',data)
    return data

def remove_redun(data):
    red_tag=re.compile(r'[?<=(  )\\]|[&&|\|\|-]')
    data=red_tag.sub(r' ',data)
    data=data.split(" ")
    return data


def stemm(x):
    l=[]
    for i in x:
        l.append(PorterStemmer().stem(i))
    return l  



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def submit_text():
    if request.method == 'POST':
        text = request.form.get('text')
        text = text.lower()
        text = convert_emojis(text)
        text = tokenize(text)
        text = remove_punct(text)
        text = whites(text)
        text = re_stop(text)
        text = remove_num(text)
        text = remove_roman(text)
        text = remove_redun(text)
        text = stemm(text)
        text = ' '.join(text)
        text = [text]
        tfidf_filename = "./tfidf_vectorizer.pkl"
        loaded_tfidf = joblib.load(tfidf_filename)
        x = loaded_tfidf.transform(text).toarray()
        model = pickle.load(open('./your_model.pkl', 'rb'))
        result = model.predict(x)
        res = ""
        if result[0]==0:
            res = "JOY"
        elif result[0]==1:
            res = "NETURAL"
        elif result[0]==2:
            res = "OPTIMISM"
        else:
            res = "UPSET"
    return render_template('index.html', text = res)


if __name__ == '__main__':
    app.run(debug=True)
