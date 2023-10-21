def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aiueoAIUEO'
    list_s = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if list_s[i] not in vowels:
            i += 1

        elif list_s[j] not in vowels:
            j -= 1

        else:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i += 1
            j -=1

    return "".join(list_s)

    