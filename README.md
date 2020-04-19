# miss futility
Before you commit, every commit

## What the heck is this repo about?

This repo is a demo of the pre-commit project, which provides an interface for configuring git hooks.

The repo name is a play on Miss Utility, a service in the mid-atlantic region for assistance with excavation.
The Miss Utility slogan is "Before you dig, every dig."

### Miss Utility links

- https://www.missutility.net
- https://va811.com/

## What are pre-commit hooks?

Pre-commit hooks are scripts that run as part of the "git commit" process, allowing for automated static code analysis or changes to the code.
Pre-commit hooks are probably the most popular hooks, but git also provides `post-commit`, `pre-rebase`, `post-merge`, `pre-push`, and many more.

https://git-scm.com/docs/githooks

## What is the pre-commit tool?

Pre-commit is also a tool written in python that provides a convenient way to configure pre-commit hooks. This is a general-use tool
and is not specific to python. The community supports many hooks for other languages like Go, Ruby, Javascript, and Java.

https://pre-commit.com/

List of community hooks: https://pre-commit.com/hooks.html

## What is the purpose of this repo?

This repo has several code/syntax formatting mistakes that should be caught by static code analysis tools.
It also has a .pre-commit-config.yaml that defines several pre-commit hooks that will fix these issues.

To fix the formatting in this repo:

```
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
