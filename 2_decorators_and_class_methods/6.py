from typing import List


class TrainSettings:
    def __init__(self, lr: float, epochs: int):
        self.lr = lr
        self.epochs = epochs


class RNNSettings(TrainSettings):
    def __init__(self, lr: float, epochs: int, cells: int):
        super(RNNSettings, self).__init__(lr, epochs)
        self.cells = cells


class TransformerSettings(TrainSettings):
    def __init__(self, lr: float, epochs: int, attention_heads: int):
        super(TransformerSettings, self).__init__(lr, epochs)
        self.att_heads = attention_heads


class Model:
    def __init__(self, settings: TrainSettings):
        self.lr = settings.lr
        self.epochs = settings.epochs

    @classmethod
    def from_settings(cls, settings: TrainSettings) -> "Model":
        return cls(settings)


class RNN(Model):
    def __init__(self, settings: RNNSettings):
        super(RNN, self).__init__(settings)
        self.cells = settings.cells


class Transformer(Model):
    def __init__(self, settings: TransformerSettings):
        super(Transformer, self).__init__(settings)
        self.cells = settings.att_heads


if __name__ == "__main__":
    settings_list: List[TrainSettings] = [
        RNNSettings(0.001, 100, 200),
        TransformerSettings(0.0001, 20, 6),
        TransformerSettings(0.0001, 20, 120),
    ]
    models: List[Model] = []
    for settings in settings_list:
        if isinstance(settings, RNNSettings):
            models.append(RNN.from_settings(settings))
        else:
            models.append(Transformer.from_settings(settings))

    print(
        "\n".join(
            [
                f"Model: {model.__class__}, attributes: {model.__dict__ }"
                for model in models
            ]
        )
    )
