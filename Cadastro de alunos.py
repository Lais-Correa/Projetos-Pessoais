from time import sleep

class Aluno:
    def __init__(self, nome='Desconhecido', idade=0, curso='Desconhecido', matricula='0'):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula


    def mostrar_alunos(self):
        print('\033[34m DADOS DO ALUNO \033[m'.center(53, '-'))
        print('\033[34m Nome: \033[m', self.nome)
        print('\033[34m Idade: \033[m', self.idade,'anos')
        print('\033[34m Curso: \033[m', self.curso)
        print('\033[34m Matricula: \033[m', self.matricula)
        print('\033[34m-\033[m'*45)

def main():
    alunos = []

    while True:
        print(' MENU '.center(45, '-'))
        print('1 - Cadastrar novo aluno(a)')
        print('2 - Exibir informações de alunos cadastrados')
        print('3 - Encerrar o programa')
        print('-'*45)

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            sleep(1)
            print('-' * 45)
            print('Cadastrando novo aluno...')
            nome = str(input('Nome: '))
            idade = (input('Idade: '))
            curso = str(input('Curso: '))
            matricula = str(input('Matricula: '))

            aluno = (Aluno(
                nome if nome.strip() else 'Desconhecido',
                int(idade) if idade.strip() else 0,
                curso if idade.strip() else 'Desconhecido',
                matricula if matricula.strip() else '0'))
            alunos.append(aluno)
            print('Aluno cadastrado com sucesso!')

        elif opcao == 2:
            sleep(1)
            if len(alunos) == 0:
                print('Nenhum aluno cadastrado.')
            else:
                for i, aluno in enumerate(alunos, start=1):
                    print(f'\nAluno {i}:')
                    aluno.mostrar_alunos()

        elif opcao == 3:
            sleep(0.5)
            print('\033[33mEncerrando o programa...\033[m')
            break

        else:
            print('Opção errada, selecione uma opção válida')


if __name__ == '__main__':
    main()
