# Entendendo algoritmos

## Recapitulando:

### Capítulo 01 - Pesquisa binária | Notação Big O | Recursão:

- A pesquisa binária é muito mais rápida que a pesquisa simples.
- O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme os elementos da lista aumentam.
- A rapidez de um algoritmo não é medida em segundos.
- O tempo de execução de um algoritmo é medido por meio de seu crescimento.
- O tempo de execução de um algoritmo é expresso na notação Big O.

### Capítulo 02 - Ordenação por seleção | arrays e listas encadeadas:

- A memória do seu computador é como um conjunto gigante de gavetas.
- Quando se quer armazenar múltiplos elementos, usa-se um array ou uma lista.
- No array, todos os elementos são armazenados um ao lado do outro.
- Arrays permitem leituras rápidas.
- Listas encadeadas permitem rápidas inserções e eliminações.
- Todos os elementos de um array devem ser do mesmo tipo (todos ints, todos doubles, e assim por diante).

### Capítulo 03 - Recursão:

- Recursão é quando uma função chama a si mesma.
- Toda função recursiva tem dois casos: o caso-base e o caso recursivo.
- Uma pilha tem duas operações: push e pop.
- Todas as chamadas de função vão para a pilha de chamada.
- A pilha de chamada pode ficar muito grande e ocupar muita memória. 

### Capítulo 04 - Quicksort:

- A estratégia Dividir pra Conquistar (DC) funciona por meio da divisão do problema em problemas menores. Se você estiver utilizando DC em uma lista, o caso base provavelmente será um array vazio ou com um elemento.
- Se você estiver implementando o Quicksort, escolha um elemento aleatório como pivô. O tempo de execusão médio do quicksort é O(n log n)!
- A constante na notação Big O, pode ser relevante em alguns casos. Esta é a razão pela qual o quicksort é mais rápido do que o merge sort.
- A constante dificilmente será relevante na comparação entre a pesquisa simples e a pesquisa binária, pois O(log n) é muito mais rápido do que O(n) quando sua lista é grande.

### Capítulo 05 - Tabela hash:

- Você provavelmente nunca terá de implementar uma tabela hash.
- As tabelas hash são estruturas de dados poderosas, pois elas são muito rápidas e possibilitam a modelagem de dados de uma forma diferente.
- Você pode fazer uma tabela hash ao combinar uma função hash com um array.
- Colisões são problemas. É necessário haver uma função hash que minimize colisões.
- As tabelas hash são extremamente rápidas para pesquisar, inserir e remover itens.
- São boas para modelar relações entre dois itens.
- Se o seu fator de carga for menor que 0.7, será necessário redimensionar sua tabela hash.
- As tabelas hash são utilizadas como cach de dados (como em um servidor web, por exemplo).
- Tabelas hash são ótimas para localizar duplicatas.

