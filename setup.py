from setuptools import setup, find_packages

setup(
    name="mqtt2database",
    version="0.0.1",
    description=(
        "library for soundcraft ui16 config management in a sqlite3 db "
        "with the use of mqtt"
    ),
    url="https://github.com/dhoessl/mqtt2database.git",
    author="Dominic Hößl",
    author_email="dhoessl@dhoessl.de",
    license="GPL-v3",
    packages=find_packages(),
    package_data={
        "mqtt2database": ["data/*.sql"]
    },
    include_package_data=True,
    install_requires=["loguru", "paho-mqtt"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ]
)
