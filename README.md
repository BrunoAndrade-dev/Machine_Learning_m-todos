## 🛠️ README do Projeto: Regressão Linear no Boston Housing

Este README lista todas as ferramentas, bibliotecas e pacotes utilizados no desenvolvimento e avaliação do modelo de Regressão Linear para o *Boston Housing Dataset*.

***

### 1. Linguagem de Programação

| Linguagem | Uso Principal |
| :--- | :--- |
| **Python** 🐍 | Linguagem principal para todo o desenvolvimento, análise de dados e treinamento do modelo. |

***

### 2. Bibliotecas Essenciais para Ciência de Dados (PyData Stack)

| Biblioteca | Propósito Principal |
| :--- | :--- |
| **Pandas** | Utilizada para o **tratamento de dados** (`tabela.dropna()`), manipulação do *DataFrame*, e separação das variáveis *features* (`X`) e *target* (`Y`). |
| **NumPy** | Utilizada indiretamente pela maioria das bibliotecas e explicitamente para manipulação eficiente de *arrays* numéricos. |
| **Matplotlib** | Utilizada para a **visualização** dos resultados, especificamente para gerar o **Gráfico de Dispersão (Real vs. Previsto)** e salvar a imagem (`plt.savefig`). |

***

### 3. Bibliotecas do Scikit-learn (Machine Learning)

| Módulo/Classe | Propósito Principal |
| :--- | :--- |
| **`sklearn.model_selection`** | Contém a função **`train_test_split`**, crucial para dividir os dados nos conjuntos de treino e teste. |
| **`sklearn.linear_model`** | Contém a classe **`LinearRegression`**, o modelo de regressão principal utilizado para o treinamento (`modelo.fit`) e previsão (`modelo.predict`). |
| **`sklearn.metrics`** | Contém as funções de avaliação **`mean_squared_error`** (MSE) e **`r2_score`** ($R^2$), utilizadas para quantificar o desempenho do modelo. |

***

### 4. Ferramentas e Conceitos Fundamentais

| Ferramenta/Conceito | Aplicação no Projeto |
| :--- | :--- |
| **Tratamento de NaN** | Uso do método **`.dropna()`** no *DataFrame* para remover linhas com valores ausentes. |
| **F-strings** | Utilizadas na formatação dos resultados para garantir **duas casas decimais** (`{variavel:.2f}`). |
| **Boston Housing Dataset** | O **conjunto de dados** alvo do projeto, utilizado para prever o valor mediano das casas (`MEDV`). |