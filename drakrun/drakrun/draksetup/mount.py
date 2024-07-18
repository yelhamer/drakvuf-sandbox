import os
import subprocess

import click

from drakrun.lib.vm import FIRST_CDROM_DRIVE


def insert_cd(domain, drive, iso):
    subprocess.run(["xl", "cd-insert", domain, drive, iso], check=True)


@click.command(help="Mount ISO into guest", no_args_is_help=True)
@click.argument("iso_path", type=click.Path(exists=True))
@click.option(
    "--domain",
    "domain_name",
    type=str,
    default="vm-0",
    show_default=True,
    help="Domain name (i.e. Virtual Machine name)",
)
def mount(iso_path, domain_name):
    """Inject ISO file into specified guest vm.
    Domain can be retrieved by running "xl list" command on the host.
    """
    iso_path_full = os.path.abspath(iso_path)
    insert_cd(domain_name, FIRST_CDROM_DRIVE, iso_path_full)
