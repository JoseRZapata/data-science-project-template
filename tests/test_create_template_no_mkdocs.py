def test_cookiecutter_mkdocs_files(cookies) -> None:  # type: ignore
    """ensures the mkdocs files not present"""
    mkdocs = False
    result = cookies.bake(extra_context={"mkdocs": mkdocs})

    file_paths = [
        "mkdocs.yml",
        ".github/workflows/docs.yml",
        "docs/index.md",
    ]

    for file_path in file_paths:
        env_path = result.project_path / file_path
        assert not env_path.is_file()

    env_path = result.project_path / "pyproject.toml"
    assert env_path.is_file()

    with open(env_path) as f:
        file_content = f.read()
        assert "tool.poetry.group.docs.dependencies" not in file_content
