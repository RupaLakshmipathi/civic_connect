from flask import Flask, render_template, request, redirect, url_for
import pickle
from database import init_db, insert_issue, get_all_issues
from model import predict_issue

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        description = request.form['description']
        category, priority = predict_issue(description)
        insert_issue(description, category, priority)
        return redirect(url_for('dashboard'))
    return render_template('report.html')

@app.route('/dashboard')
def dashboard():
    issues = get_all_issues()
    return render_template('dashboard.html', issues=issues)

if __name__ == '__main__':
    app.run(debug=True)
