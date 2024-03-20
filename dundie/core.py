from dundie.utills import get_logger

"""core modulo dundie"""


log = get_logger()
X = 1


def load(filepath):
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
