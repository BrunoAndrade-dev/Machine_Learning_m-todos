import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score  , classification_report , confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os 


st.title ('Método random forest - Análise de dados do Titanic (taxa de sobreviventes)')
st.write('Exibição da acurácia e outras métricas do modelo')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Caminho até o CSV
csv_path = os.path.join(BASE_DIR, '..', '..', 'dados', 'dados_processados', 'titanic_tratado_final.csv')


df = pd.read_csv(csv_path)
st.dataframe (df.head())
print(csv_path)
print(os.path.exists(csv_path))


features = ['Pclass' , 'Age' , 'SibSp' , 'Parch' ,'Fare' , 'Sex' , 'Embarked']
X = df[features]
Y = df['Survived']
X_train , X_test , Y_train , Y_test = train_test_split (X ,Y , test_size  = 0.3 , random_state = 42 , stratify = Y)
print (f'Shape de x_TREINO {X_train.shape }')
print (f'Shape de x_TESTE {X_test.shape }')
modelo_random_forest = RandomForestClassifier (
    n_estimators = 100 , max_depth = 5 , random_state = 42
)

print ('Iniciando o aperfeiçoamento do modelo...')
modelo_random_forest.fit (X_train , Y_train)
print ('Aperfeiçoamento concluído!')
previsoses = modelo_random_forest.predict(X_test)
acuracia = accuracy_score(Y_test , previsoses)
relatorio = classification_report(Y_test, previsoses, output_dict=True)
matriz_confusao = confusion_matrix(Y_test, previsoses)
print (f'----------------------Resultados-------------------')
print (f'Acurácia do modelo : {acuracia *100 :.2f}')
print ('Relatório de Classificação :')
print (classification_report(Y_test , previsoses))
print ('-----------------------------------------------------')

variaveis_importantes = pd.Series (modelo_random_forest.feature_importances_ , index = features).sort_values(ascending = False)
print ('Variáveis mais importantes para o modelo :')
print (variaveis_importantes)

#Exibição Streamlit
st.header("Resultados do Modelo Random Forest")
st.markdown('---')
 
col1 , col2 , col3 , col4 = st.columns(4)
with col1 :
    st.metric(label='Acurácia Geral' , value = f'{acuracia * 100:.2f}%' , delta ='O percentual de acertos do modelo no conjunto de teste')

with col2 :
    st.metric(label= 'Precisão Média' , value = f'{relatorio['weighted avg']['precision']*100:.2f}%')

with col3 : 
    st.metric(label = 'Recall Médio' , value = f'{relatorio['weighted avg']['recall'] * 100:.2f}%')    

with col4 :
    st.metric(label = 'F1-Score Médio' , value = f'{relatorio['weighted avg']['f1-score'] * 100:.2f}%')        

st.markdown('---')

st.header("Relatório")

col_a , col_b = st.columns(2)

with col_a : 
    st.subheader('Relatório de Classificação')
    relatorio_df = pd.DataFrame(relatorio).transpose().round(2)
    st.dataframe(relatorio_df)
    st.caption ("Classes : 0 ( sobreviveu) e 1 (não sobreviveu)")

with col_b : 
    st.subheader('Matriz de Confusão')
    fig , ax = plt.subplots()
    sns.heatmap(matriz_confusao , annot = True , fmt ='d' , cmap = 'Blues', ax = ax , xticklabels=['Previsto 0 ' , 'Não Previsto 1 '] , yticklabels = ['Real 0 ' , 'Não Real 1'])
    ax.set_xlabel('Rótulos Verdadeiros')
    ax.set_ylabel('Rótulos Preditos')
    st.pyplot(fig)

st.markdown('---')

st.header('Importância das Variáveis')
st.bar_chart(variaveis_importantes)

