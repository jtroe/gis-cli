from setuptools import setup

REQUIRES_PYTHON = ">=3.7.0"
setup(
    name="giscli",
    version="0.0.1",
    description="giscli--a cli tool to manage your online gis, powered by ArcGIS API for Python",
    long_description="giscli--a cli tool to manage your online gis, powered by ArcGIS API for Python",
    python_requires=REQUIRES_PYTHON,
    author="Jay Roebuck",
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3",
        "Intended Audience :: System Administrators, Developers, ArcGIS API for Python",
        "License :: MIT",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="gis geographic spatial arcgis esri cli",
    zip_safe=False,
    include_package_data=True,
    install_requires=["arcgis>=2.0.1"],
    entry_points={"console_scripts": ["gis = gis:main"]},
)
