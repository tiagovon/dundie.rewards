import argparse
from dundie.core import load


def main():
    parser = argparse.ArgumentParser(
    description="Dunder Mifflin Rewards CLI",
    epilog="Enjoy and use with cautious"
)
    
    parser.add_argument(
        "subcommad",
        type=str,
        help="The subcommad to run",
        choices=("load","show","send"),
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path load",
    )

    arg = parser.parse_args()
    globals()[arg.subcommad](arg.filepath)