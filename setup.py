from setuptools import setup

setup(name='dynalist',
      version='0.1',
      description='CLI and API library for dynalist.io',
      url='https://github.com/dfederschmidt/dynalist',
      author='Daniel Federschmidt',
      author_email='daniel@federschmidt.xyz',
      license='MIT',
      packages=['dynalist'],
      entry_points = {
        'console_scripts': ['dynalist=dynalist.cli:main'],
      },
      zip_safe=False)