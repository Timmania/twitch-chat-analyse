import sys
from collections import defaultdict


def file_handler(path):
    """
    Opens the file for use inside of the program
    :param path: path to file
    :return: list of messages longer than 120 characters
            and the amount of messages in the entire file
    """
    with open(path, "r") as f:
        text = f.read()

    text = text.split("\n")
    return [item for item in text if len(item) >= 120], len(text)


def unique_counter(text_list):
    """
    counts the unique messages and removes any messages that appear once
    :param text_list: list of messages
    :return: list of tuples as message plus amount of occurrences
    """
    d = defaultdict(int)
    for message in text_list:
        d[message] += 1

    return [item for item in d.items() if item[1] != 1]


def make_matrix(chat1, chat1_count, chat2, chat2_count):
    """
    creates 4 variables containing the amount of copypastas
    and the amount of original messages for each chat
    :param chat1: list of tuples containing messages
        plus the amount of occurrences in chat 1
    :param chat1_count: the total amount of messages of chat 1
    :param chat2: list of tuples containing messages
        plus the amount of occurrences in chat 2
    :param chat2_count: the total amount of messages of chat 2
    :return: amount of copypastas and original messages of both chats
    """
    chat1_cp = 0
    for item in chat1:
        chat1_cp += int(item[1])

    chat2_cp = 0
    for item in chat2:
        chat2_cp += int(item[1])

    chat1_count = chat1_count - chat1_cp
    chat2_count = chat2_count - chat2_cp

    return chat1_cp, chat1_count, chat2_cp, chat2_count


def print_results(results):
    """
    Prints a contingency matrix of the results
    :param results: list of results from both chats
    :return:
    """
    print("{0:^12}|{1:^12}|{2:^12}".format("", "Chat 1", "Chat2"))
    print("{0:^12}+{1:^12}+{2:^12}".format("-"*12, "-"*12, "-"*12))
    print("{0:^12}|{1:^12}|{2:^12}".format("copy pasta", results[0], results[2]))
    print("{0:^12}|{1:^12}|{2:^12}".format("original", results[1], results[3]))


def main(argv):
    _, path1, path2 = argv
    chat1, chat1_count = file_handler(path1)
    chat2, chat2_count = file_handler(path2)

    chat1 = unique_counter(chat1)
    chat2 = unique_counter(chat2)

    print_results(make_matrix(chat1, chat1_count, chat2, chat2_count))


if __name__ == '__main__':
    main(sys.argv)
