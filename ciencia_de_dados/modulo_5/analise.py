import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# 1. Carregar e preparar dados
df = pd.read_csv(
    '/home/pratinha/pessoal/academico/UNIFEI/atividades-unifei/ciencia_de_dados/modulo_5/dados_historicos_bbsa3.csv',
    sep=','
)
df.rename(columns={
    'Data': 'Date',
    'Abertura': 'Open',
    'Máxima': 'High',
    'Mínima': 'Low',
    'Último': 'Close',
    'Vol.': 'Volume',
    'Var%': 'ChangePct'
}, inplace=True)

# 2. Converter colunas numéricas
for col in ['Open', 'High', 'Low', 'Close', 'ChangePct']:
    df[col] = (
        df[col].astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .str.replace('%', '', regex=False)
        .astype(float)
    )

vol = df['Volume'].astype(str).str.replace('M', '', regex=False)
df['Volume'] = vol.str.replace(',', '.', regex=False).astype(float) * 1e6

# 3. Parse de datas e criação de alvo
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['target'] = (df['Open'] - df['Close'] > 0).astype(int)

# 4. Remover missing e separar treino/teste
df = df.dropna(subset=['Open','High','Low','Close','Volume','ChangePct','target','Year'])
train = df[df['Year'].isin([2023, 2024])]
test  = df[df['Year'] == 2025]

X_train = train[['Open','High','Low','Close','Volume','ChangePct']]
y_train = train['target']
X_test  = test[['Open','High','Low','Close','Volume','ChangePct']]
y_test  = test['target']

# 5. Grid Search com TimeSeriesSplit
param_grid = {
    'max_depth':        [3, 5, 7, None],
    'min_samples_leaf': [1, 5, 10],
    'criterion':        ['gini', 'entropy']
}
tscv = TimeSeriesSplit(n_splits=5)
grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=tscv,
    scoring='f1',
    n_jobs=-1,
    return_train_score=True
)
grid.fit(X_train, y_train)

# 6. Avaliação final
best_dt = grid.best_estimator_
y_pred = best_dt.predict(X_test)

print("Melhores parâmetros:", grid.best_params_)
print(f"Acurácia no teste (2025): {accuracy_score(y_test, y_pred):.2f}\n")
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
    