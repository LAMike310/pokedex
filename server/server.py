import requests
import json
from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint that pays user if answer is correct
@app.route('/name')
@payment.required(1)
def answer_question():

    # extract answer from client request
    id = request.args.get('id')
    url = 'http://pokeapi.co/api/v2/pokemon/' + id

    response = requests.get(url)
    pokemonData = json.loads(response.text)
    pokemonName = pokemonData['name']
    print(pokemonName)
    return pokemonName

if __name__ == '__main__':
    app.run(host='0.0.0.0')

