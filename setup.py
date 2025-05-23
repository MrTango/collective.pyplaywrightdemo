# -*- coding: utf-8 -*-
"""Installer for the collective.pyplaywrightdemo package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.pyplaywrightdemo",
    version="1.0a1",
    description="An add-on for Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Maik Derstappen",
    author_email="md@derico.de",
    url="https://github.com/collective/collective.pyplaywrightdemo",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.pyplaywrightdemo/",
        "Source": "https://github.com/collective/collective.pyplaywrightdemo",
        "Tracker": "https://github.com/collective/collective.pyplaywrightdemo/issues",
        # 'Documentation': 'https://collective.pyplaywrightdemo.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
        "plone.api>=1.8.4",
        "plone.app.dexterity",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
            "plone.app.testing",
            "plone.restapi[test]",
            "plone.testing>=5.0.0",
            "pytest",
            "pytest-cov",
            "pytest-playwright",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.pyplaywrightdemo.locales.update:update_locale
    """,
)
