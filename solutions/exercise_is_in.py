def is_in(char, instr):
    """
    char: a single character
    instr: an alphabetized string

    returns: True if char is in instr; False otherwise
    """
    if instr == '':
        return False
    if instr[len(instr) // 2] == char:
        return True
    elif len(instr) == 1:
        return False
    elif char < instr[len(instr) // 2]:
        return is_in(char, instr[:len(instr) // 2])
    else:
        return is_in(char, instr[len(instr) // 2:])
