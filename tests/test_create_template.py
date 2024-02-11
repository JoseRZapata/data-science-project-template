import os
import re
import subprocess  # nosec


def build_files_list(root_dir):  # type: ignore
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]


def test_run_cookiecutter_result(cookies):  # type: ignore
    """Runs cookiecutter and checks a couple of things"""
    project_name = "data science project template"
    repo_name = "data-science-project-template"
    result = cookies.bake(
        extra_context={"project_name": project_name, "repo_name": repo_name}
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == repo_name
    assert result.project_path.is_dir()

    readme_path = result.project_path / "README.md"
    assert readme_path.is_file()

    with open(readme_path) as f:
        readme = f.read()
        assert project_name in readme
        assert "project_name" not in readme


def test_cookiecutter_generated_files(cookies):  # type: ignore
    """tests the generated files names make sense"""
    re_bad = re.compile(r"{{\s?cookiecutter\..*?}}")
    result = cookies.bake()

    assert all(
        re_bad.search(str(file_path)) is None
        for file_path in result.project_path.glob("*")
    )


def test_cookiecutter_make_help(cookies):  # type: ignore
    """ensure the make help command runs without error"""
    result = cookies.bake()

    make_proc = subprocess.Popen(
        ["/usr/bin/make"],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=result.project_path,
    )  # nosec
    # stdout, stderr are for debuggin
    stdout, stderr = make_proc.communicate()
    assert make_proc.returncode == 0
