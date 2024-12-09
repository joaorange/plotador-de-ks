Para a visualização do KS, criei um software simples no python para realizar de forma mais automatizada.

Só é necessário, nele, preencher o separador do CSV analisado; decimal, se houver; coluna do evento (no caso, a coluna de marcação, que diz se o cliente é bom ou mau); coluna de probabilidade (coluna do score); valor do evento (no caso, o que desejamos, cliente ser bom, para o programa converter em "1"); e valor do não evento (no caso, o cliente ser mau).

![imagem ks](https://github.com/user-attachments/assets/6ace7b2c-b2c1-4a94-a282-fb295b67bccc)

Após isso, selecionamos o CSV e o gráfico é gerado. 

![figure ks](https://github.com/user-attachments/assets/31cb301e-a90f-4877-ab61-91c9e13a195f)

O indicador do KS, basicamente, mede o quão bem o modelo distingue entre duas categorias, o que para o mercado de crédito, geralmente, é se o cliente é bom ou mau. 
O modelo indicado deu um valor de 0.57 de KS, o que representa uma eficácia excelente para um modelo de crédito, que tem como norte ter 0.30 ou quiçá 0.40 na maioria dos casos.
