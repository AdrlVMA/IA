
#------------------------------------------------------------------------------------------
#   Fluxo principal de execução
#------------------------------------------------------------------------------------------
def main():
    
    endereco    = "balance-scale.data"   

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
def separar_dados(linhas):
    dados = []

    for linha in linhas:
        
        linha_2 = linha.replace("\n",'')

        dados.append(
         
            linha_2.split(',')

        )

    return dados

#------------------------------------------------------------------------------------------
#   Separando classes R - B - L da base
#------------------------------------------------------------------------------------------
def separa_classes(dados):
    classe_r = []
    classe_b = []
    classe_l = []
    
    for l in dados:
        nome = converte_nome(l[0])
        
        d2 = int(l[1])
        d3 = int(l[2])
        d4 = int(l[3])
        d5 = int(l[4])

        if name == 'R':
            classe_r.append([[d2,d3,d4,d5],[0,0,1])

        elif name == 'B':
            classe_b.append([[d2,d3,d4,d5],[0,1,0])

        elif name == 'L':
            classe_l.append([[d2,d3,d4,d5],[1,0,0])

    return [classe_r, classe_b, classe_l]

#------------------------------------------------------------------------------------------
#   Separando dois conjuntos: teste e treino
#------------------------------------------------------------------------------------------
def separa_teste(base):

    teste = []

    tamanho = len(base)

    q = int((tamanho/100)*20 + 1)

    for i in range(q):
        aux = randint(0,len(base))
        teste.append(base.pop(aux))

    sep_base = {
        
        'treino' : base,
        'teste' : teste

    }

    return separa_base


if __name__ == '__main__':
    main();