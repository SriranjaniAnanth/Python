# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance,
# standard deviation, max, min,and sum of the rows, columns, and elements in a 3 x 3 matrix.

# The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3
# Numpy array,and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along
# both axes and for the flattened matrix.

# The returned dictionary
# If a list containing less than 9 elements is passed into the function,
# it should raise a ValueError exception with the message:
# "List must contain nine numbers."
# The values in the returned dictionary should be lists and not Numpy arrays.

# For example, calculate([0,1,2,3,4,5,6,7,8]) should return: { 'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
# 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
# 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726,
# 0.816496580927726, 0.816496580927726], 2.581988897471611], 'max': [[6, 7, 8], [2, 5, 8], 8], 'min': [[0, 1, 2], [0,
# 3, 6], 0], 'sum': [[9, 12, 15], [3, 12, 21], 36] }
import numpy as np
def calculate(ar3):
    # Calculate statistics
    mean_axis1 = list(np.mean(ar3, axis=0))
    mean_axis2 = list(np.mean(ar3, axis=1))
    mean_flattened = np.mean(ar3)

    var_axis1 = list(np.var(ar3, axis=0))
    var_axis2 = list(np.var(ar3, axis=1))
    var_flattened = np.var(ar3)

    std_axis1 = list(np.std(ar3, axis=0))
    std_axis2 = list(np.std(ar3, axis=1))
    std_flattened = np.std(ar3)

    max_axis1 = list(np.max(ar3, axis=0))
    max_axis2 = list(np.max(ar3, axis=1))
    max_flattened = np.max(ar3)

    min_axis1 = list(np.min(ar3, axis=0))
    min_axis2 = list(np.min(ar3, axis=1))
    min_flattened = np.min(ar3)

    sum_axis1 = list(np.sum(ar3, axis=0))
    sum_axis2 = list(np.sum(ar3, axis=1))
    sum_flattened = np.sum(ar3)

    # Create and return the dictionary
    result_dict = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }
    return result_dict


def lst_to_arr(lst):
    try:
        arr = np.array(lst)
        ar3=arr.reshape(3, 3)
        print("The basic statistical Calculations are:\n", calculate(ar3))
    except ValueError:
        print("List must contain nine numbers")


lst = list(map(int, input("Enter 9 elements for basic statistical calculations:").strip().split()))[:9]
lst_to_arr(lst)


