from setuptools import setup, find_packages

setup(
    name="pydahua",
    version="0.1.1",
    description="Dahua biometric Python integration library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sreethul Krishna",
    author_email="sreethulkrishna24@gmail.com",
    url="https://github.com/KSreethul/pydahua",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.0"
    ],
    license="LGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Access Control",
        "Topic :: System :: Hardware",
    ],
    keywords="biometric dahua attendance api pydahua face-recognition access-control",
)
