from setuptools import setup, find_packages

setup(
    name='halo-test-plugin',
    version='0.3',
    packages=['.'],
    #packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==7.1.2'
    ],
    python_requires='>=3.6',
)