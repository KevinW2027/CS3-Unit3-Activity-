from flask import Flask, render_template, request, json

app= Flask(__name__)

MYTH_DATA = {
    "gods":[
       {"id": "zeus", "name": "Zeus", "pantheon": "Greek", "domain": "Sky & Thunder", "desc": "King of the Olympians."},
        {"id": "odin", "name": "Odin", "pantheon": "Norse", "domain": "Wisdom & War", "desc": "The All-Father of the North."},
        {"id": "ra", "name": "Ra", "pantheon": "Egyptian", "domain": "The Sun", "desc": "The ancient sun god of Heliopolis."}
    ]
}

@app.route("/")

def home():
    return render_template('index.html')

@app.route('/browse', methods=['GET','POST'])
def browse():
    display_gods = MYTH_DATA['gods']
    if request.method == 'POST':
        selection = request.form.get('pantheon')
        if selection:
            display_gods = []

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
