# Desafio de Aprendizado de Máquina: Random Forest no Titanic
 

## Objetivo do Projeto 

- Criação de uma interface interativa com streamlit para a visualização do método de aprendizado de máquina - Random Forest
- Aprender e demonstrar etapas de pré-processamento de dados, treinamento de modelo e análise de métricas.

## Etapas do projeto 

- Importação do dataset Titanic, da plataforma Kaggle, para tratamento e organização
- Implementação do Random Forest 
- Criação da interface com streamlit, possibilitando a visualização dos resultados, relatório e matriz de confusão

### Tecnologias utilizadas

- Python 3.11
- Pandas
- Numpy
- Scikit-learn
- Seaborn / Matplotlib
- Streamlit
- Git / GitHub

## Estrutura do projeto 

Machine_learning_random_forest/
├── .devcontainer/
├── .git/
├── .venv/
├── dados/
│   ├── dados_brutos/
│   ├── dados_processados/
│   └── titanic_tratado_final.csv
├── outputs/
│   ├── figures/
│   └── modelos/
├── source/
│   ├── funcoes_auxiliares/
│   │   ├── funcoes_ML.py
│   │   └── funcoes_tratar_dados.py
│   ├── app.py
│   └── README.md
├── .gitignore
├── main.py
├── Notebook/
│   └── analise.ipynb
├── requirements.txt
└── README.md

## Instalação 

### Clonar o repositório
git clone https://github.com/BrunoAndrade-dev/Machine_Learning_m-todos

### Entrar na pasta do projeto
cd Machine_learning_m-todos

### Criar ambiente virtual
python -m venv .venv

### Ativar ambiente (Windows)
.venv\Scripts\activate

### Instalar dependências
pip install -r requirements.txt

### Rodar a aplicação Streamlit
streamlit run source/funcoes_auxiliares/app.py
