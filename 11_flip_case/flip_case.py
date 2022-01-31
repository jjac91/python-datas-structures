def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> 
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = ""
    for letter in phrase:
        if letter == to_swap:
            swapped += letter.swapcase()
        elif letter.swapcase() == to_swap:
            swapped += letter.swapcase()
        else: swapped += letter
    return swapped