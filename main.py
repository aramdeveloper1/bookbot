def main():
    # Define the file path
    file_path = "books/frankenstein.txt"
    
    # Open the file and read its contents
    with open(file_path, "r") as f:
        file_contents = f.read()
    
    # Print the entire content of the book
    print(file_contents)

# Run the main function
if __name__ == "__main__":
    main()
