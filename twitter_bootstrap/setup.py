"""Setup for zope.interface package
"""

import os, sys

try:
    from setuptools import setup, Extension, Feature
except ImportError:
    # do we need to support plain distutils for building when even
    # the package itself requires setuptools for installing?
    from distutils.core import setup, Extension
    extra = {}

else:
    extra = dict(
        namespace_packages=["pramjs"],
        include_package_data = True,
        zip_safe = False,
        tests_require = [],
        install_requires = ['setuptools'],
        )

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description=(
        '********\n'
        )

setup(name='pramjs.twitter_bootstrap',
      version='0.8',
      url='http://pypi.python.org/pypi/pramjs.twitter_bootstrap',
      license='MIT',
      description='Wrapper for twitter bootstrap javascripts',
      author='Microvac Indonesia',
      author_email='dev@microvac.co.id',
      long_description=long_description,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      entry_points="""
      # -*- Entry points: -*-
      [prambanan.library]
      pramjs.twitter_bootstrap = pramjs.twitter_bootstrap.pramlib:PrambananLibrary
      """,
      packages = ['pramjs', 'pramjs.twitter_bootstrap'],
      **extra)

