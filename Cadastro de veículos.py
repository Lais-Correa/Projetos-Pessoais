#informações gerais
class Veiculo:
    def __init__(self, marca = str, modelo = str, ano = int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print(f'VEICULO - MARCA/MODELO: {self.marca} - {self.modelo}, ANO: {self.ano}.')

#informações para o carro
class Carro(Veiculo):
    def __init__(self, marca = str, modelo = str, ano = int, portas = int):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def apresentar(self):
        print(f'CARRO - MARCA/MODELO: {self.marca} - {self.modelo}, ANO: {self.ano} ({self.portas} portas).')

#informação para a moto
class Moto(Veiculo):
    def __init__(self, marca = str, modelo = str, ano = int, tipo = str):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def apresentar(self):
        print(f'MOTO - MARCA/MODELO: {self.marca} - {self.modelo}, ANO: {self.ano}, TIPO: ({self.tipo}).')

#coleta de dados
def main():
    print('='*50)
    print('Cadastrando novos veículos'.center(50))
    print('='*50)
    marca_carro = input('Digite a marca do carro: ')
    modelo_carro = input('Digite o modelo do carro: ')
    ano_carro = int(input('Digite o ano do carro: '))
    portas_carro = int(input('Digite o número de portas do carro: '))
    carro = Carro(marca_carro, modelo_carro, ano_carro, portas_carro)

    marca_moto = input('\nDigite o marca da moto: ')
    modelo_moto = input('Digite o modelo da moto: ')
    ano_moto = int(input('Digite o ano da moto: '))
    tipo_moto = input('Digite o tipo da moto (esportiva, scooter, trail, etc...): ')
    moto = Moto(marca_moto, modelo_moto, ano_moto, tipo_moto)

    #cadastro
    print('\n='*55)
    print('INICIANDO O SISTEMA...'.center(55))
    print('='*55)
    print('Informações cadastradas:')
    print('='*55)
    carro.apresentar()
    moto.apresentar()
    print('='*55)


if __name__ == '__main__':
    main()
