from AutomatoFD import AutomatoFD

class MinimizaAFD():
    
    def __init__(self, afd: AutomatoFD):
         self.afd = afd
        
    def minimizaAFD(self):
        estadosEqui =  self.afd.estadosEquivalentes();
        for (x, y) in estadosEqui.keys():
            v = estadosEqui[(x, y)]
            """verifica estados que são equivalentes"""
            if(v):
                """transições que chegam no estado y são passadas para chegar no X"""
                for (e, a) in  self.afd.transicoes.keys():
                    d =  self.afd.transicoes[(e, a)]
                    if(d == y):
                         self.afd.transicoes[(e, a)] = x
                """Remove as transições a partir de Y"""
                for a in  self.afd.alfabeto:
                  del  self.afd.transicoes[(y,a)]
                """Remove estado """
                self.afd.estados.remove(y)
        return self.afd