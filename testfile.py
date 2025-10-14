def display_first_n_lines():
    """
    Prompts the user for a filename and the number of lines to display,
    then prints the first n lines of the file.
    """
    try:
        file_name = input("Enter the filename: ")
        n_str = input("Enter the number of lines to display: ")
        
        # Convert the input to an integer
        n = int(n_str)
        
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Iterate through the file line by line
            for i in range(n):
                line = file.readline()
                # If the line is empty, we've reached the end of the file
                if not line:
                    break
                # Print the line
                print(line.strip())
                
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except ValueError:
        print("Error: Please enter a valid number for the lines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
display_first_n_lines()