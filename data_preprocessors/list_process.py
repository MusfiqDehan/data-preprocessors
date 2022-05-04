"""
A module for preprocessing lists.
"""


def delete_duplicates(list):
    """
    Delete duplicates from a list.
    """
    return list(set(list))


def delete_duplicates_from_list_of_lists(list_of_lists):
    """
    Delete duplicates from a list of lists.
    """
    return [list(set(l)) for l in list_of_lists]


def delete_duplicates_from_list_of_lists_of_lists(list_of_lists_of_lists):
    """
    Delete duplicates from a list of lists of lists.
    """
    return [delete_duplicates_from_list_of_lists(l) for l in list_of_lists_of_lists]


def delete_duplicates_from_list_of_lists_of_lists_of_lists(list_of_lists_of_lists_of_lists):
    """
    Delete duplicates from a list of lists of lists of lists.
    """
    return [delete_duplicates_from_list_of_lists_of_lists(l) for l in list_of_lists_of_lists_of_lists]


def delete_list_item(list, item):
    """
    Delete an item from a list.
    """
    return [i for i in list if i != item]


def delete_list_item_from_list_of_lists(list_of_lists, item):
    """
    Delete an item from a list of lists.
    """
    return [delete_list_item(l, item) for l in list_of_lists]


def delete_list_item_based_on_index(list, index):
    """
    Delete an item from a list based on its index.
    """
    return [i for i in list if i != list[index]]


def delete_list_item_based_on_index_from_another_list(item_list, index_list):
    """
    Delete an item from a list based on index from another list.
    """
    for index in sorted(index_list, reverse=True):
        del item_list[index]
