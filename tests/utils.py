def str_to_bool(val):
    """
    Convert a string representation of truth to True or False
    True values are 'y', 'yes', '1', or ''; case-insensitive
    False values are 'n', 'no', or '0'; case-insensitive
    Raises ValueError if 'val' is anything else.
    """
    true_vals = ['yes', 'y', '1', '']
    false_vals = ['no', 'n', '0']
    
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
        
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("Invalid input value: %s" % val)
