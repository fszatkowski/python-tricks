from typing import Any


# Assume write function for training machine learning model

def train_model(train_set: Any, test_set: Any, loss_function: str, learning_rate: float, optimizer: str, epochs: int,
                units: int, n_layers: int):
    pass


# Then we invoke this function with dummy variables
train, test = None, None
train_model(train, test, "mse", 1e-5, "adam", 10, 100, 5)

# Not really readable unless you know the exact definition of function or the arguments are named really well
# Lets specify parameter names
train_model(train_set=train, test_set=test, loss_function="mse", learning_rate=1e-5, optimizer="adam",
            epochs=10, units=100, n_layers=5)

# A bit better but still hard to understand quickly with a lot of arguments
# Lets use dataclasses to define container class

from dataclasses import dataclass


@dataclass
class ModelParams:
    loss_function: str
    learning_rate: float
    optimizer: str
    epochs: int
    units: int
    n_layers: int


def train_model(train_set: Any, test_set: Any, model_params: ModelParams):
    # Access items with dot, eg: loss = model_params.loss_function
    pass


params = ModelParams(loss_function="mse",
                     learning_rate=10e-5,
                     optimizer="adam",
                     epochs=100,
                     units=10,
                     n_layers=5)

train_model(test_set=test, train_set=train, model_params=params)
