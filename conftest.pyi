"""
This type stub file was generated by pyright.
"""

import pytest

def pytest_configure(config): # -> None:
    ...

def pytest_runtest_setup(item): # -> None:
    ...

@pytest.fixture(scope="function", autouse=True)
def check_fpu_mode(request): # -> Generator[None, None, None]:
    """
    Check FPU mode was not chan"""
    ...
