#!/usr/bin/env python

"""Sample test module."""

import pytest

def test_dependency_import():
    """Sample test method."""
    try:
        import awkat_salet  # pylint: disable=W0612
        assert True
    except ImportError:
        pytest.fail(msg="Importation failed !")
