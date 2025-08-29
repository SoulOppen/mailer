def readTxt(path):
    """
    Reads a text file, skips the first line, and returns the remaining 
    lines as a set of unique, non-empty strings.

    Parameters:
    - path (str): The path to the text file.

    Returns:
    - set: A set containing unique lines from the file, excluding the first line.
    """
    with open(path, "r", encoding="utf-8") as f:
        next(f)  # skip the first line
        return set(line.strip() for line in f if line.strip())


def writeTxt(path, lines, head):
    """
    Writes lines to a text file, adding a header as the first line.

    Parameters:
    - path (str): The path to the text file to write.
    - lines (iterable of str): Lines to write into the file.
    - head (str): Header line to write at the top of the file.

    Returns:
    - None
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'{head}\n')
        for line in lines:
            f.write(line + "\n")
