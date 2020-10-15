from typing import List

# Lets first address readability issues by using type hints


def train_model(
    train_set: List,
    test_set: List,
    loss_function: str,
    learning_rate: float,
    optimizer: str,
    epochs: int,
    units: int,
    n_layers: int,
):
    # do something
    pass


# Then let's use parameter names when invoking the function
train_model(
    train_set=[],
    test_set=[],
    loss_function="mse",
    learning_rate=1e-5,
    optimizer="adam",
    epochs=10,
    units=100,
    n_layers=5,
)

# Notice that after we added type hints IDE warns against incorrect arguments
train_model(
    train_set=set(),
    test_set=set(),
    loss_function="mse",
    learning_rate=1e-5,
    optimizer="adam",
    epochs=10,
    units=100,
    n_layers=5,
)
