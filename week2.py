def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Count the number of words
    return len(words)

def main():
    # User input
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: Please enter a sentence or paragraph.")
        return
    
    # Calculate word count
    count = word_count(user_input)
    
    # Output display
    print("Word count:", count)

if __name__ == "__main__":
    main()
