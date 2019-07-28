import os

def gravarPrato(nomePrato, precoPrato):
	if os.path.isfile('pratos.txt') == True:
		file = lerArquivo('pratos.txt', 'r+')
		codigo = int(file.readlines()[-1].split(';')[0])
		file.write('{};{};{}\n'.format(codigo+1, nomePrato, precoPrato))
		file.close()
	else:
		file = lerArquivo('pratos.txt', 'w')
		codigo = 1
		file.write('{};{};{}\n'.format(codigo, nomePrato, precoPrato))
		file.close()


def gravarBebida(nomeBebida, precoBebida):
	if os.path.isfile('bebidas.txt') == True:
		file = lerArquivo('bebidas.txt', 'r+')
		codigo = int(file.readlines()[-1].split(';')[0])
		file.write('{};{};{}\n'.format(codigo+1, nomeBebida, precoBebida))
		file.close()
	else:
		file = lerArquivo('bebidas.txt', 'w')
		codigo = 1
		file.write('{};{};{}\n'.format(codigo, nomeBebida, precoBebida))
		file.close()
			

def lerArquivo(nomeArquivo, mode):
	f = open(nomeArquivo, mode)
	return f


def gravarPedidos(listaPedido, now):
	if os.path.isfile('Pedidos.txt') == True:
		file = lerArquivo('Pedidos.txt', 'r+')
		codigo = int(file.readlines()[-1].split(';')[0])
		file.write('{};{};{}\n'.format(codigo+1, listaPedido, now))
		file.close()
	else:
		file = lerArquivo('Pedidos.txt', 'w')
		codigo = 1
		file.write('{};{};{}\n'.format(codigo, listaPedido, now))
		file.close()


def gravarPromocao(pratopromocao, precopromocao2):
	if os.path.isfile('Promocao.txt') == True:
		file = lerArquivo('Promocao.txt', 'r+')
		codigo = int(file.readlines()[-1].split(';')[0])
		file.write('{};{};{}\n'.format(codigo+1, pratopromocao, precopromocao2))
		file.close()
	else:
		file = lerArquivo('Promocao.txt', 'w')
		codigo = 1
		file.write('{};{};{}\n'.format(codigo, pratopromocao, precopromocao2))
		file.close()


def gravarReserva(reservaNome, reservaCpf, reservaData, reservaAssentos, gerarMesa):
	if os.path.isfile('Reserva.txt') == True:
		file = lerArquivo('Reserva.txt', 'r+')
		codigo = int(file.readlines()[-1].split(';')[0])
		file.write('{};Nome: {}; CPF: {}; Data: {}; Acentos: {}; Mesa: {}\n'.format(codigo+1, reservaNome, reservaCpf, reservaData, reservaAssentos, gerarMesa))
		file.close()
	else:
		file = lerArquivo('Reserva.txt', 'w')
		codigo = 1
		file.write('{};Nome: {}; CPF: {}; Data: {}; Acentos: {}; Mesa: {}\n'.format(codigo+1, reservaNome, reservaCpf, reservaData, reservaAssentos, gerarMesa))
		file.close()


def buscarPratoPorId(id):
	file = lerArquivo('pratos.txt', 'r+')
	for linha in file.readlines():
		linhaSlitted = linha.split(';')
		if int(linhaSlitted[0]) == id:
			linhaSlitted[-1] = linhaSlitted[-1].replace('\n', '')
			return linhaSlitted

def buscarPromocaoPorId(id):
	file = lerArquivo('Promocao.txt', 'r+')
	for linha in file.readlines():
		linhaSlitted = linha.split(';')
		if int(linhaSlitted[0]) == id:
			linhaSlitted[-1] = linhaSlitted[-1].replace('\n', '')
			return linhaSlitted

def buscarbebidasPorId(id):
	file = lerArquivo('bebidas.txt', 'r+')
	for linha in file.readlines():
		linhaSlitted = linha.split(';')
		if int(linhaSlitted[0]) == id:
			linhaSlitted[-1] = linhaSlitted[-1].replace('\n', '')
			return linhaSlitted
