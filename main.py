from flask import Flask, jsonify, make_response, request
from bd import Campos

app = Flask('campos')

#GET
@app.route('/campos', methods=['GET'])
def get_campos():
    return Campos

@app.route('/campos/<int:id>', methods=['GET'])
def get_campo(id):
    for campo in Campos:
        if campo.get('id') == id:
            return jsonify(campo)
        
        
#POST
@app.route('/campos', methods=['POST'])
def criar_campos():
    campo = request.json
    Campos.append(campo)
    return make_response(
        jsonify(mensagem='Campo cadastrado com sucesso!',
                campo=campo
                )
    )
    
#PUT
@app.route('/campos/<int:id>', methods=['PUT'])
def atualizar_campo_id(id):
    campo_atualizado = request.get_json()
    for indice, campo in enumerate(Campos):
        if campo.get('id') == id:
            Campos[indice].update(campo_atualizado)
            return jsonify(Campos[indice])
        
#DELETE
@app.route('/campos/<int:id>', methods=['DELETE'])
def excluir_campo(id):
    for indice, campo in enumerate(Campos):
        if campo.get('id') == id:
            del Campos[indice]
            return jsonify({"mensagem:": "Campos excluido com sucesso!"})


        
app.run(port=5000, host='localhost')