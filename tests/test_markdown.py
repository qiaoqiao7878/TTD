from src.markdown_transform import parse_arguments
import pytest


@pytest.fixture
def test_arguments_from_cli(mocker):
    """Test whether arguments from the command line are set up correctly in a HermesApp object."""
    mocker.patch(
        "sys.argv",
        [
            "markdown-transform",
            "link2footnote",
            "source.md",
            "destination.md",
        ],
    )
    app = parse_arguments(mocker.MagicMock())

    assert app.python_file_name == "markdown-transform"
