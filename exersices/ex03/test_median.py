def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if data == []:
        raise ValueError

    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_one_element_list():
    """A test that the median function returns
    the correct value for a one-element list"""
    assert median([7]) == 7


def test_odd_numbers_elements():
    """ the correct median is returned for
    lists with odd numbers of elements"""
    assert median([6, 5, 2, 9, 3]) == 5


def test_even_numbers_elements():
    """ the correct median is returned for
    lists with even numbers of elements"""
    assert median([4, 3, 2, 5]) == 3.5


def test_sorted_elements():
    """ the correct median is returned for
    list with ordered elements"""
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    assert median([1, 2, 3]) == 2


def test_reverse_elements():
    """the correct median is returned for
    list with reversed elements"""
    assert median([5, 4, 3, 2]) == 3.5


def test_unordered_elements():
    """the correct median is returned for
    list with unordered elements"""
    assert median([4, 6, 11, 5, 7]) == 6


def test_empty_list():
    """A test checking that requesting the median of an
    empty list raises a ValueError exception"""
    """
    with pytest.raises(ValueError):
        median([])
    """
    try:
        median([])
    except ValueError:
        pass
    else:
        assert False


def test_original_unchanged():
    """A test that ensures that the median
     function leaves the original data unchanged."""
    data = [1, 3, 4, 6, 8]
    assert median([1, 3, 4, 6, 8]) == median(data)


def tuple_as_well_as_lists():
    """A test that ensures that the median
    function works for tuples as well as lists"""
    assert median((1, 2, 3)) == 2
