# random-markdown-generator

[![Build Status](https://travis-ci.com/IgnisDa/python-random-markdown-generator.svg?branch=master)](https://travis-ci.com/IgnisDa/python-random-markdown-generator)

[![Coverage Status](https://coveralls.io/repos/github/IgnisDa/python-random-markdown-generator/badge.svg?branch=master)](https://coveralls.io/github/IgnisDa/python-random-markdown-generator?branch=master)

A library to generate random markdown text.

## But why?

I was making a blog web-app that lets its users write blog posts using markdown
syntax. I couldn't find any python package that does this easily. Using the
[`faker`](https://github.com/joke2k/faker) library, I created this package to
make a highly configurable markdown post generator. Additionally, it also
provides an API for creating markdown files using python.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Installing

You must have `python` and `pip` installed on your system, and in you `PATH`.
An activated virtual environment is also recommended.

Using `pip`:

```bash
pip install mdgen
```

Or using poetry:

```bash
poetry add mdgen
```

## Sample usage

```python
from faker import Faker
from mdgen import MarkdownPostProvider
fake = Faker()
fake.add_provider(MarkdownPostProvider)
fake_post = fake.post(size='medium') # available sizes: 'small', 'medium', 'large'
print(fake_post)
```

The output from the above command:

```txt
Drop question writer.

> After step respond support argue issue western movie.
[First memory suffer yard.](https://www.simmons.com/)

        1. Possible career speak another believe realize analysis.
|First fear enter surface hospital nothing raise condition.|Name quickly deep free before if.|Rather church provide walk power thank student.|
|----------------------------------------------------------|---------------------------------|-----------------------------------------------|
|Box seem hotel picture popular politics century.|Side simple daughter central suggest.|Campaign nation Republican economy perform require.|
```

## Documentation

The documentation for this project can be found at https://ignisda.github.io/python-random-markdown-generator/.

## Running the tests

The project uses `pytest` to automate its test suite. To install all
dependencies, ensure you have [`poetry`][1] installed on your system and then run:

```bash
poetry install
```

This will install all dependencies for testing this project in a virtual
environment. Then run all tests using:

```bash
poetry shell
pytest
```

To see test coverage, run:

```bash
pytest --cov --cov-report=html --cache-clear
```

Then open `htmlcov/index.html` in your browser to see the test coverage.

### Coding style

This project follows the [pep8](https://pep8.org/) specifications. The maximum
line length has been increased to 90 characters. For the flake8 configuration
used, see [tox.ini](tox.ini). The test suite automatically runs the linters by
default, but you can run just the linting tests.

```bash
flake8
```

## Built With

- [Poetry][1] - Dependency Management
- [Sphinx](https://www.sphinx-doc.org/en/master/index.html) - Used to generate this project's
  documentation.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of
conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Author

- [IgnisDa](https://github.com/IgnisDa/) (**Diptesh Choudhuri**) - _Initial
  work_

See also the list of [contributors](contributors.md) who participated in this project. If you
have made any contribution to this project, please add it in
[contributors.md](contributors.md).

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE.md](LICENSE.md)
file for details.

## Acknowledgments

- Hat tip to anyone whose code was used

[1]: https://github.com/python-poetry/poetry
