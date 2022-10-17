from fila_factory import FilaFactory


teste_factory = FilaFactory.pegar_fila('normal')
teste_factory.atualizar_fila()
teste_factory.atualizar_fila()
teste_factory.atualizar_fila()
print(teste_factory.chamar_cliente(10))