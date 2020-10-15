# Let's assume we want to write function for training machine learning model


def train_model(
    train_set,
    test_set,
    loss_function,
    learning_rate,
    optimizer,
    epochs,
    units,
    n_layers,
):
    # do something ...
    pass


# Then we invoke this function with some arguments
train_model([], [], "mse", 1e-5, "adam", 10, 100, 5)

# There are some problems with with readability:
# - the invocation is hard to follow (eg which argument is supposed to be which parameter)
# - we don't have an info about what exactly is expected for each parameter
# And also with function design:
# - too many parameters in the function (3-4 is the upper bound for readability)
# - either function does too much or it can be rewritten to use objects
