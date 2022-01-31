def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lowercase = word.lower() 
    lowerletter = letter.lower()
    answer = 0
    for char in lowercase:
        if char == lowerletter:
            answer +=1
    return answer