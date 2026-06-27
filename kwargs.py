def print_modal_parameters(**hyperparams):
    print(f"hyperparameters received:{hyperparams}")
    for key,value in hyperparams.items(): type(hyperparams)
    print(f" -  {key}:{value}")
print_modal_parameters(learning_rate=0.01, batch_size=32, dropout=0.7)