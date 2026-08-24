def normalise(values, minimum=None, maximum=None):
    """
    Scales a list of numbers into the 0-1 range.[cite: 1]
    
    Args:
        values (list of float/int): Numerical values to scale.[cite: 1]
        minimum (float/int, optional): Lower bound. Defaults to min(values).[cite: 1]
        maximum (float/int, optional): Upper bound. Defaults to max(values).[cite: 1]
        
    Returns:
        list of float: Min-max scaled values between 0.0 and 1.0.[cite: 1]
    """
    if not values:
        return []
    
    min_val = min(values) if minimum is None else minimum[cite: 1]
    max_val = max(values) if maximum is None else maximum[cite: 1]
    
    if max_val == min_val:
        return [0.0 for _ in values] # Prevents division by zero when max and min are identical[cite: 1]
        
    return [(x - min_val) / (max_val - min_val) for x in values]

# Test cases[cite: 1]
print("Normalise regular:", normalise([12, 18, 25, 40]))[cite: 1]
print("Normalise identical:", normalise([5, 5, 5, 5]))[cite: 1]


def summarise_scores(scores):
    """
    Calculates summary metrics for a list of evaluation scores.[cite: 1]
    
    Args:
        scores (list of float/int): Numerical performance scores.[cite: 1]
        
    Returns:
        dict: Contains count, mean, min, max, and count of scores >= 0.8. Returns zero values for empty lists.[cite: 1]
    """
    if not scores:
        return {"count": 0, "mean": 0.0, "minimum": None, "maximum": None, "above_threshold": 0}[cite: 1]
        
    return {
        "count": len(scores),
        "mean": sum(scores) / len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
        "above_threshold": sum(1 for s in scores if s >= 0.8)
    }[cite: 1]

# Test cases[cite: 1]
print("Summary 1:", summarise_scores([0.45, 0.82, 0.91, 0.73, 0.88]))[cite: 1]
print("Summary Empty:", summarise_scores([]))[cite: 1]


def safe_divide(numerator, denominator, default=0.0):
    """
    Safely divides two inputs, returning a default value on error.[cite: 1]
    
    Args:
        numerator (int/float/str): Dividend.[cite: 1]
        denominator (int/float/str): Divisor.[cite: 1]
        default (float): Fallback value on ZeroDivisionError or TypeError/ValueError. Defaults to 0.0.[cite: 1]
        
    Returns:
        float: Result of division or default value.[cite: 1]
    """
    try:
        num = float(numerator)
        den = float(denominator)
        return num / den[cite: 1]
    except (ZeroDivisionError, ValueError, TypeError):[cite: 1]
        return default[cite: 1]

# Test cases[cite: 1]
print("Safe divide normal:", safe_divide(10, 2))[cite: 1]
print("Safe divide zero:", safe_divide(10, 0))[cite: 1]
print("Safe divide text:", safe_divide("ten", 2))[cite: 1]