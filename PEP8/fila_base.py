import abc

from PEP8.const import TAMANHO_PADRAO_MAX, TAMANHO_PADRAO_MIN


class FilaBase:
    codigo: int = TAMANHO_PADRAO_MIN
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senha_atual: str = ""
    
    def atualizar_fila(self) -> None:
        self.resetar_fila()
        self.gerar_senha()
        self.inserir_cliente()
    
    def resetar_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAX:
            self.codigo = 0
        else:
            self.codigo += 1
    
    def inserir_cliente(self):
        self.fila.append(self.senha_atual)
    
    @abc.abstractmethod
    def gerar_senha(self) -> None:
        ...
        
    @abc.abstractmethod
    def chamar_cliente(self, caixa:int) -> str:
        ...
        