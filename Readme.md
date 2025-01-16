# Readme 📜

Bem-vindo(a) ao repositório request_discorgs! Aqui você encontrará o passo a passo da construção do projeto e todas as ações importantes necessárias para sua execução.

# Planejamento ☕️

O projeto consiste em capturar dados de artistas e seus álbuns no site Discogs **(https://www.discogs.com/pt_BR/)**. Inicialmente, foi feito um estudo da estrutura do site para, posteriormente, capturar dados específicos, como artistas, detalhes atribuídos a eles e aos seus álbuns.

# Mapeamento 📜
O primeiro passo foi realizar uma pesquisa para entender a estrutura do site e como funcionam as requisições. Cheguei à página de documentação da API **https://www.discogs.com/developers/#**.

Durante o desenvolvimento, encontrei um erro ao tentar utilizar o import requests, que foi corrigido ao atualizar o Python para a versão 3.12. Após a API, percebi a necessidade de gerar um token de acesso no próprio site, após efetuar o login, acessando essa página **https://www.discogs.com/pt_BR/settings/developers**.

# Construção ✨

O projeto tem como objetivo realizar uma requisição para capturar dados sobre:


* Gênero
* Nome do artista
* Membros do artista
* Sites do artista
* Ano de lançamento do álbum
* Nome do álbum
* Gravadora do álbum
* Faixas do álbum
* Duração de cada faixa
* Número da faixa
* Estilos do álbum


A requisição é feita de maneira estruturada, com blocos separados para captura e alocação dos dados, organizados por ID's retornados em formato JSON. O uso de **time_sleep** foi implementado para evitar o **erro 429 (Timeout)**, que ocorre quando as requisições são feitas em um curto período de tempo.

# Execução do final_file.py 🔥

Neste arquivo, a estrutura foi organizada para facilitar a visualização e compreensão do projeto. Os dados são capturados em blocos distintos, com tratamento de erros utilizando try e except para evitar excessos de if/elif/else.

Os artistas estão previamente definidos nas listas, e, para alterá-los, será necessário modificar as listas e as referências no código.

# Para executar o código final_file:✨

Abra o arquivo na sua IDE (VScode) e clique em "run", ou execute o código diretamente no terminal com o comando:

**python final_file.py**

O script irá gerar um arquivo JSON com todos os dados solicitados.
Caso ocorram erros relacionados aos imports, verifique se as bibliotecas estão instaladas. Se necessário, instale-as com o comando:
**pip3 install requests**

# Execução do teste-argparse.py ✨

Neste arquivo, a estrutura é semelhante ao código anterior, mas foi implementada a utilização da biblioteca argparse. O código agora permite que você passe parâmetros diretamente para a API Discogs, utilizando a URL https://api.discogs.com/database/search.

**Para executar o código:**
Execute o script passando o nome de um ou mais artistas como argumento:

*python teste-argparse.py "Nirvana"* ou *python teste-argparse.py "Nirvana","Nickelbak, "Dua Lipa"*

O código irá gerar um arquivo JSON com os dados dos artistas consultados, permitindo que a API faça a busca com base nos parâmetros fornecidos.

# Exemplo de retorno em Json:

![image](https://github.com/user-attachments/assets/00422c4d-5ec9-41d9-98bf-189e8d35cb85)


# Importante: Verifique se as bibliotecas necessárias estão instaladas ⚠️ 

Nesse projeto não foi necessária um arquivo com as dependencias conhecido como **requirements.txt** , por apenas precisar da lib **requests*.



