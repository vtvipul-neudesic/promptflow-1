from setuptools import find_packages, setup

PACKAGE_NAME = "oai"

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": [
            "oai_search = oai.tools.utils:list_package_tools",
            "oai_setupenv = oai.tools.oai_setupenv:oai_setupenv_tool",
        ],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
