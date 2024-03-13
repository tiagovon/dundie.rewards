from dundie.utills import get_logger
"""core modulo dundie"""


log = get_logger()

def load(filepath):
    try:
        with open(filepath)as file_:
           return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
x=323