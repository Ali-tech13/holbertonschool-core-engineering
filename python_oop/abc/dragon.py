#!/usr/bin/env python3
"""Defines mixins and the Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
