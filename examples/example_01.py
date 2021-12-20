#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run a test calculation on localhost.

Usage: ./example_01.py
"""
from os import path
import click
from aiida import cmdline, engine
from aiida.plugins import CalculationFactory
from aiida.orm import Dict, load_code, load_computer
from aiida.common.exceptions import NotExistent

INPUT_DIR = path.join(path.dirname(path.realpath(__file__)), 'input_files')


def test_run_scf(qmcchem_code, computer):
    """Run a calculation on the localhost computer.

    """
    if not computer:
        try:
            computer = load_computer('localhost')
        except:
            raise Exception('You forgot to provide the --computer argument'
                            ) from NotExistent

    if not qmcchem_code:
        try:
            qmcchem_code = load_code('qmcchem@localhost')
        except:
            raise Exception(
                'You forgot to provide the --code argument') from NotExistent

    # Prepare input parameters
    ezfio_name = 'hcn.ezfio'
    qmcchem_commands = [f'set_file {ezfio_name}', 'run scf']

    ezfio_tar = path.join(INPUT_DIR, f'{ezfio_name}.tar.gz')
    prepend_commands = [f'cp {ezfio_tar} .']

    qmcchem_parameters = {
        'qp_prepend': prepend_commands,
        'qp_commands': qmcchem_commands,
        'ezfio_name': ezfio_name
    }

    inputs = {
        'code': qmcchem_code,
        'parameters': Dict(dict=qmcchem_parameters),
        'metadata': {
            'computer': computer
        }
    }

    result = engine.run(CalculationFactory('qmcchem'), **inputs)
    energy = float(result['output_energy'])

    print(f'Computed SCF energy: \n  {energy}')


@click.command()
@cmdline.utils.decorators.with_dbenv()
@cmdline.params.options.CODE()
@cmdline.params.options.COMPUTER()
def cli(code, computer):
    """Run example_01: SCF calculation using QP2 on existing EZFIO database.

    Example usage: $ ./example_01.py --code qmcchem@localhost --computer localhost

    Alternative (loads qmcchem@localhost code and localhost computer): $ ./example_01.py

    Help: $ ./example_01.py --help
    """

    test_run_scf(code, computer)


if __name__ == '__main__':
    cli()  # pylint: disable=no-value-for-parameter
