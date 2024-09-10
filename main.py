# um programa vai ter várias classes, 20, 50, até 200 em arquivos separados.
# Herança: é quando vc tem duas classes complemente diferentes, mas possui atributos e métodos em comum herdados da Super Classe.
# superclasse (classe-pai)
class Pessoa: 
    # definindo atributos
    cidade = "Brasília"
    telefone = "(61) 98765-4321"
    email = "nome@gmail.com"

# subclasse (classe-filha)
class PessoaFisica(Pessoa):
    # atributos
    nome = "Fulano de Tal"
    cpf = "123.456.789-12"
    peso = 90
    altura = 1.80

class PessoaJuridica(Pessoa):
    # atributos
    nome_fantasia = "Cobra Kai LTDA"
    razao_social = "Fulano de Tal S.A."
    cnpj = '62.245.916/0001-69'

# programa principal
if __name__ == "__main__":
    # instamcia dos objetos
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

    print(f'{"-"*30} DADOS DO USUÁRIO {"-"*30}\n')
    print(f'Nome do usuário: {usuario.nome}.')
    print(f'CPF do usuário: {usuario.cpf}.')
    print(f'Peso do usuário: {usuario.peso}.')
    print(f'Altura do usuário: {usuario.altura}.')
    print(f'Cidade do usuário: {usuario.cidade}.')
    print(f'Telefone do usuário: {usuario.telefone}.')
    print(f'Email do usuário: {usuario.email}.')    

    print(f'{"-"*30} DADOS DA EMPRESA {"-"*30}\n')
    print(f'Nome da empresa: {empresa.nome_fantasia}.')
    print(f'Razão Social da empresa: {empresa.razao_social}.')
    print(f'CNPJ da empresa: {empresa.cnpj}.')
    print(f'Cidade sede da empresa: {empresa.cidade}.')
    print(f'Telefone do usuário: {empresa.telefone}.')
    print(f'Email da empresa: {empresa.email}.')