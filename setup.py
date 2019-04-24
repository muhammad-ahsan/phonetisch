from setuptools import setup, find_packages

setup(name='phonetisch',
      version='0.2.1',
      description='Python implementation of phonetisch algorithms e.g. soundex and Cologne phonetics which are '
                  'phonetic algorithms for English and German. The homophones are '
                  'encoded to the same representation so that they can be matched despite '
                  'minor differences in spellings.',
      long_description=open('README.md').read(),
      url='https://github.com/muhammad-ahsan/soundex-py.git',
      author='Muhammad Ahsan',
      author_email='muhammad.ahsan@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests.*']),
      zip_safe=False)