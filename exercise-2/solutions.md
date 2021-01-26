# Solutions

## Bug 1: Missing API key
## Bug 2: OpenWeather API city query string
        'q': city,
## Bug 3: Incorrect request.args.get(NAME) 
```python
    city = request.args.get('city')
    units = request.args.get('units')
```
## Bug 4: Incorrect JSON key
```python
'temp': result_json['main']['temp'],
```
