from fila_base import FilaBase

class FilaNormal(FilaBase):
    def gerar_senha(self) -> None:
        self.senha_atual = f'NM{self.codigo}'
        
    def chamar_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'clliente atual: {cliente_atual} caixa: {caixa}')
    