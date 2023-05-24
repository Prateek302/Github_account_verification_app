from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        repositories = get_github_repositories(username)
        return render_template('result.html', username=username, repositories=repositories)
    return render_template('index.html')

def get_github_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        return None

if __name__ == '__main__':
    app.run()
