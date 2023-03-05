from typing import Union
from pandas import DataFrame


def verify_file_format() -> str:
    pass


def extract_bank_name(data: Union[str, bytes]) -> str:
    pass


def extract_customer_name(data: Union[str, bytes]) -> str:
    pass


def extract_transaction_list(data: Union[str, bytes]) -> list[list]:
    pass


def transactions_to_df(transactions: list[list]) -> DataFrame:
    pass


# Might not be needed
def reverse_df_order(data: Union[str, bytes]) -> DataFrame:
    pass
