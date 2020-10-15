from dataclasses import dataclass
from typing import List

# The code can be further improved if we use dataclass for storing parameters
# Dataclasses require type hints by design
# This is really useful in bigger projects


@dataclass
class ModelParams:
    loss_function: str
    learning_rate: float
    optimizer: str
    epochs: int
    units: int
    n_layers: int


def train_model(train_set: List, test_set: List, model_params: ModelParams):
    # params can now be accessed with dots, but are now logically organized
    if model_params.loss_function == "mse":
        print("Using mean squared error")
    # do something ...


params = ModelParams(
    loss_function="mse",
    learning_rate=10e-5,
    optimizer="adam",
    epochs=100,
    units=10,
    n_layers=5,
)

train_model(test_set=[], train_set=[], model_params=params)

# Type hints now work if we try to create incorrect ModelParams object
another_params = params = ModelParams(
    loss_function="mse",
    learning_rate="0.001",
    optimizer="adam",
    epochs=100,
    units=10,
    n_layers=5.5,
)
