def write_to_text(data, output_file):
    """
    Writes the given data to a text file.
    
    Args:
        data (dict or list): The data to be written to the file.
        output_file (str): The path to the output text file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        if isinstance(data, dict):
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        elif isinstance(data, list):
            for item in data:
                f.write(f"{item}\n")
        else:
            raise TypeError("Data must be a dictionary or a list.")
