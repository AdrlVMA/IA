from MLP import MLP
from RNA import RNA
import random

class MLP_Treinar(RNA):

    def treinar(self, base, qtd_hidden):
        n_x = len(base[1][0])
        n_y = len(base[1][1])

        #print([n_x, n_y])

        rna = MLP(qtd_input=n_x, qtd_hidden = qtd_hidden, qtd_output=n_y)

        for e in range(0,300000):
            erroEpoca = 0
            erro_classificacao = 0

            for a in range(0, len(base)):
                amostra = base[a]
                x = amostra[0]
                y = amostra[1]

                # Saída da Rede Neural
                out = rna.treinar(x, y)

                # Calculo do erro simples
                err = []
                for er in zip(out,y):
                    err.append(abs(er[0]-er[1]))

                # Erro de aproximação
                for er in err:
                    erroEpoca += er

                
                # Erro de Classificação 01
                vet_cla = []
                for o in out:
                    if o>=0.5:
                        vet_cla.append(1)
                    else:
                        vet_cla.append(0)

                aux = 0
                for v in zip(vet_cla,y):
                    aux +=abs(v[1]-v[0])

                ecl = 0
                if aux>0:
                    ecl = 1

                erro_classificacao +=  ecl

            print('Época: {}'.format(e+1), end=' --- ')
            print('Erro: {}'.format(erroEpoca), end=' --- ')
            print('Classificação: {}'.format(erro_classificacao))

    def run(self, base, n_x, n_y, qtd_hidden, n_epocas):
        
        cl_vet_treino = []
        ap_vet_treino = []

        cl_vet_teste = []
        ap_vet_teste = []
        
        rna = MLP(qtd_input=n_x, qtd_hidden = qtd_hidden, qtd_output=n_y)

        for e in range(0,n_epocas):
            
            treino_dict = self.treinar(base['treino'], rna)
            teste_dict  = self.treinar(base['teste'], rna)

            e_ap_teste = teste_dict['eEpoca']
            e_cl_teste = teste_dict['eClass']
            e_ap_treino = treino_dict['eEpoca']
            e_cl_treino = treino_dict['eClass']

            cl_vet_treino.append(e_cl_treino)
            ap_vet_treino.append(e_ap_treino)

            cl_vet_teste.append(e_cl_teste)
            ap_vet_teste.append(e_ap_teste)

            print('Época: {}'.format(e+1), end=' - ')
            print('Treino ap: {}'.format(e_ap_treino), end=' - ')
            print('Treino cl: {}'.format(e_cl_treino), end=' - ')
            print('Teste ap: {}'.format(e_ap_teste), end=' - ')
            print('Teste cl: {}'.format(e_cl_teste))

        run_dict = {

            'cl_treino': cl_vet_treino,
            'ap_treino': ap_vet_treino,
            'cl_teste': cl_vet_teste,
            'ap_teste': ap_vet_teste

        }

        return run_dict

    
    def treinar(self, base_treino, rna):
        erroEpoca = 0
        erro_classificacao = 0
        
        random.shuffle(base_treino)

        for a in range(0, len(base_treino)):
            
            amostra = base_treino[a]

            x = amostra[0]
            y = amostra[1]
            
            # Saída da Rede Neural
            out = rna.treinar(x, y)

            # Calculo do erro simples
            err = []
            for er in zip(out,y):
                err.append(abs(er[0]-er[1]))

            # Erro de aproximação
            for er in err:
                erroEpoca += er
            
            # Erro de Classificação 01
            vet_cla = []
            for o in out:
                if o>=0.5:
                    vet_cla.append(1)
                else:
                    vet_cla.append(0)

            aux = 0
            for v in zip(vet_cla,y):
                aux +=abs(v[1]-v[0])

            ecl = 0
            if aux>0:
                ecl = 1

            erro_classificacao +=  ecl

        treino_dict = {
            
            'eEpoca': erroEpoca,
            'eClass': erro_classificacao

        }

        return treino_dict

    def testar(self, base_teste, rna):
        erroEpoca = 0
        erro_classificacao = 0

        #random.shuffle(base_teste)

        for a in range(0, len(base_treino)):
        
            amostra = base_teste[a]

            x = amostra[0]
            y = amostra[1]
            
            # Saída da Rede Neural
            out = rna.testar(x, y)


            # Calculo do erro simples
            err = []
            for er in zip(out,y):
                err.append(abs(er[0]-er[1]))

            # Erro de aproximação
            for er in err:
                erroEpoca += er

            
            # Erro de Classificação 01
            vet_cla = []
            for o in out:
                if o>=0.5:
                    vet_cla.append(1)
                else:
                    vet_cla.append(0)

            aux = 0
            for v in zip(vet_cla,y):
                aux +=abs(v[1]-v[0])

            ecl = 0
            if aux>0:
                ecl = 1

            erro_classificacao +=  ecl

        teste_dict = {
            
            'eEpoca': erroEpoca,
            'eClass': erro_classificacao

        }

        return teste_dict