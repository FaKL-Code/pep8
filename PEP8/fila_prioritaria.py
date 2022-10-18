from typing import List, Union
from fila_base import FilaBase
from const import CODIGO_PRIORITARIO

class FilaPrioritaria(FilaBase):
    def gerar_senha(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'
        
    def chamar_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'clliente atual: {cliente_atual} caixa: {caixa}')   
    
    def estatistica(self, dia: str, agencia: int, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(dia, agencia)
        return estatistica.roda_estatistica(self.clientes_atendidos)
    