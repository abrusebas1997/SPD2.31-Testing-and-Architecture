# Solutions

## Bug 1: Pizzas aren't being displayed after creation


- `TypeError: 'topping' is an invalid keyword argument for PizzaTopping`
- [FIX] Change append toppings loop to:
    ``` python
    for topping in toppings_list:
        pizza.toppings.append(PizzaTopping(topping_type=topping))
    ```

- [FIX] request.form.get(NAME) to `order_name` and `pizza_size`
    ```python
        order_name = request.form.get('order_name')
        pizza_size_str = request.form.get('pizza_size')
    ```

- [FIX] `request.form.get('toppings)` to `request.form.getlist('toppings')`
    ```python
        toppings_list = request.form.getlist('toppings')
    ```

- [FIX] Commit pizza to db in `pizza_order_submit()`:
    ```python
        db.session.add(pizza)
        # Add commit after add
        db.session.commit()
    ```
