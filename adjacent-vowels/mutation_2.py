def adjacent_vowels(word: str) -> int:
    '''
    range set from index 1
    '''
    count = 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for index in range(1, len(word) - 1):
        if word[index] in vowels and word[index + 1] in vowels:
            count += 1

    return count