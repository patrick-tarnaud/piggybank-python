import ofxtools
from models.transaction import Transaction
from datetime import datetime
from models.account import Account


def import_from_ofx_file(filename: str) -> Account:
    parser = ofxtools.Parser.OFXTree()
    parser.parse(filename)
    ofx = parser.convert()

    # account loading
    bankacctfrom = ofx.bankmsgsrsv1.statements[0].bankacctfrom
    account = Account(bankacctfrom.bankid, bankacctfrom.branchid, bankacctfrom.acctid)

    # transactions loading
    transactions = ofx.bankmsgsrsv1.statements[0].transactions
    transaction_list = []
    for tx in transactions:
        transaction_list.append(Transaction(tx.fitid, tx.dtposted,
                                            Transaction.TypeTransaction.CREDIT if tx.trntype == 'CREDIT' else Transaction.TypeTransaction.DEBIT,
                                            tx.trnamt, tx.name, tx.memo))
    account.transactions = transaction_list

    return account
