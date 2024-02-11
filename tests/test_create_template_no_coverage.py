def test_cookiecutter_conf_files(cookies) -> None:  # type: ignore
    """ensures the codecov files not present"""
    codecov = False
    result = cookies.bake(extra_context={"codecov": codecov})

    env_path = result.project_path / ".github/workflows/test.yml"
    assert env_path.is_file()

    with open(env_path) as f:
        file_content = f.read()
        assert "CODECOV_TOKEN" not in file_content

    env_path = result.project_path / "codecov.yml"
    assert not env_path.is_file()
