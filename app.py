from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mystoryapp'

@app.route("/home")
def ask_question():
    """
    This will display a form to ask for different words in a input field
    """
    prompts = story.prompts
    return render_template('questions.html', prompts = prompts)

@app.route("/story")
def show_story():
    """
    this is will show the story
    """
    # html = """
    # <h1>WASSUP</h1>
    # """
    # return html
    text= story.generate(request.args)
    return render_template("story.html", text = text)
