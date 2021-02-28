print("Sorting is a very important function, as well as other functions.")
sentence = "The quick brown fox jumps over the lazy dog"
letters = sorted(sentence)
print(letters)
letters.sort(reverse=True)   # Sorted and .sort are the same thing, but depends on the code.
print(letters)
print(len(letters))

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
Sorted_numbers = sorted(numbers)
print(Sorted_numbers)
Sorted_numbers.sort(reverse=True)
print(Sorted_numbers)
print(min(Sorted_numbers))
print(max(Sorted_numbers))
print(len(Sorted_numbers))
# Sorted creates new list then sorts, whereas sort just sorts the list.

another_sentence = sorted("The quick brown fox jumps over the lazy dog",
                          key=str.casefold)
print(another_sentence)
another_sentence.sort(reverse=True)
another_sentence_capitalized = sorted("The quick brown fox jumps over the lazy dog",
                          key=str.capitalize)
print(another_sentence_capitalized)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)