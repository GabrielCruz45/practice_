# NumPy Cheat Sheet

## Array Creation

    np.array(), np.arange(), np.linspace(), np.zeros(), np.ones()
    np. full, np.eye(), np.random.rand(), np.random.randint()

## Array Information

    .shape, .size, .ndim, .dtype, .itemsize, .nbytes

## Array Manipulation

    .reshape(), .flatten(), .T (transpose)
    np.concatenate(), np.vstack(), np.hstack(),
    np.split(), np.array_split()
    np.expand_dims(array, axis) -> crucial for neural net batching

## Mathematical Operations

    +, -, *, /,  **, %, np.sqrt(), np.sin(), np.cos(), np.exp(), np.log()

## Statistical Functions

    np.sum(), np.mean(), np.median(), np.std(), np.var(),
    np.min(), np.max(), np.argmin(), np.argmax(),
    np.percentile(), np.quantile()

## Linear Algebra

    np.dot(), @ matrix multiplication
    np.linalg.det(), np.linalg.inv(), np.linalg.eig()
    np.linalg.solve() (solve linear equations)

## Searching and sorting

    np.where(), np.argwhere()
