from typing import Union
from const import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


class FilaFactory:
    @staticmethod
    def pegar_fila(tipo_fila: str) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria
        else:
            raise NotImplementedError('Tipo de fila nao existe')