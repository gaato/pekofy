from setuptools import setup

setup(
    name='pekofy',
    version='0.1.0',
    description='語尾にぺこをつけるぺこ',
    author='Gakuto Furuya',
    url='https://github.com/gaato/pekofy',
    packages=[''],
    package_dir={'': 'pekofy'},
    python_requires='>=3.7',
    install_requires=open('requirements.txt').read().splitlines(),
)
