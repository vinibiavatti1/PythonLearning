"""
Class Template

* This is the template for class construction
"""
from abc import ABC, abstractmethod
from typing import Any


class ClassTemplate(ABC):
    """
    Summary of the class.

    Some description here.
    """

    ###########################################################################
    # Class Constants
    ###########################################################################

    PUBLIC_CONST = 1      # public
    _PROTECTED_CONST = 2  # protected
    __PRIVATE_CONST = 3   # private

    ###########################################################################
    # Class Attributes
    ###########################################################################

    public_attr = 1      # public
    _protected_attr = 2  # protected
    __private_attr = 3   # private

    ###########################################################################
    # Static Methods
    ###########################################################################

    @staticmethod
    def static_method(parameter: Any) -> None:
        """
        Static method.
        """

    ###########################################################################
    # Class Methods
    ###########################################################################

    @classmethod
    def class_method(cls, parameter: Any) -> None:
        """
        Class method.
        """

    ###########################################################################
    # Magic Methods
    ###########################################################################

    def __init__(self, name: str, surname: str, age: int) -> None:
        """
        Constructor.
        """
        self.name = name         # public attribute
        self._surname = surname  # protected attribute
        self.__age = age         # private attribute

    ###########################################################################
    # Abstract Instance Methods
    ###########################################################################

    @abstractmethod
    def abstract_method(self, parameter: Any) -> None:
        """
        Abstract method.
        """

    ###########################################################################
    # Public Instance Methods
    ###########################################################################

    def public_method(self, parameter: Any) -> None:
        """
        Public method.
        """

    ###########################################################################
    # Protected Instance Methods
    ###########################################################################

    def _protected_method(self, parameter: Any) -> None:
        """
        Protected method.
        """

    ###########################################################################
    # Private Instance Methods
    ###########################################################################

    def __private_method(self, parameter: Any) -> None:
        """
        Private method.
        """

    ###########################################################################
    # Instance Properties
    ###########################################################################

    @property
    def age(self) -> int:
        """Age getter."""
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        """Age setter."""
        self.__age = age

    @age.deleter
    def age(self) -> None:
        """Age deleter."""
        del self.__age