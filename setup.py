from setuptools import setup, find_packages


setup(
    name='free_the_paper',
    version='0.0.0',
    license='GNU General Public License v3.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        ]
    )
