def assembler(program):
    """
    Assemble and execute a simple program represented as a list of instructions.

    Parameters:
        program (list): A list of strings representing the program instructions.

    Returns:
        int: The final value of the register after executing all the instructions in the program.
    """
    # TODO


# DO NOT CHANGE CODE BELOW!!!
def main():
    """TESTING CODE"""
    program = ['dec 8', 'inc 7', 'inc 6', 'dec 3', 'inc 8', 'dec 2']
    result = assembler(program)
    print(result)  # 8


if __name__ == '__main__':
    main()
