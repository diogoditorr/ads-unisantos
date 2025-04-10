def main():
    print('oi')

    lista = [1, -3, 4, -6]
    new_lista = map(invert_int_signal, lista)

    print(list(new_lista))

    exemplo2()

def exemplo2():
    numeros = [1, 2, 3, 4, 5]
    indices = (2,2,2,2,2)

    resultado = map(pow, numeros, indices)
    print(list(resultado))


def invert_int_signal(value: int):
    return value * -1

if __name__ == "__main__":
    main()