import random
import math as m

from RNA import RNA as rna


class MLP(rna):

    def __init__(self, qtd_input, qtd_hidden, qtd_output, ni = None):
        
        self.qtd_hidden = qtd_hidden
        self.qtd_output = qtd_output
        self.qtd_input = qtd_input

        if ni is None:
            self.ni = 0.001
        else:
            self.ni = ni
        
        self.wh = []
        self.wo = []

        self.inicializar_pesos()

    def inicializar_pesos(self):

        for i in range(self.qtd_hidden):
            
            aux = []
            for h in range(self.qtd_input+1):
                aux.append(0.6 * random.random() - 0.3)
            
            self.wh.append(aux)

        for h in range(self.qtd_output):
            
            aux = []
            for o in range(self.qtd_hidden+1):
                aux.append(0.6 * random.random() - 0.3)
                
            self.wo.append(aux)

    def calcular(self, x, y):

        H = []
        for w in self.wh:
            aux_0 = 0
            for i in range(len(x)):
                aux_0 += x[i]*w[i]
        
            o = 1/(1+m.exp(-1*aux_0))
        
            H.append(o)
            
        H.append(1)

        # Cálculo de valores de saída finais
        out = []
        for w in self.wo:
            aux = 0
            for i in range(len(H)):
                aux += H[i]*w[i]
            
            o = 1/(1+m.exp(-1*aux))

            out.append(o)
        
        return out, H

    def recalcular_deltas(self, x, out, y, H):

        # -------------------------------------------------
        #  Delta Saída e Back Propagation
        # -------------------------------------------------
        DO = []
        for oy in zip(out, y):
            if (oy[1] - oy[0]) >= 0:
                DO.append(oy[0] * (1 - oy[0]) * (m.pow((oy[1] - oy[0]), 2)))
            else:
                DO.append(oy[0] * (1 - oy[0]) * ((m.pow((oy[1] - oy[0]), 2))*(-1)))

        # -------------------------------------------------
        #  Delta intermediário e Back Propagation
        # -------------------------------------------------
        aux = [0 for i in range(self.qtd_hidden)]
        for i in range(len(DO)):
            for w in range(len(self.wo[0])-1):
                aux[w] += DO[i]*self.wo[i][w]

        DH = []
        for haux in zip(H,aux):
            DH.append(haux[0]*(1-haux[0])*haux[1])

        # -------------------------------------------------
        #  Ajuste dos pesos mediante os deltas calculados
        # -------------------------------------------------
        for w in range(len(self.wh)):
            for i in range(len(x)):
                self.wh[w][i] += self.ni*DH[w]*x[i]                     

        for w in range(len(self.wo)):
            for h in range(len(H)):
                self.wo[w][h] += self.ni*DO[w]*H[h]                   

    def treinar(self, x_input, y):
        x = x_input.copy()
        x.append(1)
        
        out, H = self.calcular(x=x, y=y)
        self.recalcular_deltas(x=x, out=out, y=y, H=H)

        return out

    def testar(self, x_input, y):
        out, H = self.calcular(x=x_input, y=y)

        return out

'''
# Teste 01:
x = [21.71, 17.25, 140.9, 1546.0, 0.09384, 0.08562, 0.1168, 0.08465, 0.1717, 0.05054, 1.207, 1.051, 7.733, 224.1, 0.005568, 0.01112, 0.02096, 0.01197, 0.01263, 
     0.001803, 30.75, 26.44, 199.5, 3143.0, 0.1363, 0.1628, 0.2861, 0.182, 0.251, 0.06494, 1]
y = [0.05, 0.95]

rna = MLP(qtd_input=30, qtd_hidden = 10, qtd_output=2)
rna.testar(x,y)
'''