"""
An example training an SGDClassifier, performing grid search
using TuneGridSearchCV.

This example uses early stopping to further improve runtimes
by eliminating worse hyperparameter choices early based off
of its average test score from cross validation.
"""

from tune_sklearn import TuneGridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

x, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

clf = LogisticRegression()
parameter_grid = {"C": [1e-4, 1e-1, 1, 2]}

tune_search = TuneGridSearchCV(
    clf,
    parameter_grid,
    early_stopping="MedianStoppingRule",
    max_iters=10,
)
tune_search.fit(x_train, y_train)

pred = tune_search.predict(x_test)
accuracy = np.count_nonzero(np.array(pred) == np.array(y_test)) / len(pred)
print(accuracy)
