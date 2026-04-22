

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def compare_models(X_train, X_test, y_train, y_test):

    models = {
        "Logistic": LogisticRegression(),
        "RandomForest": RandomForestClassifier(),
        "DecisionTree": DecisionTreeClassifier()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"{name} Accuracy:", accuracy_score(y_test, y_pred))