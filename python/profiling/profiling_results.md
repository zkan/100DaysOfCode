### Before

Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    30500    0.481    0.000    0.564    0.000 {built-in method builtins.print}
    28500    0.166    0.000    0.295    0.000 csv.py:108(__next__)
    28000    0.223    0.000    0.256    0.000 csv_data_analysis.py:18(parse_row)
    29000    0.086    0.000    0.092    0.000 {built-in method builtins.next}
    30000    0.083    0.000    0.083    0.000 __init__.py:422(__repr__)
     2000    0.030    0.000    0.050    0.000 {built-in method builtins.max}
    56500    0.029    0.000    0.042    0.000 csv.py:94(fieldnames)
      500    0.032    0.000    0.040    0.000 {built-in method io.open}
    28000    0.014    0.000    0.027    0.000 <string>:1(__new__)
     1500    0.005    0.000    0.014    0.000 pathlib.py:615(_parse_args)

### After Storing Only Necessary Data

 Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    30500    0.344    0.000    0.406    0.000 {built-in method builtins.print}
    28500    0.152    0.000    0.269    0.000 csv.py:108(__next__)
    28000    0.106    0.000    0.154    0.000 csv_data_analysis.py:17(parse_row)
    29000    0.078    0.000    0.084    0.000 {built-in method builtins.next}
    30000    0.062    0.000    0.062    0.000 __init__.py:422(__repr__)
     2000    0.030    0.000    0.050    0.000 {built-in method builtins.max}
    56500    0.026    0.000    0.039    0.000 csv.py:94(fieldnames)
      500    0.030    0.000    0.038    0.000 {built-in method io.open}
    28000    0.012    0.000    0.024    0.000 <string>:1(__new__)
   140002    0.023    0.000    0.023    0.000 {method 'get' of 'dict' objects}
