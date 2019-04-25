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

@app.route('/getcategorias')
def api_get_categorias():
    categorias = []
    dbUtils = DbUtils()
    db_aux = dbUtils.get_categoria()
    for linha in db_aux:
        json_aux = {"id_categoria": linha[0], "tituloCategoria": linha[1], "descricaoCategoria":linha[2], "fg_ativo": linha[3]}
        categorias.append(json_aux)

    return jsonify(categorias)


if __name__ == '__main__':
	app.run()