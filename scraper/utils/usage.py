"""usage.

Helper method that is displayed in screen when the flag '-h' or '--help' is
requested.

"""
import sys


def usage(exit_code: int = 0):
    """Usage.

    Shows a message with the available prompt options.

    Parameters
    ----------
    exit_code: int
        System exit code.

    """
    print(
        "\n".join(
            [
                "\nDESCRIPTION\n",
                (
                    "This script pretends to mine Facebook Messenger "
                    "conversations from a page or a user profile using "
                    "Facebook's Graph API, if there isn't a database "
                    "especified in the command line arguments the script will "
                    "store all the data in ./data folder, for more "
                    "information there's a README.md file in the scraper's "
                    "root folder.\n"
                ),
                "\t-t, --timeout=<int>",
                (
                    "\t\tIn case that your Graph API app has reach its request"
                    " limit, define a timeout to continue the download,"
                    " default is 5 minutes."
                ),
                "\t-d, --database=<bool>",
                (
                    "\t\tStore the retrieved information in a Mongo Database. "
                    "If there's a db available, value should be 1 otherwise 0."
                    " The default value is False."
                ),
                "\t-q, --quantity=<int>",
                "\t\tQuantity of conversations to download, default is all.",
                "\t-h, --help",
                "\t\tHelp - Show this message.\n",
            ]
        )
    )
    sys.exit(exit_code)
