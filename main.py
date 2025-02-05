def main():
    file_path = "books/frankenstein.txt"
    
    # Read the file content
    with open(file_path, "r") as f:
        file_contents = f.read()
    
    # Count words in the file
    word_count = count_words(file_contents)
    
    # Print the total word count
    print(f"The book contains {word_count} words.")
    print(f"The book contains {count_characters(file_contents)} characters.")
    print(f"The book contains {sort_characters(characters)} characters.")
def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()  # Split text into words using whitespace
    return len(words)

characters = {}
def count_characters(text):
    """Returns the number of characters in the given text."""
    
    for char in text:
        # print("****",char)
        
        if char in characters:
            characters[char] += 1
            
        else:
            characters[char] = 1
    print("characters count",characters)
    return len(characters)
def sort_characters(characters):
    """Returns the sorted characters in the given text."""
    sorted_chars = sorted(characters.keys())
    return sorted_chars


# Run the main function
if __name__ == "__main__":
    main()
