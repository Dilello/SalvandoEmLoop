
# Definir o caminho de saida

CaminhoDadoSaida = 'Documents/Projetos/OrlaSemLixo/Linha1/'

# Definir o nome dos arquivos de saida (sem a extensao .txt, .csv, .png):

NomeArquivoSaida = 'NomeArquivo' 

# Definir a quantidade de arquivos de saida:

NumArquivo = 5

# ARQUIVOS TXT OU PNG

for i in range(NumArquivo):
    # Entrar com uma VARIAVEL de uma FUNÇÃO
    with open(CaminhoDadoSaida+NomeArquivoSaida+str(i+1)+'.txt', 'w') as f:
        f.write(str(VARIAVEL))


# FIGURAS PNG, JPG OU PDF


for i in range(NumArquivo):
    # Entrar com uma VARIAVEL de uma FUNÇÃO
    plt.savefig(CaminhoDadoSaida+NomeArquivoSaida+str(i+1)+'.jpg', dpi = 300, bbox_inches='tight')
    plt.show()

