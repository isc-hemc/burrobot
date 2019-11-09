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
                    "This script pretends to consume the raw data stored in a "
                    "NoSQL server, pre-process that data\nand analyse it for "
                    "generate statistics about the information retrieved.\n"
                ),
                "\t-p, --preprocess=<int>",
                (
                    "\t\tPre-process the information stored in the MongoDB "
                    "server. Default value is 0 (False),\n\t\tif want to "
                    "perform the action the value must be 1 (True)."
                ),
                "\t-t, --topics=<int>",
                (
                    "\t\tIf the SQL database has been populated with "
                    "different types of pre-processed\n\t\tdata this value "
                    "should be 1 (default), otherwise 0."
                ),
                "\t-c, --collection=<int>",
                ("\t\tMongoDB collection to retrieve the data."),
                "\t-g, --graph=<int>",
                (
                    "\t\tPlot the most common topics retrieved from the LDA."
                    "analysis."
                ),
                "\t-h, --help",
                "\t\tHelp - Show this message.\n",
                "\t--topic_column=<str>",
                (
                    "\t\tMySQL database column to analyse, the available "
                    "options are: raw_msg, with_stopwords_no_lemmas_msg,\n\t\t"
                    "with_stopwords_with_lemmas_msg, "
                    "no_stopwords_no_lemmas_msg, no_stopwords_with_lemmas_msg."
                ),
                "\t--num_topics=<int>",
                "\t\tNumber of topics to retrieve from the LDA analysis.",
                "\t--load_topics=<int>",
                (
                    "\t\tLoad topics from a file named `topics.txt` in the "
                    "resources directory. If exists this label should\n\t\tbe 1, "
                    "otherwise 0."
                ),
            ]
        )
    )
    sys.exit(exit_code)
