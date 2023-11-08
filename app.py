from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = []

@app.route("/", methods=["GET", "POST"])
def index():
  # TODO
  return
