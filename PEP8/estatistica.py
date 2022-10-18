from typing import List


class Estatistica:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia
        
    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: dict = {f'{self.agencia} - {self.dia}': len(clientes_atendidos)}
        return estatistica