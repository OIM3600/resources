def assembler(program):
    """
    Assemble and execute a simple program represented as a list of instructions.

    Parameters:
        program (list): A list of strings representing the program instructions.

    Returns:
        dict: The final values of all the registers after executing all the instructions in the program.
    """
    # TODO


# DO NOT CHANGE CODE BELOW!!!
def main():
    """TESTING CODE"""
    program = ["mov a 5", "inc a", "dec a", "mov b a", "dec a", "inc b"]
    result = assembler(program)
    print(result)  # {'a': 4, 'b': 6}


if __name__ == '__main__':
    main()
