from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def get_model(churn):
    #Handle missing values
    churn=churn.dropna()

    #Scaling
    scaler=StandardScaler()
    for col in churn.select_dtypes(include=float):
        churn[col]=scaler.fit_transform(churn[[col]])

    #Encoding
     #Encoding
    for col in churn.select_dtypes(include=str):
        churn[col]=churn[col].map(lambda val:list(churn[col].unique()).index(val))


    #Model Training
    dbscan=DBSCAN(eps=1.5,min_samples=20)
    labels=dbscan.fit_predict(churn)
    print("------------------")
    print(labels)
    return labels
