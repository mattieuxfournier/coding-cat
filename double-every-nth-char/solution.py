def double_nth_char(text: str, n: int) -> str:
    result = []
    for i, char in enumerate(text, start=1): 
        if i % n == 0:  
            result.append(char * 2)  
        else:
            result.append(char)
    return ''.join(result)
