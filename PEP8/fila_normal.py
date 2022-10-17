class FilaNormal:
    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ""
    
    def gerar_senha(self) -> None:
        self.senha_atual = f'NM{self.codigo}'
        
    def resetar_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
            
    def atualizar_fila(self) -> None:
        self.resetar_fila()
        self.gerar_senha()
        self.fila.append(self.senha_atual)
        
    def chamar_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'clliente atual: {cliente_atual} caixa: {caixa}')