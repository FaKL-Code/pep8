import abc


class FilaBase:
    codigo: int = 0
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senha_atual: str = ""
    
    def resetar_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
    
    @abc.abstractmethod
    def gerar_senha(self) -> None:
        ...
    
    @abc.abstractmethod
    def atualizar_fila(self) -> None:
        ...
        
    @abc.abstractmethod
    def chamar_cliente(self, caixa:int) -> str:
        ...
        