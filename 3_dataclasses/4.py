from dataclasses import dataclass

# Dataclass decorator creates init from passed list of arguments, but the resulting class can also define methods
# To declare parameters with default values, add them after other parameters without default value
# If more advanced logic is needed when creating dataclass, we can use __post_init__ magic method


@dataclass
class ModelParams:
    units: int
    n_layers: int
    loss_function: str = "mse"
    learning_rate: float = 0.001
    optimizer: str = "adam"
    epochs: int = 50

    def __post_init__(self):
        if self.learning_rate > 0.1:
            raise ValueError(f"Only learning rate values smaller than 0.1 are accepted")
        if self.epochs > 100:
            self.epochs = 100

    def print_model(self):
        print(
            f"Number of layers: {self.n_layers}, each layer consists of {self.units} units.\n"
            f"Training for {self.epochs} epochs using {self.optimizer} optimizer, "
            f"{self.loss_function} loss and learning rate {self.learning_rate}.\n"
        )


if __name__ == "__main__":
    params = ModelParams(units=10, n_layers=5, epochs=10000)
    params.print_model()

    try:
        ModelParams(units=10, n_layers=5, learning_rate=1)
    except ValueError as e:
        print(e)
