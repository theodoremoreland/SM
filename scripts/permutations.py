import argparse

parser = argparse.ArgumentParser()
parser.description = "Print out all permutations of given text file."
parser.add_argument(
    "--file-path",
    type=str,
    required=True,
    help="The file to read. Required.",
)


def read_file(file_path):
    """
    Read a file and return its contents in str format.

    Parameters
    ----------
    file_path : str
        The path to the file to read.

    Returns
    -------
    str
        The contents of the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_permutations(line):
    """
    Get all permutations of a given string.

    To accomplish this, the function will swap each character with the next
    saving each swap as a new permutation. Eventually, the new permutation
    will be the same as the original string, indicating that all permutations
    have been found.

    Parameters
    ----------
    line : str
        The string to get permutations of.

    Returns
    -------
    list
        An unsorted list of all permutations of the given string.

    """
    permutations = []
    length = len(line)

    if length == 1:
        return [line]

    permutation = list(line)

    while permutations == [] or permutations[-1] != line:
        for i in range(length - 1):
            swap_a = permutation[i]
            swap_b = permutation[i + 1]

            permutation[i] = swap_b
            permutation[i + 1] = swap_a

            permutations.append("".join(permutation))

    return permutations


if __name__ == "__main__":
    args = parser.parse_args()
    p = read_file(args.file_path)

    for line in p.split("\n"):
        permutations = get_permutations(line)
        permutations.sort()

        print(",".join(permutations))
