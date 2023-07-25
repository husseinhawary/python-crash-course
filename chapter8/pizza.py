def make_pizza(size, *toppings):
    """
    :param size:
    :param toppings:
    :return:
    """
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")