"""
pycosec package


Expose the main client class at package level for convenience.
"""


from .biometric import DahuaAPI


__all__ = ["DahuaAPI"]
__version__ = "0.1.1"