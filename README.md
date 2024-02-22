# Progress Bar in Python

A simple progress bar library for Python that can be used in both terminal and Jupyter Notebook environments.

## Usage

Import the `progress_bar` function from the `progress_bar` module and use it in your Python program.

```python
from progress_bar import progress_bar

data = range(100)
for _ in progress_bar(data, title='Processing'):
    # Your processing logic here
    time.sleep(0.1)  # Simulating some processing time
```

## Parameters

The `progress_bar` function accepts the following parameters:

- `iterable`: An iterable object to loop over.
- `total`: The total number of iterations (optional).
- `length`: The length of the progress bar (default is 40).
- `title`: The string to be displayed before the ratio (default is 'Progress').
