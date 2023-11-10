import pandas

# TODO 1. Create a dictionary in this format: {'A':'Alpha','B':'Bravo'...}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from word that the user inputs.
def nato_name(word):
    my_name = [c.upper() for c in word]
    result = [nato_dict[char] for char in my_name if char in nato_dict]
    return result


name = input("Enter a word: ")
print(nato_name(name))
