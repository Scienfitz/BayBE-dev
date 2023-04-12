"""Tests for the streamlit demos."""
import glob
import subprocess

import pytest


@pytest.mark.parametrize("script", glob.glob("streamlit/*.py"))
def test_streamlit_scripts(script):
    """All streamlit demos run without errors."""
    result = subprocess.run(["python", script], stderr=subprocess.PIPE, check=False)
    assert result.returncode == 0, f"Error running {script}: {result.stderr.decode()}"
