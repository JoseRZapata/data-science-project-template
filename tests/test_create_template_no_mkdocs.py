def test_cookiecutter_mkdocs_files(cookies) -> None:  # type: ignore
    """ensures the mkdocs files not present"""
    mkdocs = False
    result = cookies.bake(extra_context={"mkdocs": mkdocs})

    env_path = result.project_path / "mkdocs.yml"
    assert not env_path.is_file()

    env_path = result.project_path / ".github/workflows/docs.yml"
    assert not env_path.is_file()

    env_path = result.project_path / "docs/index.md"
    assert not env_path.is_file()
