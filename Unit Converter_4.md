
## Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).


|  | ft  | mi  | m  | km  |
|---|----|----|----|---|
|ft|1||0.3048||
|mi||1|1609.34||
|m|1/0.3048|1/1609.34|1|1/1000|
|km|||1000|1|

But instead of filling out that matrix, and checking for each pair of units (`if from_units == 'mi' and to_units == 'km'`), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units **_to_** meters, then convert **_from_** meters to the output units.


Below is some sample input/output:

```python
def unit_converter():
    - input: "what is the distance?" 100
    - input: "what are the input units?" mi
    - input: "what are the output units?" ft
    - return : "<initial value> <units> is <converted amount> <units>"
```

