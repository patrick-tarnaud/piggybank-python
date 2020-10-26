class Account:
    def __init__(self, bank_id: str, branch_id: str, account_id: str):
        self.bank_id = bank_id
        self.branch_id = branch_id
        self.account_id = account_id
        self.transactions = []

    def __str__(self):
        return f'bank_id: {self.bank_id}, branch_id; {self.branch_id}, account_id: {self.account_id}'

    def __repr__(self):
        return self.__repr__()
