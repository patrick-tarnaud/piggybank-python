from enum import Enum
from datetime import datetime


class Transaction:
    class TypeTransaction(Enum):
        DEBIT = 'debit'
        CREDIT = 'credit'

    def __init__(self, id_tx: str, date_tx: datetime, type_tx: TypeTransaction, amount: float, name: str, memo: str):
        """
        Constructor
        :param id_tx:
        :param date_tx:
        :param type_tx:
        :param amount:
        :param name:
        :param memo:
        """
        self.id = id_tx
        self.type = type_tx
        self.date = date_tx
        self.amount = amount
        self.name = name
        self.memo = memo

    def __str__(self):
        return f'id: {self.id}, type: {self.type}, date: {self.date}, amount: {self.amount}, name: {self.name}, memo: {self.memo}'

    def __repr__(self):
        return self.__str__()
