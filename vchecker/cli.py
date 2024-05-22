from argparse import ArgumentParser

from rich import print

from .api import VanishChecker


def setup_argparse():
    parser = ArgumentParser(description="IPVanish validity account checker.")
    parser.add_argument(
        "-e",
        "--email",
        required=True,
        type=str,
        help="Email address of IPVanish account.",
    )
    parser.add_argument(
        "-p",
        "--password",
        required=True,
        type=str,
        help="Password of IPVanish account.",
    )
    return parser.parse_args()


def main():
    args = setup_argparse()
    with VanishChecker(args.email, args.password) as checker:
        checker.initiate_auth()
        user_info = checker.get_user_info()
        print(user_info)
