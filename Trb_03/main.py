from matplotlib.pyplot import plot, figure, show, title, xlabel, ylabel, savefig, legend
from numpy import arange, array
from random import randint

from MLP_Treinar import MLP_Treinar

#------------------------------------------------------------------------------------------
#   Fluxo principal de execução
#------------------------------------------------------------------------------------------
def main():
    
    endereco     = "wdbc.data"  

    linhas_base  =  buscar_base(endereco = endereco)
    vetor_linha  = separar_dados(linhas_base=linhas_base)

    vetor_classe = separa_classes(vetor_linha=vetor_linha)


    base_dict    = []
    for classe in vetor_classe:
        dict_class = separa_teste(classe)
        base_dict.append(dict_class)
    
    treinar_container = []
    testar_container  = []

    for dic in base_dict:
        treinar_container.extend(dic['treino'])
        testar_container.extend(dic['teste'])

    base =  {

        'teste': testar_container,
        'treino': treinar_container

    }

    treinar = MLP_Treinar()

    n_x = len(vetor_classe[0][0][0])
    n_y = len(vetor_classe[0][0][1])
    qtd_hidden = 2
    n_epocas   = 30000

    run_dict = treinar.run(
        
                base, 
                n_x=n_x, 
                n_y=n_y, 
                qtd_hidden=qtd_hidden, 
                n_epocas=n_epocas,
        
    )

    plot_classificacao(
        
        cl_teste=run_dict['cl_teste'],
        cl_treino=run_dict['cl_treino'],
        n_epocas=n_epocas,
        
    )

    plot_aproximacao(
        
        ap_teste=run_dict['ap_teste'],
        ap_treino=run_dict['ap_treino'],
        n_epocas=n_epocas,
        
    )


def plot_classificacao(cl_teste, cl_treino, n_epocas):
    
    epocas = arange(start=1, stop=n_epocas+1, step=1)

    treino = array(cl_treino)/len(cl_treino)
    teste = array(cl_teste)/len(cl_teste)

    xlabel('Época')
    ylabel('Classif/i_epoca')

    fig = figure()

    title('Erro de Classificação')

    plot(epocas, teste, label='Teste')
    plot(epocas, treino, label='Treino')

    legend()

    #show()
    savefig(fname='cl.png')

def plot_aproximacao(ap_teste, ap_treino, n_epocas):
    epocas = arange(start=1, stop=n_epocas+1, step=1)

    treino = array(ap_treino)/max(ap_treino)
    teste = array(ap_teste)/max(ap_teste)

    xlabel('Época')
    ylabel('Aprox/i_epoca')

    fig = figure()

    title('Erro de Aproximação')

    plot(epocas, teste, label='Teste')
    plot(epocas, treino, label='Treino')

    legend()

    #show()
    savefig(fname='ap.png')

    
#------------------------------------------------------------------------------------------
#   Busca da base
#------------------------------------------------------------------------------------------
def buscar_base(endereco):
    arquivo = open(endereco, 'r')

    linhas = arquivo.readlines()

    return linhas

#------------------------------------------------------------------------------------------
#   Trabalhando com strings vindas do texto
#------------------------------------------------------------------------------------------
def separar_dados(linhas_base):
    dados = []

    for linha in linhas_base:
        
        linha_2 = linha.replace("\n",'')

        dados.append(
         
            linha_2.split(',')

        )

    return dados

#------------------------------------------------------------------------------------------
#   Separando classes R - B - L da base
#------------------------------------------------------------------------------------------
def separa_classes(vetor_linha):
    classe_m = []
    classe_b = []

    for linha in vetor_linha:

        classe = linha[1]

        vet = []
        for i in range(2,len(linha)):
            vet.append(float(linha[i]))

        if classe == 'M':
            classe_m.append([vet,[0.05,0.95]])

        elif classe == 'B':
            classe_b.append([vet,[0.95,0.05]])

    return [classe_m, classe_b]

#------------------------------------------------------------------------------------------
#   Separando dois conjuntos: teste e treino
#------------------------------------------------------------------------------------------
def separa_teste(base):

    teste = []

    tamanho = len(base)
    #print(tamanho)

    q = int((tamanho/100)*20 + 1)

    for i in range(q):
        aux = randint(0,len(base)-1)
        teste.append(base.pop(aux))

    sep_base = {
        
        'treino' : base,
        'teste' : teste

    }

    return sep_base


if __name__ == '__main__':
    main();

    #print(separa_classes([[1110524,10,5,5,6,8,8,7,1,1,4]]))
