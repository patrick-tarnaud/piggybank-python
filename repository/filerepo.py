from model.account import Account
import pickle


def save(accounts: [Account]):
    with open('accounts.sav', 'bw') as file:
        pickler = pickle.Pickler(file)
        pickler.dump(accounts)


def load(filename: str) -> [Account]:
    with open('accounts.sav', 'br') as file:
        unpickler = pickle.Unpickler(file)
        return unpickler.load()
