from setuptools import setup, find_packages

# python3 setup.py sdist bdist_wheel

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='pwger_private',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/FabianKP/pwger',
    license='GNU-GPL',
    author='Fabian Parzer',
    entry_points={"console_scripts": ["pwger_private=pwger_private.main:cli"]},
    description='Generiert eine Passphrase aus zufälligen deutschen Wörtern.',
    install_requires=[
        'numpy',
        'optparse-pretty',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: GNU GPL-2.0'
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)