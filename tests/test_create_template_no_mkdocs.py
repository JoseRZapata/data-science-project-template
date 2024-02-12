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

    file_paths = ["pyproject.toml", "Makefile"]
    text_check = ["tool.poetry.group.docs.dependencies", "mkdocs"]

    for file_path, text in zip(file_paths, text_check, strict=False):
        env_path = result.project_path / file_path
        if env_path.is_file():
            with open(env_path) as f:
                file_content = f.read()
                assert text not in file_content
