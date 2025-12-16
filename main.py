# Third Party Modules
from colorama import Fore, Style

# Local Modules
from modules import operations as op

if __name__ == '__main__':
    print(Fore.LIGHTCYAN_EX, Style.BRIGHT)
    op.cli()