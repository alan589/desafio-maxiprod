class Transacao:
    def __init__(self, transacao_id, descricao, valor, tipo, pessoa_id):
        self.transacao_id = transacao_id
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.pessoa_id = pessoa_id

