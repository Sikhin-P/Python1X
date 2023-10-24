#  Count vowels and consonants in a String

def count(my_string):
    vow = ['a', 'e', 'i', 'o', 'u']
    vow_count = 0
    cons_count = 0
    for string in my_string:
        if string in vow:
            vow_count += 1
        else:
            cons_count += 1

    return vow_count, cons_count


vow, cons = count('The quick brown fox jumps over the lazy dog')
print(f'Number of vowels: {vow}, and number of consonants : {cons}')
