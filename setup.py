from setuptools import setup, find_packages

setup(
    name="click-multi-commands-example",
    version="0.1",
    packages=find_packages(),
    install_requires=["click"],
    extras_require={
        "develop": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "custom_commands = custom_commands.main:cli",
        ],
    }
)
