from setuptools import setup
from pv import __version__

setup(name="capybara",
      version=__version__,
      description="A MongoDB/Solr search connector",
      author="Phos",
      author_email="phosphos0@gmail.com",
      license="AGPLv3",
      url="https://code.google.com/p/capybara/",
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python"])
