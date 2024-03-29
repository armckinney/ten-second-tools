from abc import ABC

from cryptax.core.transactions import Transaction


class TransactionFactory(ABC):
    def get_transactions(self, transaction_report_file_path: str) -> Transaction:
        raise NotImplementedError
