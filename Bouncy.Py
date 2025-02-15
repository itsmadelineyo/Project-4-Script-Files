>>> def calculate_total_distance():
...     initial_height = float(input("Enter the height from which the ball is dropped: "))
...     10
...     bounciness_index = float(input("Enter the bounciness index of the ball: "))
...     .6
...      num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
...      2
...       total_distance = initial_height
...
  File "<python-input-0>", line 6
    num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
IndentationError: unexpected indent
>>> for _ in range(num_bounces):
...     initial_height *= bounciness_index
...     total_distance += 2 * initial_height
...
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    for _ in range(num_bounces):
                   ^^^^^^^^^^^
NameError: name 'num_bounces' is not defined
>>> print("Total distance traveled is: ", total_distance, "units.")
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    print("Total distance traveled is: ", total_distance, "units.")
                                          ^^^^^^^^^^^^^^
NameError: name 'total_distance' is not defined
>>>
