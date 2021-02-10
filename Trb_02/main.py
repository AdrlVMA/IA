from random import randint

#------------------------------------------------------------------------------------------
#   Fluxo principal de execução
#------------------------------------------------------------------------------------------
def main():
    
    endereco     = "Trb_02/balance-scale.data"  

    linhas_base  =  buscar_base(endereco = endereco)
    vetor_linha  = separar_dados(linhas_base=linhas_base)

    vetor_classe = separa_classes(vetor_linha=vetor_linha)

    vetor_dict = []
    for classe in vetor_classe:
        dict_class = separa_teste(classe)
        vetor_dict.append(dict_class)
    
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
    classe_r = []
    classe_b = []
    classe_l = []
    
    for linha in vetor_linha:
        
        name = linha[0]
    
        d2 = int(linha[1])
        d3 = int(linha[2])
        d4 = int(linha[3])
        d5 = int(linha[4])

        if name == 'R':
            classe_r.append([[d2,d3,d4,d5],[0,0,1]])

        elif name == 'B':
            classe_b.append([[d2,d3,d4,d5],[0,1,0]])

        elif name == 'L':
            classe_l.append([[d2,d3,d4,d5],[1,0,0]])

    return [classe_r, classe_b, classe_l]

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
