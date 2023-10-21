def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ""

    for ltr in phrase:
        if ltr == to_swap:
            ltr = ltr.upper()
            swapped_phrase += ltr
        elif ltr == to_swap.upper():
            ltr = ltr.lower()
            swapped_phrase += ltr

        swapped_phrase += ltr

    return swapped_phrase
       
