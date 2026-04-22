from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import joblib

class ModelSelector:

    def train_and_select(self, X_train, X_test, y_train, y_test):

        models = {
            "Logistic": LogisticRegression(max_iter=1000),
            "RandomForest": RandomForestClassifier(),
            "DecisionTree": DecisionTreeClassifier()
        }

        best_model = None
        best_score = 0

        '''
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            score = accuracy_score(y_test, y_pred)

            print(f"{name} Accuracy: {score}")

            if score > best_score:
                best_score = score
                best_model = model

        print(f"\nBest Model Selected: {best_model}")

        joblib.dump(best_model, "src/models/model.pkl")
        '''
        print("\n========== MODEL EVALUATION ==========\n")

        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred)
            rec = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)

            print(f"{name}")
            print(f" Accuracy : {acc}")
            print(f" Precision: {prec}")
            print(f" Recall   : {rec}")
            print(f" F1 Score : {f1}")
            print("-----------------------------------")

            # Choose best based on F1 (better than accuracy)
            if f1 > best_score:
                best_score = f1
                best_model = model

        print("\n========== BEST MODEL SELECTED ==========")
        print(best_model)
        print(f"Best F1 Score: {best_score}")
        print("================================\n")

        joblib.dump(best_model, "src/models/model.pkl")
