def bubble_sort(data):
    data = list(data)
    length = len(data)
    while length >= 1:
        loop(data)
        length -= 1
    return data


def loop(data):
    for k in range(len(data) - 1):
        if data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]
    return data


def test_empty():
    assert bubble_sort([]) == [], "List should be empty"


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([8]) == [8], "List should contain one number"


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    original = [1, 2, 3]
    result = bubble_sort(original)
    assert original is not result


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort(range(4)) == list(range(4))


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([3, 3, 3]) == [3, 3, 3]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort([4, 1, 6, 3]) == [1, 3, 4, 6]
    assert bubble_sort(["f", "c", "a"]) == ["a", "c", "f"]
