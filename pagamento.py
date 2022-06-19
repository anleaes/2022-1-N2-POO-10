class Pagamento:

  def __init__(self, quantidade_total, valor_total, metodo_pagamento, tratamento):
    self.quantidade_total = quantidade_total
    self.valor_total = valor_total
    self.metodo_pagamento = metodo_pagamento
    self.tratamento = tratamento

  def finaliza_pagamento(self):
    return 'Pagamento realizado!'

  def valida_promocao(self):
    return 'Desconto aplicado!'