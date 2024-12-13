from model import Prediciton

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediciton:
    if len(inputs) != len(outputs):
        raise Exception('Length of inputs and outputs must match.')

    # create a datafame for our data
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the data using Numpy (x: iputs, y:outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    Y = np.array(df['outputs']).reshape(-1, 1)

    # print(X)
    # print(Y)

    # Split the data into training data to test our model
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, random_state=0, test_size=.20)

    # Initialize the mode and test it
    model = LinearRegression()
    model.fit(train_X, train_Y)

    # Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # Plot
    if plot:
        #raise NotImplementedError('Plot function has not been created yet')
        display_plot(inputs=X, outputs=Y, y_line=y_line)

    return Prediciton(value=y_prediction[0][0],
                      r2_score=r2_score(test_Y, y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_Y, y_test_prediction))


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('inputs')
    plt.ylabel('outputs')
    plt.plot(inputs, y_line, color='r')
    plt.show()


if __name__ == '__main__':
    years: list[int] = [1,2,3,4,5,6,7,8,9,10]
    earnings: list[int] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]
    my_input: int = 20

    prediction: Prediciton = make_prediction(inputs=years, outputs=earnings, input_value=my_input, plot=False)
    print('Input: ', my_input)
    print(prediction)
    print('mean_absolute_error: ', prediction.mean_absolute_error)

    print('Year 30: ', prediction.slope * 30)
    print('Year 40: ', prediction.slope * 40)
    print('Year 50: ', prediction.slope * 50)