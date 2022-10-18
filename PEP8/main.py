from fila_factory import FilaFactory
from estatistica_detalhada import EstatisticaDetalhada
from estatistica import Estatistica


teste_factory = FilaFactory.pegar_fila('prioridade')
print(teste_factory.chamar_cliente(10))