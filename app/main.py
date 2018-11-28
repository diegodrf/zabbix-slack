from flask import Flask, request, jsonify
from Slack import Slack

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():

    url = request.form['2']
    data = request.form['3']

    slack = Slack(url)

    # O slack responde como texto puro, portanto para padronizar a visualização, a resposta é convertida para json.
    msg = slack.post(data)

    return jsonify({'status': msg})

if __name__ == '__main__':
    app.run(debug=True)
