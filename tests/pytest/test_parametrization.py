import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('numbers', [1, 2, 3, -1])
def test_numbers(numbers: int):
    assert numbers > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['macOS', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webKit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webKit', 'firefox'])
def browser(request: SubRequest) -> str:
    return request.param

def test_open_browser(browser: str):
    print(f'running test on browser: {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_opreation(self, user: str, account: str):
        print(f'User with operation: {user}')

    def test_user_without_operation(self, user: str):
        print(f'User without operation: {user}')



users = {
    '70000000011': 'User with money on bank account',
    '70000000022': 'User without money on bank account',
    '70000000033': 'User with operations on bank account'
}

@pytest.mark.parametrize('phone',
                         users.keys(),
                         ids=lambda phone_numbers: f'{phone_numbers}: {users[phone_numbers]}'
                         )
def test_identifiers(phone: str):
    pass