# 📧 Analisador de Contatos – Enron Email Dataset

## 📌 Descrição do Projeto

O objetivo deste trabalho é desenvolver um **analisador de contatos** a partir da base de e-mails [**Enron Email Dataset**](https://www.cs.cmu.edu/~./enron/).

O projeto aplica **teoria dos grafos** para extrair informações úteis da rede de contatos gerada a partir das mensagens de e-mail.

---

## ✅ Funcionalidades

### Construção do Grafo

* [ ] Gerar um **grafo direcionado** a partir das mensagens, considerando remetente e destinatário(s).
* [ ] Tornar o grafo **ponderado** pela frequência de envio de mensagens.
* [ ] Rotular o grafo com os **endereços de e-mail dos usuários**.

### Informações Gerais do Grafo

* [ ] Calcular o **número de vértices**.
* [ ] Calcular o **número de arestas**.
* [ ] Identificar os **20 indivíduos com maior grau de saída** e seus valores.
* [ ] Identificar os **20 indivíduos com maior grau de entrada** e seus valores.

### Algoritmos de Busca

* [ ] Implementar **busca em profundidade (DFS)** para verificar se um indivíduo X alcança Y, mostrando o caminho percorrido.
* [ ] Implementar **busca em largura (BFS)** para verificar se um indivíduo X alcança Y, mostrando o caminho percorrido.

### Distâncias e Caminhos

* [ ] Implementar função que retorna os **nós a uma distância D** de um nó N.
* [ ] Implementar método que calcula o **caminho crítico do fluxo de informação (maior custo acumulado)** entre dois indivíduos, adaptando o algoritmo de **Dijkstra** para considerar `1/peso`.

---

## ⚠️ Observações

* Todos os algoritmos devem **tratar ciclos** (evitar loops infinitos).
