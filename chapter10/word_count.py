def word_counts(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
    except FileExistsError:
        print(f"Sorry, the file {file_name} doesn't exist")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")


file_nam = "programming.txt"
word_counts(file_nam)
