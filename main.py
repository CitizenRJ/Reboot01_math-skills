import sys
import statistics
import math


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers rounded to the nearest integer.
        None: If an error occurs during the calculation.
    """
    try:
        average = sum(numbers) / len(numbers)
        return round(average)
    except ZeroDivisionError:
        return "Error: Cannot calculate average of an empty list."
    except Exception as e:
        return f"Error occurred in calculate_average: {str(e)}"


def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The median of the numbers rounded to the nearest integer.
        None: If an error occurs during the calculation.
    """
    try:
        median = statistics.median(numbers)
        return math.ceil(median)
    except statistics.StatisticsError as e:
        return f"Error occurred in calculate_median: {str(e)}"
    except Exception as e:
        return f"Error occurred in calculate_median: {str(e)}"


def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The variance of the numbers rounded to the nearest integer.
        None: If an error occurs during the calculation.
    """
    try:
        variance = statistics.pvariance(numbers)
        return round(variance)
    except statistics.StatisticsError as e:
        return f"Error occurred in calculate_variance: {str(e)}"
    except Exception as e:
        return f"Error occurred in calculate_variance: {str(e)}"


def calculate_std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The standard deviation of the numbers rounded to the nearest integer.
        None: If an error occurs during the calculation.
    """
    try:
        std_dev = statistics.pstdev(numbers)
        return round(std_dev)
    except statistics.StatisticsError as e:
        return f"Error occurred in calculate_std_dev: {str(e)}"
    except Exception as e:
        return f"Error occurred in calculate_std_dev: {str(e)}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid data in the file '{input_file}'.")
        sys.exit(1)

    if not numbers:
        print("Error: The input file is empty.")
        sys.exit(1)

    print("Statistical Measures:")
    print("Average:", calculate_average(numbers))
    print("Median:", calculate_median(numbers))
    print("Variance:", calculate_variance(numbers))
    print("Standard Deviation:", calculate_std_dev(numbers))


if __name__ == '__main__':
    main()
