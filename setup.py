from setuptools import setup

setup(name='bratiaa',
      version='0.0.1',
      author='Tobias Kolditz',
      author_email='tbs.kldtz@gmail.com',
      description='Inter-annotator agreement for Brat annotation projects',
      packages=['bratiaa', 'bratsubset'],
      install_requires=[
          'filelock',  # imported by bratsubset.annotation.py, but not used here (read-only)
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
