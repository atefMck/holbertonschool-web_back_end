#!/usr/bin/env python3
""" azrfezaazdzad """


from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ azrfezaazdzad """
    if lst:
        return lst[0]
    else:
        return None