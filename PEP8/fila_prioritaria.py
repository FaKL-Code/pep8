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
    
    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quantidade de clientes atendidos'] = len(self.clientes_atendidos)
        return estatistica
    