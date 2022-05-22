import pytest
from app import check_document_existance, get_doc_owner_name, add_new_shelf

class TestFunctions:

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    @pytest.mark.parametrize('number, expected_result',
    [
        ("2207 876234", True),
        ("11-2", True),
        ("10006", True),
        ("0981", False),
        ("13893 098", False)

    ])

    def test_check_document_existance(self, number, expected_result):
        actual_result = check_document_existance(number)
        assert actual_result == expected_result
        print(number, expected_result)

    @pytest.mark.parametrize('number, expected_result',
    [
        ("2207 876234", "Василий Гупкин"),
        ("11-2", "Геннадий Покемонов"),
        ("10006", "Аристарх Павлов"),
        ("8979", None),
        ("02 393", None)

    ]
                             )

    def test_get_doc_owner_name(self, number, expected_result):
        actual_result = get_doc_owner_name(number)
        assert actual_result == expected_result
        print(number, expected_result)

    @pytest.mark.parametrize('shelf, expected_result',
    [
        ('4', ('4', True)),
        ('7', ('7', True)),
        ('1', ('1', False))
    ]
                             )

    def test_add_new_shelf(self, shelf, expected_result):
        actual_result = add_new_shelf(shelf)
        assert actual_result == expected_result
        print(shelf, expected_result)



