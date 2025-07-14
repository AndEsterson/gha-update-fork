# Tox Environments

A convenient way to use this tool is with a [Tox] environment. Other
environments can be added for updating other pinned tools, such as [pre-commit]
hooks and [pip-tools] for Python requirements files. A label can be used to
create one command that runs all three update environments.

[Tox]: https://tox.wiki
[pre-commit]: https://pre-commit.com
[pip-tools]: https://pip-tools.readthedocs.io

```{code-block} toml
:caption: `pyproject.toml`

[dependency-groups]
gha-update = ["gha-update"]
pre-commit = ["pre-commit", "pre-commit-uv"]

[tool.tox.env.update-actions]
labels = ["update"]
dependency_groups = ["gha-update"]
commands = [["python", "-m", "gha_update"]]

[tool.tox.env.update-pre_commit]
labels = ["update"]
dependency_groups = ["pre-commit"]
skip_install = true
commands = [["pre-commit", "autoupdate", "--freeze", "-j4"]]

[tool.tox.env.update-requirements]
labels = ["update"]
dependency_groups = []
skip_install = true
commands = [["uv", "lock", { replace = "posargs", default = ["-U"], extend = true }]]

```

You can run a single environment to update the corresponding pins:

```
$ tox r -e update-actions
```

Or all the environments labeled `update`:

```
$ tox r -m update
```
