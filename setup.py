from setuptools import setup, find_packages, Command
from the_useless_cli.constants import VERSION


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        import shutil
        shutil.rmtree("dist")
        shutil.rmtree("build")
        shutil.rmtree("__pycache__")
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename.endswith(".pyc"):
                    os.unlink(os.path.join(root, filename))
                if filename.endswith(".pyo"):
                    os.unlink(os.path.join(root, filename))
                if filename.endswith("~"):
                    os.unlink(os.path.join(root, filename))
                if filename.endswith(".bak"):
                    os.unlink(os.path.join(root, filename))

setup(
    # ...
    cmdclass={
        "clean": CleanCommand,
    },
)

setup(
    name='the_useless_cli',
    version=VERSION,
    packages=find_packages(),
    author='ItsQuadrus',
    author_email='quadrus@gaboule.com',
    description='A pretty useless CLI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_dir={'the_useless_cli': 'the_useless_cli'},
    install_requires=[
        'typer',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'useless = the_useless_cli.__main__:app',
        ],
    },
)