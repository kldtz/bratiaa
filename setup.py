from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='bratiaa',
      version='0.1.3',
      author='Tobias Kolditz',
      author_email='tbs.kldtz@gmail.com',
      description='Inter-annotator agreement for Brat annotation projects',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/kldtz/bratiaa',
      packages=['bratiaa', 'bratsubset'],
      install_requires=[
          'numpy',
          'matplotlib',
          'pytest',
          'scipy',
          'tabulate'
      ],
      python_requires='>=3.5',
      entry_points={
          'console_scripts': [
              'brat-iaa=bratiaa.agree_cli:main'
          ]
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
      )
