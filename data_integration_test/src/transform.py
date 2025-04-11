def applytransformations(df):
    """
    Apply transformations to the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    # Example transformation: Convert all string columns to uppercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.upper()
    
    return df