# ToDo App Exercise - Flask
Welcome to the ToDo App Exercise with Flask! In this assignment, you'll be creating a basic ToDo application using Flask, a micro web framework written in Python. The goal is to understand how to handle web requests and dynamically update web pages using server-side logic with Flask.

This exercise is designed to be run entirely within a development container, which means you don't need to install Python, Flask, or any other dependencies on your local machine—everything will be ready for you to use in the provided development environment.

Once you have completed your version of the ToDo app, you can compare it with our sample solution which is available in the answer folder.

## Objective:
Build a Flask-based web application that allows users to:

1. Enter a task using a form.
2. View the tasks they've added to a global list that gets updated with each new entry.

## Specific Tasks:
Your tasks for this exercise are outlined as follows:

### Set Up the HTML Form:
1. Design a form in index.html that includes:
- An `<input>` field for users to type their tasks.
- A `<button>` to submit the task to the list.

2. Create Unordered List in HTML:
- Add an `<ul>` element where the tasks will appear as `<li>` elements.

3. In app.py, set up Flask routes to handle:
- Displaying the current list of tasks.
- Adding a new task to the list when the form is submitted.

## How to Run Your Application:
Start the Flask Server: `python -m flask run`
Access the application by navigating to localhost:5000 in your web browser.

## How to Run Tests:
1. Ensure your Flask server is not running, or it will occupy the terminal.
2. In the root directory of the exercise, run `python test_app.py` in your terminal.

### Viewing Test Results:
The test script will provide output directly in the terminal.
If the tests pass, you'll see a success message for each test case.
If a test fails, you'll get feedback on what might be wrong.
Remember, the tests are there to guide your development process. Don't hesitate to run them frequently to ensure each part of your application is functioning as it should.
