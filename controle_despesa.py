class ControleDespesas:
    def __init__(self):
        self.despesas=[]

    def adicionardespesas(self, gastos):
        self.despesas.append(gastos)

    def totalporcategoria(self):
        categorias={}

        for despesa in self.despesas:
            categoria=despesa.categoria
            if categoria in categorias:
                categorias[categoria]+=despesa.valor
            else:
                categorias[categoria]=despesa.valor
        return categorias

    def totalgasto(self):
        total=0
        for despesa in self.despesas:
            total+=despesa.valor

        return total