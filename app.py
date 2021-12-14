import re
from flask import Flask, request, render_template
import stories

app = Flask(__name__)


@app.route("/")
def get_madlib():
    return render_template("data_form.html")


@app.route("/story")
def get_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    words = {"place": place,
             "noun": noun,
             "verb": verb,
             "adjective": adjective,
             "plural_nuon": plural_noun
             }

    story = stories.Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    madlib = story.generate(words)
