# O objetivo desta atividade é criar um programa simples em Python para gerenciar um cadastro de compras e vendas de produtos.
# Crie um menu interativo que permita ao usuário escolher entre as seguintes opções:
# Registrar uma compra.
# Registrar uma venda.
# Verificar o saldo total das vendas.
# Sair do programa.

# Crie duas listas, uma para armazenar as compras e outra para armazenar as vendas. Cada registro nas listas deve conter informações como o nome do produto, a quantidade e o valor unitário.
# Ao registrar uma compra, solicite ao usuário que insira o nome do produto, a quantidade e o valor unitário. Adicione essas informações à lista de compras.
# Ao registrar uma venda, solicite ao usuário que insira o nome do produto, a quantidade e o valor unitário. Adicione essas informações à lista de vendas.
# Ao verificar o saldo total das vendas, calcule o lucro total subtraindo o valor total das compras do valor total das vendas. Exiba o lucro na tela.
# Certifique-se de que o programa possa lidar com erros, como entradas inválidas ou divisão por zero. Também atente-se a indentação ao enviar o código pelo sistema.
from typing import TypedDict
import time


class Product(TypedDict):
    name: str
    amount: int
    unit_value: float


purchases: list[Product] = []
sales: list[Product] = []


def handle_add_sale():
    product = get_product()

    if product is not None:
        sales.append(product)


def handle_add_purchase():
    product = get_product()

    if product is not None:
        purchases.append(product)


def get_product() -> Product | None:
    while True:
        try:
            print('')
            print(' Formulário de produto '.center(48, '='))
            print('* Nome do produto')
            name = input('Digite: ')

            print('')
            print('* Quantidade desse produto')
            print('- Regra: O valor deve ser número inteiro.')
            print('Exemplo: "199", "10", "24"')
            amount = int(input('Digite: '))

            print('')
            print('* Valor unitário do produto')
            print('- Regra: O valor deve ser um número inteiro ou decimal.')
            print('Exemplo: "1000", "10.00", "59.00"')
            unit_value = float(input('Digite: '))

            return {
                'name': name,
                'amount': amount,
                'unit_value': unit_value
            }
        except ValueError:
            print('')
            print(' Erro '.center(48, '='))
            print('Parece que você digitou algum tipo de informação errada')
            print('')
            should_try_again = input('Gostaria de tentar novamente? [s/n] ')

            match should_try_again:
                case 's':
                    continue
                case 'n' | _:
                    break


def check_total_sales():
    total_sales = calculate_total_products(sales)
    total_purchases = calculate_total_products(purchases)

    print('')
    print(' Saldo total das vendas '.center(48, '='))
    print('- Produtos comprados')
    print('Quantidade:', len(purchases))
    print('Receita:', total_purchases)
    print('')
    print('- Produtos vendidos')
    print('Quantidade:', len(sales))
    print('Receita:', total_sales)
    print('')
    print(f'Lucro: {total_sales - total_purchases:.2f}')

    time.sleep(2)


def calculate_total_products(products: list[Product]):
    total_products: float = 0

    for product in products:
        total_products += product['amount'] * product['unit_value']

    return total_products


def parse_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def main():
    while True:
        print('')
        print(' Menu '.center(48, '='))
        print('1. Registrar uma compra.')
        print('2. Registrar uma venda.')
        print('3. Verificar o saldo total das vendas.')
        print('4. Sair do programa.')
        print('')

        option = parse_int((input('Digite uma opção: ')))

        match option:
            case 1:
                handle_add_purchase()
            case 2:
                handle_add_sale()
            case 3:
                check_total_sales()
            case 4:
                break
            case None:
                print('A opção não é um número!')
                time.sleep(2)
            case _:
                print('Opção inválida!')
                time.sleep(2)


if __name__ == '__main__':
    main()
