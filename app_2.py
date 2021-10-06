from flask import Flask, render_template, request

from api.main import recommender

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        artist = request.args['artist'] 
        res = recommender(artist)
        res = ', '.join(res.split())
        return render_template('result.html', result=res), 200

    if request.method == 'POST':
        artist = request.form['artist']
        res = recommender(artist)
        res = ', '.join(res.split('\n'))
        return render_template('result.html', result=res), 200
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)