import numpy as np


def bisect_min(array, val):
    """
    Given a sorted array, return the index of an existing element
    that has the closest absolute distance to val.
    """
    array = np.asarray(array)
    index = np.searchsorted(array, val, side='left')

    if index == array.size:
        return array.size - 1
    elif index == 0:
        return 0

    if index == array.size - 1:
        offsetArray = np.array([
            array[index - 1],
            array[index]])
    else:
        offsetArray = np.array([
            array[index - 1],
            array[index],
            array[index + 1]])

    return np.argmin(np.abs(val - offsetArray)) - 1 + index


def getOutputShape(inputShape, kernelShape, padding, stride):
    """
    Given an input shape, kernel shape, padding and stride, return the
    dimensions of the convoled image. Will throw an error if the
    dimensionalities do not match.

    The inputShape can have 2 or 3 dimensions.
    The kernelShape can 3 or 4 dimensions

    """
    assert kernelShape[0] == kernelShape[1]
    filterSize = kernelShape[0]
    outputWidth = (inputShape[1] - filterSize + 2 * padding) / stride + 1
    outputHeight = (inputShape[0] - filterSize + 2 * padding) / stride + 1

    outputWidth = int(outputWidth)
    outputHeight = int(outputHeight)

    if len(inputShape) == 2:
        # In the case where the input shape has an implied depth of 1,
        # the output depth is the depth of the kernel.
        assert len(kernelShape) == 3
        outputDepth = kernelShape[2]
    else:
        # In the case where the input shape has an an explicit depth,
        # the output depth is the number of kernels.
        assert kernelShape[2] == inputShape[2]
        outputDepth = kernelShape[3]

    return (outputHeight, outputWidth, outputDepth)