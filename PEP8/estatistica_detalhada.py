from typing import List, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia
        
    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: dict[str, Union[List[str], str, int]] = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes atendidos'] = clientes_atendidos
        estatistica['quantidade de clientes atendidos'] = len(clientes_atendidos)
        return estatistica