import pandas
from transaction import Transaction
from decimal import Decimal


def main():
    excel = pandas.read_excel("C:\\Users\\przem\\Desktop\\krypto.xlsx")
    token_list = []
    existing_tokens = {}

    # Init token_list with existing tokens in the krypto.xlsx
    for row in excel.itertuples():
        existing_token = found_token(token_list, row.Token)

        if len(token_list) == 0 or existing_token is None:
            token = Transaction(row.Token, row.Ilosc, row.Wartosc, row.Oplata, row.Dodatkowa_oplata)
            token.count_return_price()
            token_list.append(token)
        else:
            existing_token.amount += row.Ilosc
            existing_token.cost += row.Wartosc + row.Oplata + row.Dodatkowa_oplata
            existing_token.count_return_price()

    for token in token_list:
        print(f"NAZWA: {token.token}, CENA ZWROTNA: {Decimal(token.return_price).quantize(Decimal('0.00000000000'))}")




def found_token(token_list, token_name):
    for token in token_list:
        if token.token == token_name:
            return token

    return None


if __name__ == "__main__":
    main()
