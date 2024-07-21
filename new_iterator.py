class FlatIterator:
    def __init__(self, list_of_lists):
        self.flat_list = self.flatten_list(list_of_lists)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.flat_list):
            raise StopIteration

        element = self.flat_list[self.current_index]
        self.current_index += 1
        return element

    def flatten_list(self, nested_list):
        flattened_list = []
        for element in nested_list:
            if isinstance(element, list):
                flattened_list.extend(self.flatten_list(element))
            else:
                flattened_list.append(element)
        return flattened_list


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
