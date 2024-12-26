from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd


def train_model(data_path: str, model_path: str):
    data = pd.read_excel(data_path)
    x, Y = data['text'], data['label']

    # split into train and test
    X_train, X_test, y_train, y_test = train_test_split(x,Y,test_size=0.2,random_state=42)

    # creating a pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('svm', SVC(kernel='linear', probability=True))
    ])

    #train model
    pipeline.fit(X_train,y_train)

    #test model
    y_pred = pipeline.predict(X_test)

    print(f'Accuracy: {accuracy_score(y_test,y_pred):.2f}')

    #save model
    joblib.dump(pipeline, model_path)
    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    train_model("data\dataset.xlsx", "model\svm_model.pkl")

