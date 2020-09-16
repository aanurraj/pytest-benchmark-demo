from functions.sigmoid import calculate_sigmoid
import pytest


def test_sigmoid_10(benchmark):
    benchmark(calculate_sigmoid, 10)


def test_sigmoid_20(benchmark):
    benchmark(calculate_sigmoid, 100)

def test_sigmoid_1000(benchmark):
    benchmark(calculate_sigmoid, 1000)

