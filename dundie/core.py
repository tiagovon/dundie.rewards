"""core modulo dundie"""


def load(filepath):
    try:
        with open(filepath)as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"file not found {e}")