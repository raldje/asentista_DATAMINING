def countwords(sentences):
    word_count = 0
    
    for char in sentences:
        # Check for spaces to identify word boundaries
        if char == ' ':
            word_count += 1
    
    # Add 1 to count the last word, as it may not end with a space
    return word_count + 1

# User input
user_sentence = input("Enter a sentence: ")

# Call the function and display the result
result = countwords(user_sentence)
print(f"Number of words: {result}")