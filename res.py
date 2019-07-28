from random import randrange
import manipulacaoArquivos
from datetime import datetime
from random import randint

soma = 0.0
pagamento = 0.0
precoPrato = 0.0
precoBebida = 0.0
precopromocao2 = 0.0
pedidoBebida = 0
pedidoPrato = 0

listaPedido = []


print ('Olá aqui iremos criar um restaurante para você :) ')
donoRestaurante = input ('Para começar, digite qual é o seu nome: ')
restaurante = str (input ('Agora digite como vai se chamar o seu restaurante: '))
print ('Seja bem vindo(a) {}, ao seu novo restaurante: {}'.format(donoRestaurante, restaurante))


condicao = 0
while condicao !=9:
    print ('Que ação deseja realizar? ')
    print ('1 - Cadastrar novos pratos')
    print ('2 - Cadastrar bebidas')
    print ('3 - Cadastro de promoção (para pratos) ')
    print ('4 - Realizar pedido ')
    print ('5 - Fechar pedido ')
    print ('6 - Realizar pagamento (credito, debito ou dinheiro)')
    print ('7 - Reservar mesas')
    print ('8 - Consulte o seu lucro total')
    print ('9 - Sair')
    opcao = int (input())

    if opcao == 1: 
        nomePrato = str (input ('Digite o nome do prato que deseja cadastrar: '))
        precoPrato = float(input('Digite o preço do prato: '))
        manipulacaoArquivos.gravarPrato(nomePrato, precoPrato)
        print ('Parabéns!!')
        print ('Você cadastrou o prato {}'.format(nomePrato))
    if opcao == 2:
        nomeBebida = str (input ('Digite o nome da bebida que deseja cadastrar: '))
        precoBebida = float(input('Digite o preço da bebida: '))
        manipulacaoArquivos.gravarBebida(nomeBebida, precoBebida)
        print ('Parabéns!!')
        print ('Você cadastrou a bebida {}'.format(nomeBebida))
    if opcao == 3:
        print ('Cadastre uma promoção aqui!')
        pratopromocao = str (input ('Digite o nome do novo prato para promoção: '))
        precopromocao1 = float (input ('Digite o quanto estava custando o prato {}: '.format(pratopromocao)))
        precopromocao2 = float (input ('Digite o novo valor do prato {}, para promoção: '.format(pratopromocao)))
        manipulacaoArquivos.gravarPromocao(pratopromocao, precopromocao2)
        print ('Promoção cadastrada com sucesso!')
        print ('Nova promoção do dia: {}'.format(pratopromocao))
        print ('Que estava custando antes: R${}'.format(precopromocao1))
        print ('Por apenas agora: R${}'.format(precopromocao2))
    if opcao == 4:
        print ('O que deseja pedir? ')
        promocao = str (input ('Deseja ver o cardapio promocional? [S/N] ')).upper()
        if promocao == 'S':
            arquivo = manipulacaoArquivos.lerArquivo('Promocao.txt', 'r')
            for linha in arquivo:
                codigo = linha.split(';')[0]
                pratopromocao = linha.split(';')[1]
                precopromocao2 = float(linha.split(';')[2]) 
                print(codigo)
                print(pratopromocao)
                print(precopromocao2) 
            pedidoPromocao = int (input ('Digite uma das opções anteriores: ')) 
            PromocaoSplitted = manipulacaoArquivos.buscarPromocaoPorId(pedidoPromocao)
            listaPedido.append(PromocaoSplitted)
        elif promocao == 'N': 
            arquivo = manipulacaoArquivos.lerArquivo('pratos.txt', 'r')
            for linha in arquivo: 
                codigo = linha.split(';')[0] 
                nomePrato = linha.split(';')[1] 
                precoPrato = float(linha.split(';')[2]) 
                print(codigo) 
                print(nomePrato) 
                print(precoPrato) 
            pedidoPrato = int (input ('Digite uma das opções anteriores: '))
            pratoSplitted = manipulacaoArquivos.buscarPratoPorId(pedidoPrato)
            listaPedido.append(pratoSplitted)
        print ('Deseja alguma bebida? (Se não deseja digite 0)')
        arquivo = manipulacaoArquivos.lerArquivo('bebidas.txt', 'r')
        for linha in arquivo:
            codigo = linha.split(';')[0]
            nomeBebida = linha.split(';')[1]
            precoBebida = float(linha.split(';')[2])
            print(codigo)
            print(nomeBebida)
            print(precoBebida)
        pedidoBebida = int (input ('Digite uma das opções anteriores: '))
        bebidasSplitted = manipulacaoArquivos.buscarbebidasPorId(pedidoBebida)
        listaPedido.append(bebidasSplitted)
        print ('Pedido efetuado com sucesso!') 
    if opcao == 5:
        print ('Para finalizar o pedido, Digite:')
        nomeCliente = str (input ('Qual é o nome do cliente: '))
        cpfCliente = str (input ('Qual é o CPF do cliente: '))
        print ('Pedido finalizado com sucesso!') 
        print('Lista de pedido')
        print(listaPedido)
        now = datetime.now()
        print (now)
        arquivo = manipulacaoArquivos.gravarPedidos(listaPedido, now)
    if opcao == 6:
        opcoesPagamento = str (input ('Digite em que forma de pagamento deseja pagar (credito, debito ou dinheiro): ')) 
        for linha in listaPedido: 
            soma = soma + float(linha[2])
        print ('O total a ser pago é: R$ {}'.format(soma))
    if opcao == 7: 
        print('Aqui vamos reservar uma mesa antecipadamente para você!') 
        print('Para isso digite algumas informações') 
        reservaNome = str (input('Digite seu nome completo: '))  
        reservaCpf = int (input('Digite seu CPF: '))
        reservaData = str (input('Digite em que data deseja reserva a sua mesa: '))
        reservaAssentos = int (input('Digite quantos assentos deseja ter em sua mesa: ')) 
        print ('Parabéns! A sua mesa foi reservada com Sucesso!')
        gerarMesa = (randint(1,50))
        print ('O número da sua mesa é: {}'.format(gerarMesa))
        print ('Procure a nossa recepção e informe seus dados para ter direito a sua reserva')
        now = datetime.now()
        print (now)
        manipulacaoArquivos.gravarReserva(reservaNome, reservaCpf, reservaData, reservaAssentos, gerarMesa) 
    if opcao == 8:
        print ('Veja aqui o quanto você tem ganho!')
        print ('No seu orçamento a cada pedido feito!')
        arquivo = manipulacaoArquivos.lerArquivo('Pedidos.txt', 'r')
        soma = 0.0
        for linha in arquivo:
            linha = linha.split (';')
            produtos = eval(linha[1])
            print (produtos)
            for p in produtos:    
                if p: 
                    soma += float(p[2])
        print ('O seu orçamento é de: {}'.format(soma))
    if opcao == 9:
        print ('Muito obrigado pelo acesso, volte sempre!')
        break
