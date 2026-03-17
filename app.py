from flask import Flask, render_template, request, json
import random
app= Flask(__name__)

MYTH_DATA = {
    "gods":[
       {"id": "zeus", "name": "Zeus", "pantheon": "Greek", "domain": "Sky", "tier": "Supreme", "icon": "⚡", "desc": "Ruler of the Olympians and god of thunder."},
        {"id": "odin", "name": "Odin", "pantheon": "Norse", "domain": "Wisdom", "tier": "Supreme", "icon": "👁️", "desc": "The All-Father who sacrificed an eye for universal knowledge."},
        {"id": "ra", "name": "Ra", "pantheon": "Egyptian", "domain": "Sun", "tier": "Supreme", "icon": "☀️", "desc": "The sun god who sails across the sky in a golden bark."},
        {"id": "amaterasu", "name": "Amaterasu", "pantheon": "Japanese", "domain": "Universe", "tier": "Supreme", "icon": "⛩️", "desc": "The solar goddess from whom the Japanese Imperial family claims descent."},
        {"id": "poseidon", "name": "Poseidon", "pantheon": "Greek", "domain": "Sea", "tier": "Major", "icon": "🔱", "desc": "The Earth-Shaker and ruler of the deep oceans."},
        {"id": "athena", "name": "Athena", "pantheon": "Greek", "domain": "Strategy", "tier": "Major", "icon": "🦉", "desc": "Goddess of wisdom, craft, and the disciplined side of war."},
        {"id": "thor", "name": "Thor", "pantheon": "Norse", "domain": "Thunder", "tier": "Major", "icon": "🔨", "desc": "The protector of mankind and wielder of the hammer Mjolnir."},
        {"id": "anubis", "name": "Anubis", "pantheon": "Egyptian", "domain": "Dead", "tier": "Major", "icon": "⚖️", "desc": "The jackal-headed god who weighs hearts in the afterlife."},
        {"id": "hermes", "name": "Hermes", "pantheon": "Greek", "domain": "Trade", "tier": "Lesser", "icon": "🥾", "desc": "The fleet-footed messenger and patron of travelers and thieves."},
        {"id": "loki", "name": "Loki", "pantheon": "Norse", "domain": "Mischief", "tier": "Lesser", "icon": "🐍", "desc": "A trickster god known for causing chaos among the Aesir."},
        {"id": "bastet", "name": "Bastet", "pantheon": "Egyptian", "domain": "Cats", "tier": "Lesser", "icon": "🐱", "desc": "A fierce protector goddess often depicted as a lioness or domestic cat."}
    ]
}

@app.route("/")

def home():
    return render_template('index.html')

@app.route('/browse', methods=['GET','POST'])
def browse():
    # Default: show everyone
    results = MYTH_DATA["gods"] 
    
    if request.method == 'POST':
        choice = request.form.get('pantheon')
        if choice:
            results = [g for g in MYTH_DATA["gods"] if g['pantheon'] == choice]
            
    return render_template('browse.html', gods=results)

@app.route('/hero/<hero_id>')
def profile(hero_id):
    # Find the one hero that matches the URL
    hero = next((g for g in MYTH_DATA["gods"] if g['id'] == hero_id), None)
    return render_template('profile.html', hero=hero)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
@app.route('/random')
def random_legend():
    chosen = random.choice(MYTH_DATA['gods'])
    return render_template('profile.html', hero=chosen)