import random
import math as m

from RNA import RNA as rna

class MLP(rna):

    def __init__(self, qtd_input, qtd_hidden, qtd_output, ni = None):
        
        self.qtd_hidden = qtd_hidden
        self.qtd_output = qtd_output
        self.qtd_input  = qtd_input

        if ni == None:
            self.ni = 0.001;
        else:
            self.ni = ni
        
        self.wh = []
        self.wo = []

        self.inicializar_pesos()

    def inicializar_pesos(self):

        for i in range(self.qtd_hidden):                                # Colunas se referindo aos neurônios
            
            aux = []
            for h in range(self.qtd_input+1):                           # Linhas se referindo às entradas
                aux.append(0.6 * random.random() - 0.3)
            
            self.wh.append(aux)

        for h in range(self.qtd_output):                                # Colunas se referindo aos neurônios
            
            aux = []
            for o in range(self.qtd_hidden+1):                          # Linhas se referindo às entradas
                aux.append(0.6 * random.random() - 0.3)
                
            self.wo.append(aux)


    def calcular(self, x, y):

        # Cálculo de valores de saída intermediários
        H            = []
        for w in self.wh:                                               # Para cada vetor de pesos relacionado a 1 neuronio
            aux = 0
            for i in range(len(x)): 
                aux += x[i]*w[i]                                        # Multiplique o elemento por seu peso correspondente
            
            o = 1/(1+m.exp(-1*aux))                                     # Aplique a função de aplicação a um dado neurônio 

            H.append(o)
            
        H.append(1)                                                     # Bias da Camada intermediária

        # Cálculo de valores de saída finais
        out          = []
        for w in self.wo:                                               # Para cada vetor de pesos relacionado a 1 neuronio
            aux = 0
            for i in range(len(H)) :
                aux += H[i]*w[i]                                        # Multiplique o elemento por seu peso correspondente
            
            o = 1/(1+m.exp(-1*aux))                                     # Aplique a função de aplicação a um dado neurônio 

            out.append(o)
        
        return out, H                                                      # Retornar os valores obtidos

    def recalcular_deltas(self, x, out, y, H):

        # -------------------------------------------------
        #  Delta Saída e Back Propagation
        # -------------------------------------------------
        DO           = []                                               # Delta de Saída
        for oy in zip(out,y):
            DO.append(oy[0] * (1 - oy[0]) * (oy[1] - oy[0]))

        # -------------------------------------------------
        #  Delta intermediário e Back Propagation
        # -------------------------------------------------
        aux           = [0 for i in range(self.qtd_hidden)]
        for i in range(len(DO)):                                        # Para cada neurônio na saída
            for w in range(len(self.wo[0])-1):                          # Para cada vetor de pesos relacionado a 1 neuronio da saída
                aux[w] += DO[i]*self.wo[i][w]                           # Para cada auxiliar relacionado a 1 neurônio na intermediária

        DH            = []
        for haux in zip(H,aux):
            DH.append(haux[0]*(1-haux[0])*haux[1])

        # -------------------------------------------------
        #  Ajuste dos pesos mediante os deltas calculados
        # -------------------------------------------------
        for w in range(len(self.wh)):                                   # Para cada vetor associado a um neurônio na intermediária
            for i in range(len(x)):                                     # Para cada peso associado e uma entrada para um neurônio
                self.wh[w][i] += self.ni*DH[w]*x[i]                     

        for w in range(len(self.wo)):                                   # Para cada vetor associado a um neurônio na saída
            for h in range(len(H)):                                     # Para cada peso associado e uma entrada intermediária para um neurônio
                self.wo[w][h] += self.ni*DO[w]*H[h]                   


    def treinar(self, x_input, y):
        x            = x_input.copy()
        x.append(1)
        
        out, H = self.calcular(x=x, y=y)
        self.recalcular_deltas(x=x, out=out, y=y, H=H)

        return out

    def testar(self, x_input, y):
        out, H = self.calcular(x_input=x_input, y=y)

        return out
