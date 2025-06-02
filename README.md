# Quadratic Equation Solver
___

This Python CLI application solves quadratic equations of the form:

```
a x^2 + b x + c = 0
```

It supports both interactive and non-interactive (file-based) modes.

## Running the Application
___

### Interactive Mode

Run the application without arguments:

```
python equation.py
```

You will be prompted to enter the coefficients (`a`, `b`, `c`) manually.

### Non-Interactive Mode

Run the application with a file path as an argument:

```
python equation.py <file_path>
```

For example:

```
python equation.py test_files/test_valid.txt

or

python equation.py test_files/test_invalid.txt

or

python equation.py test_files/test_zero.txt
```

## File Format
___

The input file must contain exactly three space-separated real numbers followed by a newline:

```
1 -3 2
```

This represents the equation:

```
(1.0) x^2 + (-3.0) x + (2.0) = 0
```

## Revert commit
___

Revert commit: [`517e14c`](https://github.com/Ederatone/quadratic-equation-solver/commit/05a479ec37e6b1b863944a24f83d6f3d993d292a)