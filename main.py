print("WELCOME...")
print("This is a word count project.")

# Take user input
data = input("Enter a sentence or paragraph: ").strip()

# Function to count words
def counter(data):
    words = data.split()
    return len(words)

# Error handling for empty input
if data == "":
    print("Error: No input provided. Please enter a valid sentence or paragraph.")
else:
    word_count = counter(data)
    print(f"The words are: {data.split()}")
    print(f"The word count is: {word_count}")
