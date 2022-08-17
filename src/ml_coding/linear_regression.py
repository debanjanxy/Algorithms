import numpy as np
from numpy.linalg import inv

class LinearRegression:
    def __init__(self, n_jobs==-1):
        self.n_jobs = n_jobs

    def fit(self, X, y):
        self.theta = np.matmul(np.matmul(inv(np.matmul(X.T, X)), X.T), y)


    def predict(self, X):
        return np.matmul(X, self.theta)

if __name__ == "__main__":
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_val = lr.predict(X_val)
    evaluate(y_val, y_true)