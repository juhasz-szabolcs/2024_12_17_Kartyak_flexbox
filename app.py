from flask import Flask, render_template

app = Flask(__name__)

# Route az alapértelmezett oldalhoz
@app.route('/')
def home():
    return render_template('index.html')

# Route a "Kezdőlap" linkhez
@app.route('/kezdolap')
def kezdolap():
    return "Üdvözlünk a Kezdőlapon!"

# Route a "Rólunk" linkhez
@app.route('/rolunk')
def rolunk():
    return "Ez az oldal rólunk szól."

# Route a "Kapcsolat" linkhez
@app.route('/kapcsolat')
def kapcsolat():
    return "Ez a kapcsolat oldal."

if __name__ == '__main__':
    app.run(debug=True)
