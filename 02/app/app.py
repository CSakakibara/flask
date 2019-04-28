#Lucas Guerra Borges
#Christopher Jun Maruyama Sakakibara

from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from bottle import response
from dbUtils import DbUtils

app = Flask(__name__)

@app.route('/createtablecategoria')
def api_create_table_categoria():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_categorias()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/createtablevendedores')
def api_create_table_vendedores():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_vendedores()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/createtablefornecedores')
def api_create_table_fornecedores():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_fornecedores()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/createtableprodutos')
def api_create_table_produtos():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_produtos()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/createtablevendas')
def api_create_table_vendas():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_vendas()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/createtablecompras')
def api_create_table_compras():
	dbUtils = DbUtils()
	if (dbUtils.create_tb_compras()):
		result = {"result": "Tabela criada!"}
	else:
		result = {"result": "Problemas para criar Tabela!"}
	return jsonify(result)

@app.route('/addcategoria', methods=['POST'])
def api_add_categoria():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_categoria = req_data['id_categoria']
	tituloCategoria = req_data['tituloCategoria']
	descricaoCategoria = req_data['descricaoCategoria']
	fg_ativo = req_data['fg_ativo']
	dbUtils = DbUtils()

	if(dbUtils.add_categoria(id_categoria, tituloCategoria, descricaoCategoria, fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/addvendedor', methods=['POST'])
def api_add_vendedor():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_vendedor = req_data['id_vendedor']
	cpf = req_data['cpf']
	nome = req_data['nome']
	carteiraTrabalho = req_data['trabalho']
	telefone = req_data['telefone']
	dataAdmissao = req_data['dataAdmissao']
	fg_ativo = req_data['fg_ativo']

	dbUtils = DbUtils()

	if(dbUtils.add_vendedor(id_vendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao ,fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/addfornecedor', methods=['POST'])
def api_add_fornecedor():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_fornecedor = req_data['id_fornecedor']
	cnpj = req_data['cnpj']
	razaoSocial = req_data['razaoSocial']
	telefone = req_data['telefone']
	endereco = req_data['endereco']
	contato = req_data['contato']
	fg_ativo = req_data['fg_ativo']

	dbUtils = DbUtils()

	if(dbUtils.add_fornecedor(id_fornecedor, cnpj, razaoSocial, telefone, endereco, contato ,fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/addproduto', methods=['POST'])
def api_add_produto():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_produto = req_data['id_produto']
	id_fornecedor = req_data['id_fornecedor']
	id_categoria = req_data['id_categoria']
	nomeProduto = req_data['nomeProduto']
	descricaoProduto = req_data['descricaoProduto']
	valorUnitario = req_data['valorUnitario']
	quantidade = req_data['quantidade']
	quantidadeMinima = req_data['quantidadeMinima']
	fg_ativo = req_data['fg_ativo']

	dbUtils = DbUtils()

	if(dbUtils.add_produto(id_produto, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/addvenda', methods=['POST'])
def api_add_venda():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_venda = req_data['id_venda']
	id_vendedor = req_data['id_vendedor']
	id_categoria = req_data['id_categoria']
	id_produto = req_data['id_produto']
	dataVenda = req_data['dataVenda']
	valorTotal = req_data['valorTotal']
	quantidade = req_data['quantidade']
	fg_ativo = req_data['fg_ativo']

	dbUtils = DbUtils()

	if(dbUtils.add_venda(id_venda, id_vendedor, id_categoria, id_produto, dataVenda, valorTotal, quantidade, fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/addcompra', methods=['POST'])
def api_add_compra():
	if not request.json:
		abort(400)

	req_data = request.get_json()

	id_compra = req_data['id_compra']
	id_fornecedor = req_data['id_fornecedor']
	id_produto = req_data['id_produto']
	id_categoria = req_data['id_categoria']
	dataCompra = req_data['dataCompra']
	valorTotal = req_data['valorTotal']
	quantidade = req_data['quantidade']
	fg_ativo = req_data['fg_ativo']

	dbUtils = DbUtils()

	if(dbUtils.add_compra(id_compra, id_fornecedor, id_produto, id_categoria, dataCompra, valorTotal, quantidade, fg_ativo)):
		result = {"result": "Inserido com sucesso!"}
	else:
		result = {"result": "Não foi possivel inserir"}
	return jsonify(result)

@app.route('/getcategorias')
def api_get_categorias():
    categorias = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_categoria": linha[0], "tituloCategoria": linha[1], "descricaoCategoria":linha[2], "fg_ativo": linha[3]}
        categorias.append(json_aux)

    return jsonify(categorias)

@app.route('/getvendedores')
def api_get_vendedores():
    vendedores = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_vendedor": linha[0], "cpf": linha[1], "nome":linha[2], "carteiraTrabalho": linha[3], "telefone": linha[4], "dataAdmissao": linha[5], "fg_ativo": linha[6]}
        vendedores.append(json_aux)

    return jsonify(vendedores)

@app.route('/getfornecedores')
def api_get_fornecedores():
    fornecedores = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_fornecedores": linha[0], "cnpj": linha[1], "razaoSocial":linha[2], "telefone": linha[3], "endereco": linha[4], "contato": linha[5], "fg_ativo": linha[6]}
        fornecedores.append(json_aux)

    return jsonify(fornecedores)

@app.route('/getprodutos')
def api_get_produtos():
    produtos = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_produto": linha[0], "id_fornecedor": linha[1], "id_categoria":linha[2], "nomeProduto": linha[3], "descricaoProduto": linha[4], "valorUnitario": linha[5], "quantidade": linha[6], "quantidadeMinima":linha[7] ,"fg_ativo": linha[8]}
        produtos.append(json_aux)

    return jsonify(produtos)

@app.route('/getvendas')
def api_get_vendas():
    vendas = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_venda": linha[0], "id_vendedor": linha[1], "id_categoria":linha[2], "id_produto": linha[3], "dataVenda": linha[4], "valorTotal": linha[5], "quantidade": linha[6],"fg_ativo": linha[7]}
        vendas.append(json_aux)

    return jsonify(vendas)

@app.route('/getcompras')
def api_get_compras():
    compras = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categorias()
    for linha in db_aux:
        json_aux = {"id_compra": linha[0], "id_fornecedor": linha[1], "id_produto":linha[2], "id_categoria": linha[3], "dataCompra": linha[4], "valorTotal": linha[5], "quantidade": linha[6],"fg_ativo": linha[7]}
        compras.append(json_aux)

    return jsonify(compras)

if __name__ == '__main__':
	app.run()
