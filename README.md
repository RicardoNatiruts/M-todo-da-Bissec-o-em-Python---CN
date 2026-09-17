# 🧮 Método da Bissecção em Python

Este projeto implementa um algoritmo recursivo em Python para calcular a raiz de uma função matemática utilizando o **Método da Bissecção**. 

O grande diferencial desta implementação é o rigor matemático: o código utiliza a biblioteca nativa `decimal` para evitar as falhas de precisão de ponto flutuante (os famosos "bits de lixo"), cravando os cálculos em exatas **5 casas decimais**.

## ✅ O que já está pronto (Features)

A base lógica e a interface de texto do sistema já estão 100% operacionais:

* **Motor Recursivo (`bisseccao.py`):** Algoritmo que divide o intervalo sucessivamente até encontrar a raiz ou atingir a margem de erro desejada ($e < 0.1$).
* **Precisão Absoluta:** Uso do método `.quantize()` com `ROUND_HALF_UP` em todos os passos da recursão para garantir exatidão em 5 casas decimais.
* **Função Alvo:** Atualmente configurada para resolver $f(x) = x^2 - 3$.
* **Interface de Terminal (`main.py`):** Script principal que recebe o input do usuário e exibe os resultados passo a passo em uma tabela bem formatada.

## 🚧 Próximos Passos

* [ ] **Representação Visual (Plano Cartesiano):** Implementar a plotagem gráfica da função iterada utilizando as bibliotecas `matplotlib` (para desenhar o plano e os eixos). O objetivo é visualizar a curva da função, o intervalo inicial $[a, b]$ e o ponto exato onde a raiz foi encontrada.

## 🚀 Como executar

Certifique-se de ter o Python instalado (versão 3+ recomendada). Nenhuma biblioteca externa é necessária para a versão atual.

1. Clone o repositório ou baixe os arquivos.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```
4. Quando solicitado, digite os valores de `a` e `b` separados por espaço (ex: para a raiz quadrada de 3, tente o intervalo entre `1` e `2`):
   ```text
   Digite a e b: 1 2
   ```

## 📂 Estrutura de Arquivos

* `bisseccao.py`: Contém a lógica matemática, a definição da função $f(x)$ e a função recursiva `bissecao()`.
* `main.py`: Ponto de entrada do programa. Trata a entrada do usuário e exibe a tabela de iterações.