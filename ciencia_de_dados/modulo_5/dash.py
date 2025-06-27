# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

st.set_page_config(page_title="Dashboard BBSA3", layout="wide")

@st.cache_data
def load_and_prepare(path):
    df = pd.read_csv(path, sep=',')
    df.rename(columns={
        'Data':'Date','Abertura':'Open','Máxima':'High','Mínima':'Low',
        'Último':'Close','Vol.':'Volume','Var%':'ChangePct'
    }, inplace=True)
    # numeric conversions
    for col in ['Open','High','Low','Close','ChangePct']:
        df[col] = (
            df[col].astype(str)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
            .str.replace('%', '', regex=False)
            .astype(float)
        )
    vol = df['Volume'].astype(str).str.replace('M','', regex=False)
    df['Volume'] = vol.str.replace(',', '.', regex=False).astype(float) * 1e6
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Year'] = df['Date'].dt.year
    # target: 1 if Open > Close else 0
    df['target'] = (df['Open'] - df['Close'] > 0).astype(int)
    df = df.dropna(subset=['Open','High','Low','Close','Volume','ChangePct','target'])
    return df

df = load_and_prepare('/home/pratinha/pessoal/academico/UNIFEI/atividades-unifei/ciencia_de_dados/modulo_5/dados_historicos_bbsa3.csv',
)

st.title("📊 Dashboard de BBSA3 com Decision Tree")

# --- Sidebar for training year selection ---
st.sidebar.header("Configuração de Treino")
years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect("Anos de Treinamento", years, default=[2023, 2024])

train = df[df['Year'].isin(selected_years)]
test  = df[df['Year'] == 2025]

features = ['Open','High','Low','Close','Volume','ChangePct']
X_train, y_train = train[features], train['target']
X_test,  y_test  = test[features],  test['target']

# --- Train with GridSearchCV ---
param_grid = {
    'max_depth':        [3,5,7,None],
    'min_samples_leaf': [1,5,10],
    'criterion':        ['gini','entropy']
}
tscv = TimeSeriesSplit(n_splits=5)
grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=tscv,
    scoring='f1',
    n_jobs=-1
)
grid.fit(X_train, y_train)
best = grid.best_estimator_
y_pred = best.predict(X_test)

# --- Metrics and confusion ---
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
specificity = tn / (tn + fp)

# --- Financial returns ---
test = test.copy()
test['pred'] = y_pred
# daily pct return: (Close - Open)/Open * 100
test['ret_pct'] = (test['Close'] - test['Open']) / test['Open'] * 100
# gains: days where true movement was up (target=1)
gains = test.loc[test['target'] == 1, 'ret_pct'].sum()
losses = test.loc[test['target'] == 0, 'ret_pct'].sum()
net = gains + losses

# --- Layout ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("Série Temporal de Fechamento")
    st.line_chart(df.set_index('Date')['Close'])

with col2:
    st.subheader("Distribuição das Classes (Teste)")
    class_counts = y_test.value_counts(normalize=True).sort_index() * 100
    st.bar_chart(class_counts)

    st.write("**Percentual por classe:**")
    st.write(class_counts.rename({0:'Queda (0)', 1:'Alta (1)'}).to_frame('%'))

# --- Predictions performance ---
st.markdown("## Desempenho de Previsão (2025)")
perf_col1, perf_col2, perf_col3 = st.columns(3)
perf_col1.metric("Acurácia", f"{acc:.2%}")
perf_col2.metric("Precision / Recall", f"{prec:.2%} / {rec:.2%}")
perf_col3.metric("F1-score / Especificidade", f"{f1:.2%} / {specificity:.2%}")

st.markdown("### Acertos vs Erros")
correct = int((y_pred == y_test).sum())
incorrect = int((y_pred != y_test).sum())
st.write(f"- Acertos: **{correct}**")
st.write(f"- Erros: **{incorrect}**")

# --- Financial summary ---
st.markdown("## Retorno Financeiro (2025)")
fin_col1, fin_col2, fin_col3 = st.columns(3)
fin_col1.metric("Total Ganhos (%)", f"{gains:.2f}%")
fin_col2.metric("Total Perdas (%)", f"{losses:.2f}%")
fin_col3.metric("Retorno Líquido (%)", f"{net:.2f}%")
