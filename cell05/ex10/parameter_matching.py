import sys

if len(sys.argv) != 2:
    print("None")
else:

    expected_word = sys.argv[1]

    user_word = input("Enter a word: ")
    
    if user_word == expected_word:
        print("Good job!")
    else:
        print("Nope, sorry...")