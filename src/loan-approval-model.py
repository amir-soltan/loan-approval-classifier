import pandas as pd
import numpy as np
df = pd.read_csv('loan_approval_dataset.csv')
#check null values
#(df.isnull().sum())
self_employed = {' Yes':1 , ' No':0}
df['self_employed'] = df['self_employed'].map(self_employed)
df['education'] = df['education'].map({' Graduate': 1, ' Not Graduate': 0})
df[' loan_status'] = df[' loan_status'].map({' Approved': 1, ' Rejected': 0})
df = df.drop('loan_id', axis=1)
y = df[' loan_status']
X = df.drop(' loan_status', axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
from sklearn.metrics import r2_score
def evaluate(name, y_true , y_pred):
    r2 = r2_score(y_true, y_pred)
    print(f"{name}")
    print(f"R2:   {r2:.4f}")
from sklearn.ensemble import RandomForestClassifier
modelXGB = XGBClassifier()
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate('Random Forest', y_test, y_pred)