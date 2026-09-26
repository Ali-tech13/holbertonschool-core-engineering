#!/usr/bin/env python3
"""Defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an abstract animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
