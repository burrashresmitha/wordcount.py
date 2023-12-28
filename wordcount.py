def word_counter(text):
    words = text.split()
    return len(words)

def main():
    try:
        user_input = input("Enter a sentence or paragraph: ")
        if not user_input:
            raise ValueError("Input is empty. Please enter some text.")

        count = word_counter(user_input)
        print(f"Word count: {count}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
