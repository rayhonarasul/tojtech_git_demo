import pytest

from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass
