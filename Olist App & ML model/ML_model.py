# Modelo y performance
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Manipulación de la data
import pandas as pd
import numpy as np

def transform(df, target='', test_size=False, random_state=False, ros=False):

    ord_enc = OrdinalEncoder(dtype=np.int64)
    one_hot = OneHotEncoder(dtype=np.int64)

    columns_to_ordinal = ['product_id', 'seller_id', 'customer_id', 'cod_estado_customer', 'cod_estado_seller']
    columns_to_one_hot = ['payment_type']

    df[columns_to_ordinal] = ord_enc.fit_transform(df[columns_to_ordinal])
    df_one_hot = one_hot.fit_transform(df[columns_to_one_hot]).toarray()
    df_one_hot_labels = np.concatenate(one_hot.categories_).tolist()
    df_one_hot = pd.DataFrame(df_one_hot, columns=df_one_hot_labels)
    df = pd.concat([df, df_one_hot], axis=1)
    df.drop('payment_type', axis=1, inplace=True)

    df[[target]] = df[[target]].mask(df[[target]] <= 3, 0)
    df[[target]] = df[[target]].mask(df[[target]] > 3, 1)

    y = df[[target]]
    X = df.drop(target, axis=1)

    scaler = StandardScaler()

    if test_size:

        if ros:
            ros = RandomOverSampler(sampling_strategy=ros)
            X, y = ros.fit_resample(X, y)

        X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        X_Train = scaler.fit_transform(X_Train)
        X_Test = scaler.transform(X_Test)

        return X_Train, X_Test, Y_Train, Y_Test

    else:

        X = scaler.fit_transform(X)

        return X, y

df_train_test = pd.read_csv('datasets\olist_to_train_test.csv')
X_Train, X_Test, Y_Train, Y_Test = transform(df_train_test, target='review_score', test_size=0.15, random_state=42, ros=0.60)

pipe = Pipeline([('GaussianNB', GaussianNB())])

pipe.fit(X_Train, Y_Train.values.ravel())
gaus_Y_Pred = pipe.predict(X_Test)

joblib.dump(pipe, 'Olist App & ML model\GaussPipeline.pkl')

#classification_report
print(classification_report(Y_Test, gaus_Y_Pred))
