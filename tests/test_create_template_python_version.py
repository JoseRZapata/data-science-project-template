def test_cookiecutter_python_version(cookies) -> None:  # type: ignore
    """ensures the mkdocs files not present"""
    python_ver = "3.11"
    result = cookies.bake(extra_context={"compatible_python_versions": python_ver})

    env_path = result.project_path / ".github/actions/python-poetry-env/action.yml"
    assert env_path.is_file()

    with open(env_path) as f:
        file_content = f.read()
        assert python_ver in file_content

    env_path = result.project_path / ".github/workflows/test.yml"
    assert env_path.is_file()

    with open(env_path) as f:
        file_content = f.read()
        assert python_ver in file_content

    env_path = result.project_path / "pyproject.toml"
    assert env_path.is_file()

    with open(env_path) as f:
        file_content = f.read()
        assert python_ver in file_content
