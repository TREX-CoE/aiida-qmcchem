[![Build Status](https://github.com/TREX-CoE/aiida-qmcchem/workflows/ci/badge.svg?branch=master)](https://github.com/q-posev/aiida-qmcchem/actions)
[![Coverage Status](https://coveralls.io/repos/github/TREX-CoE/aiida-qmcchem/badge.svg?branch=master)](https://coveralls.io/github/q-posev/aiida-qmcchem?branch=master)
[![Docs status](https://readthedocs.org/projects/aiida-qmcchem/badge)](http://aiida-qmcchem.readthedocs.io/)
[![PyPI version](https://badge.fury.io/py/aiida-qmcchem.svg)](https://badge.fury.io/py/aiida-qmcchem)

# aiida-qmcchem

AiiDA plugin for QMC=Chem

This plugin is the modified output of the
[AiiDA plugin cutter](https://github.com/aiidateam/aiida-plugin-cutter),
intended to help developers get started with their AiiDA plugins.

## Repository contents

* [`.github/`](.github/): [Github Actions](https://github.com/features/actions) configuration
  * [`ci.yml`](.github/workflows/ci.yml): runs tests, checks test coverage and builds documentation at every new commit
  * [`publish-on-pypi.yml`](.github/workflows/publish-on-pypi.yml): automatically deploy git tags to PyPI - just generate a [PyPI API token](https://pypi.org/help/#apitoken) for your PyPI account and add it to the `pypi_token` secret of your github repository
* [`qmcchem/`](qmcchem/): The main source code of the plugin package
  * [`data/`](qmcchem/data/): A new `QmcchemParameters` data class, used as input to the `QmcchemCalculation` `CalcJob` class
  * [`calculations.py`](qmcchem/calculations.py): A new `QmcchemCalculation` `CalcJob` class
  * [`cli.py`](qmcchem/cli.py): Extensions of the `verdi data` command line interface for the `QmcchemParameters` class
  * [`parsers.py`](qmcchem/parsers.py): A new `Parser` for the `QmcchemCalculation`
* [`docs/`](docs/): A documentation template ready for publication on [Read the Docs](http://aiida-qmcchem.readthedocs.io/en/latest/)
* [`examples/`](examples/): Examples of how to submit a calculation using this plugin
* [`tests/`](tests/): Basic regression tests using the [pytest](https://docs.pytest.org/en/latest/) framework (submitting a calculation, ...). Install `pip install -e .[testing]` and run `pytest`.
* [`.coveragerc`](.coveragerc): Configuration of [coverage.py](https://coverage.readthedocs.io/en/latest) tool reporting which lines of your plugin are covered by tests
* [`.gitignore`](.gitignore): Telling git which files to ignore
* [`.pre-commit-config.yaml`](.pre-commit-config.yaml): Configuration of [pre-commit hooks](https://pre-commit.com/) that sanitize coding style and check for syntax errors. Enable via `pip install -e .[pre-commit] && pre-commit install`
* [`.readthedocs.yml`](.readthedocs.yml): Configuration of documentation build for [Read the Docs](https://readthedocs.org/)
* [`LICENSE`](LICENSE): License for your plugin
* [`MANIFEST.in`](MANIFEST.in): Configure non-Python files to be included for publication on [PyPI](https://pypi.org/)
* [`README.md`](README.md): This file
* [`conftest.py`](conftest.py): Configuration of fixtures for [pytest](https://docs.pytest.org/en/latest/)
* [`pytest.ini`](pytest.ini): Configuration of [pytest](https://docs.pytest.org/en/latest/) test discovery
* [`setup.json`](setup.json): Plugin metadata for registration on [PyPI](https://pypi.org/) and the [AiiDA plugin registry](https://aiidateam.github.io/aiida-registry/) (including entry points)
* [`setup.py`](setup.py): Installation script for pip / [PyPI](https://pypi.org/)


See also the following video sequences from the 2019-05 AiiDA tutorial:

 * [aiida-qmcchem setup.json](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=240s)
 * [run aiida-qmcchem example calculation](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=403s)
 * [aiida-qmcchem CalcJob plugin](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=685s)
 * [aiida-qmcchem Parser plugin](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=936s)
 * [aiida-qmcchem computer/code helpers](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=1238s)
 * [aiida-qmcchem input data (with validation)](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=1353s)
 * [aiida-qmcchem cli](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=1621s)
 * [aiida-qmcchem tests](https://www.youtube.com/watch?v=2CxiuiA1uVs&t=1931s)
 * [Adding your plugin to the registry](https://www.youtube.com/watch?v=760O2lDB-TM&t=112s)
 * [pre-commit hooks](https://www.youtube.com/watch?v=760O2lDB-TM&t=333s)

For more information, see the [developer guide](https://aiida-qmcchem.readthedocs.io/en/latest/developer_guide) of your plugin.


## Features (TODO)

 * Add input files using `SinglefileData`:
   ```python
   SinglefileData = DataFactory('singlefile')
   inputs['file1'] = SinglefileData(file='/path/to/file1')
   inputs['file2'] = SinglefileData(file='/path/to/file2')
   ```

 * Specify command line options via a python dictionary and `QmcchemParameters`:
   ```python
   d = { 'ignore-case': True }
   QmcchemParameters = DataFactory('qmcchem')
   inputs['parameters'] = QmcchemParameters(dict=d)
   ```

## Installation

```shell
pip install aiida-qmcchem
verdi quicksetup  # better to set up a new profile
verdi plugin list aiida.calculations  # should now show your calclulation plugins
```

## Usage

Here goes a complete example of how to submit a test calculation using this plugin.

A quick demo of how to submit a calculation:
```shell
verdi daemon start     # make sure the daemon is running
cd examples
./example_01.py        # run simple SCF calculation on existing EZFIO database
./example_02.py        # run more advanced 2-step workflow
verdi process list -a  # check record of calculation
```

The plugin also includes verdi commands to inspect its data types:
```shell
verdi data qmcchem list
verdi data qmcchem export <PK>
```

## Development

```shell
git clone https://github.com/q-posev/aiida-qmcchem .
cd aiida-qmcchem
pip install -e .[pre-commit,testing]  # install extra dependencies
pre-commit install  # install pre-commit hooks
pytest -v  # discover and run all tests
```

See the [developer guide](http://aiida-qmcchem.readthedocs.io/en/latest/developer_guide/index.html) for more information.

## License

MIT

## Contact

posenitskiy@irsamc.ups-tlse.fr
