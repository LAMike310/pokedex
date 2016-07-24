from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://localhost:5000/'


def name():
    id = input("Please enter a Pokemon ID: ")
    sel_url = server_url + 'name?id={0}'
    answer = requests.get(url=sel_url.format(id))
    print(answer.text)

if __name__ == '__main__':
    name()