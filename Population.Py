>>> def prediction():
...     initialNumber = int(input("Enter the initial number of organisms: "))
...
>>> initialNumber = int(input("Enter the initial number of organisms: "))
Enter the initial number of organisms: 10
>>> rateGrowth = float(input("Enter the rate of growth [a real number > 1]: "))
Enter the rate of growth [a real number > 1]: 2
>>> time_to_achieve_rate = int(input("Enter the number of hours to achieve the rate of growth: "))
Enter the number of hours to achieve the rate of growth: 2
>>> total_hours = int(input("Enter the total hours of growth: "))
Enter the total hours of growth: 6
>>> time_periods = total_hours // time_to_achieve_rate
>>> total_population = initial_population * (growth_rate ** time_periods)
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    total_population = initial_population * (growth_rate ** time_periods)
                       ^^^^^^^^^^^^^^^^^^
NameError: name 'initial_population' is not defined
>>> total_population = initialNumber * (growth_rate ** time_periods)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    total_population = initialNumber * (growth_rate ** time_periods)
                                        ^^^^^^^^^^^
NameError: name 'growth_rate' is not defined
>>> total_population = initial_population * (rateGrowth ** time_periods)
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    total_population = initial_population * (rateGrowth ** time_periods)
                       ^^^^^^^^^^^^^^^^^^
NameError: name 'initial_population' is not defined
>>> total_population = initialNumber * (rateGrowth ** time_periods)
>>> print(f"The total population is {total_population}")
The total population is 80.0
>>>
