# PROJECT 2
# PYTHON PROGRAMMING INTERNSHIP - MOTION CUT
# AUTHOR: KARAN DIUNDI


# Function to count the number of words in a given text
def word_counter(text):
    # Strip leading and trailing whitespace from the input and split the text by spaces.
    # This generates a list of words (any sequence of characters separated by spaces).
    words = text.strip().split()
    
    # Return the length of the list, which corresponds to the number of words.
    return len(words)

# Main function that controls the flow of the program
def main():
    # Prompt the user to input a sentence or paragraph. 
    # The input is stripped of leading/trailing spaces immediately to ensure cleaner processing.
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty after stripping spaces.
    # If the input is empty, the program will print an error message and not proceed with counting.
    if not user_input:
        print("Error: The input cannot be empty.")
    else:
        # Call the word_counter function, passing the user's input as an argument.
        # The function returns the word count, which is stored in the 'count' variable.
        count = word_counter(user_input)
        
        # Display the word count result to the user in a user-friendly message.
        print(f"Word count: {count}")

# This ensures that the main function will only be called if this script is executed directly.
# It prevents the code from running automatically when the script is imported as a module in another file.
if __name__ == "__main__":
    main()
