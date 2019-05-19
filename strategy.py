"""
Strategy lets the algorithm vary independently from
clients that use it.
"""

import abc


class StrategyMixin:
    """
    StrategyMixin for use in applications.  Adds functionality for processing a
    message into a context for backend integration.
    """
    def create_context(self, message):
        """
        Used to generalize the message in a way that is succinct with our
        backend strategies.  Raise exceptions here to report to clientelle.
        """
        return {'strategy': {'logingest': {'data': message}}}


class IStrategy(abc.ABC):
    """
    Declare an interface common to all supported strategies. Context
    uses this interface to call the strategies.
    """
    @abc.abstractmethod
    def bind(self, context):
        """Bind to the context"""
        pass
