def test_cookiecutter_python_version(cookies) -> None:  # type: ignore
    """check correct python version in the generated files."""
    versions = ["3.10", "3.11"]
    file_paths = [
        ".github/actions/python-poetry-env/action.yml",
        ".github/workflows/ci.yml",
        "pyproject.toml",
    ]

    for python_ver in versions:
        result = cookies.bake(extra_context={"compatible_python_versions": python_ver})

        for file_path in file_paths:
            env_path = result.project_path / file_path
            assert env_path.is_file()

            with open(env_path) as f:
                file_content = f.read()
                assert python_ver in file_content
