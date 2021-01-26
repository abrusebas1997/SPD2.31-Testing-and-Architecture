# Solutions

## Bug 1: Pizzas aren't being displayed after creation

- `TypeError: 'topping' is an invalid keyword argument for PizzaTopping`
- 
    ``` python
    for topping_str in ToppingType:
        pizza.toppings.append(PizzaTopping(topping=topping_str)) 
    ```

- parameter mis-labeled for `request.form.get`
```
    order_name = request.form.get('order_name')
    pizza_size_str = request.form.get('pizza_size')
```

- Add `db.session.commit()` after add pizza in `pizza_order_submit`
