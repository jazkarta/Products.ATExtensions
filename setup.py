from setuptools import setup, find_packages

version = '0.9.7'

setup(name='Products.ATExtensions',
      version=version,
      description="This package provides some further fields and widgets for archetypes.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raphael Ritz',
      author_email='r.ritz@biologie.hu-berlin.de',
      url='http://pypi.python.org/pypi/Products.ATExtensions',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
