import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split


class Bayes:
    def __init__(self):
        self.class_prior = []
        self.class_count = []
        self.theta = []
        self.atributes_prob = []
        self.predict_likelihoods_ = []
        self.predict_proba_ = []

    def fit(self, X, y,przelacznik):
        if(przelacznik):
            x1 = np.sum(y == 1)
            x2 = np.sum(y == 2)
            x3 = np.sum(y == 3)

            self.class_count.append(x1)
            self.class_count.append(x2)
            self.class_count.append(x3)

            self.class_prior.append(x1 / len(y))
            self.class_prior.append(x2 / len(y))
            self.class_prior.append(x3 / len(y))

            for i in range(X.shape[1]):
                y1 = [0, 0, 0, 0]
                y2 = [0, 0, 0, 0]
                y3 = [0, 0, 0, 0]
                for j in range(X.shape[0]):
                    if (y[j] == 1): y1[int(X[j][i])] = y1[int(X[j][i])] + 1
                    if (y[j] == 2): y2[int(X[j][i])] = y2[int(X[j][i])] + 1
                    if (y[j] == 3): y3[int(X[j][i])] = y3[int(X[j][i])] + 1

                self.theta.append((y1, y2, y3))

            for a in range(X.shape[1]):
                p_x_Y_y = []
                for i in range(len(self.class_count)):
                    p_x = []
                    for j in range(4):
                        p_x.append((self.theta[a][i][j] + 1) / (self.class_count[i] + len(self.class_count)))
                    p_x_Y_y.append(p_x)
                self.atributes_prob.append(p_x_Y_y)
        else:
            x1 = np.sum(y == 1)
            x2 = np.sum(y == 2)
            x3 = np.sum(y == 3)

            self.class_count.append(x1)
            self.class_count.append(x2)
            self.class_count.append(x3)

            self.class_prior.append(x1 / len(y))
            self.class_prior.append(x2 / len(y))
            self.class_prior.append(x3 / len(y))

            for i in range(X.shape[1]):
                y1 = [0, 0, 0, 0]
                y2 = [0, 0, 0, 0]
                y3 = [0, 0, 0, 0]
                for j in range(X.shape[0]):
                    if (y[j] == 1): y1[int(X[j][i])] = y1[int(X[j][i])] + 1
                    if (y[j] == 2): y2[int(X[j][i])] = y2[int(X[j][i])] + 1
                    if (y[j] == 3): y3[int(X[j][i])] = y3[int(X[j][i])] + 1

                self.theta.append((y1, y2, y3))

            for a in range(X.shape[1]):
                p_x_Y_y = []
                for i in range(len(self.class_count)):
                    p_x = []
                    for j in range(4):
                        p_x.append((self.theta[a][i][j]) / (self.class_count[i]))
                    p_x_Y_y.append(p_x)
                self.atributes_prob.append(p_x_Y_y)


    def predict_proba(self, X):


        for i in range(len(X)):
            prob1 = 1
            prob2 = 1
            prob3 = 1
            for j in range(len(X[0])):
                prob1 *= self.atributes_prob[j][0][int(X[i][j])]
                prob2 *= self.atributes_prob[j][1][int(X[i][j])]
                prob3 *= self.atributes_prob[j][2][int(X[i][j])]
            self.predict_likelihoods_.append([prob1, prob2, prob3])


        for i in range(len(self.predict_likelihoods_)):
            for k in range(len(self.class_prior)):
                self.predict_likelihoods_[i][k] = self.predict_likelihoods_[i][k] * self.class_prior[k]

        for i in range(len(self.predict_likelihoods_)):
            likelihoods_sum = np.sum(self.predict_likelihoods_[i])
            prob1 = self.predict_likelihoods_[i][0] / likelihoods_sum
            prob2 = self.predict_likelihoods_[i][1] / likelihoods_sum
            prob3 = self.predict_likelihoods_[i][2] / likelihoods_sum
            self.predict_proba_.append([prob1,prob2,prob3])

        return self.predict_proba_

    def predict(self, X):
        predicted_proba=self.predict_proba_
        y_predicted=[]
        for i in range(len(X)):
            y_predicted.append(np.argmax(predicted_proba[i])+1)

        return y_predicted



data = np.genfromtxt('wine.data', delimiter=',')
print("The wine dataset size: rows x columns", data.shape)
print(data)

X = data[:, 1:]
y = data[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y)
print("The wine training size: rows x columns", X_train.shape)
print("The wine testing size: rows x columns", X_test.shape)

discretizer = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform', subsample=None)
X_train_discrete = discretizer.fit_transform(X_train)
X_test_discrete = discretizer.fit_transform(X_test)
print("First training sample after discratization", X_train_discrete[0])
print("First testing sample after discratization", X_test_discrete[0])

bayes = Bayes()

#przy ustawieniu przelacznika na true stosowana jest poprawka laplace'a
bayes.fit(X_train_discrete, y_train,przelacznik=True)

print("Predicted probabilities:")
print(bayes.predict_proba(X_test_discrete))

y_predicted=bayes.predict(X_test_discrete)

print("CategoricalNB accuracy:", np.sum(y_predicted == y_test) / len(y_test))

"""
Srednia dokladnosc wynosila 95%
"""