from functools import wraps
import time

def monitor_prediction_time():
    """
    Decorator to monitor the time taken for predictions.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Prediction time: {end_time - start_time:.2f} seconds")
            return result
        return wrapper
    return decorator


# import time

# def monitor_prediction_time():
#     """
#     A decorator to monitor and log the time taken by a function to execute.
#     """
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()  # Record the start time
#             result = func(*args, **kwargs)  # Execute the decorated function
#             end_time = time.time()  # Record the end time
#             print(f"Execution time for {func._name_}: {end_time - start_time:.2f} seconds")
#             return result
#         return wrapper
#     return decorator