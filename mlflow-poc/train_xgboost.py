import mlflow.xgboost
import xgboost as xgb
import mlflow
import argparse

def load_dataset(path:str, target_col:str, test_size:float=0.2):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    df = pd.read_csv(path)
    X = pd.get_dummies(df.drop(columns=[target_col]))
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    mlflow.log_param("test_size", test_size)
    mlflow.log_param("data_path", path)
    mlflow.log_param("target_col", target_col)
    mlflow.log_param("onehot_encoding", True)
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="bank-additional/bank-additional-full.csv", help="Path to dataset")
    parser.add_argument("--target_col", type=str, default="y", help="Target column name")
    parser.add_argument("--test_size", type=float, default=0.2, help="Test size")
    args = parser.parse_args()
    data_path = args.path
    target_col = args.target_col
    test_size = args.test_size

    mlflow.set_experiment("dm-xgboost")
    with mlflow.start_run(run_name="dm-xgboost-basic") as run:
        x_train, x_test, y_train, y_test = load_dataset(data_path, target_col, test_size)
        cls = (xgb.XGBClassifier(n_estimators=100, 
        max_depth=3, 
        objective="binary:logistic", 
        eval_metric="auc"))
        cls.fit(x_train, y_train)
        auc = cls.score(x_test, y_test)
        mlflow.log_metric("auc", auc)
        mlflow.xgboost.log_model(cls, "dm-xgboost-model")
        mlflow.end_run()