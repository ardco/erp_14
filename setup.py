from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_14/__init__.py
from erp_14 import __version__ as version

setup(
	name="erp_14",
	version=version,
	description="install skipped doctype in eprnext v14",
	author="ARD",
	author_email="Hadeel.milad@ard.ly",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
