"""
Simple log strategy to output messages.
"""


from log import create_logger

from strategy import IStrategy


class Logger(IStrategy):
    """Log Strategy implementation"""
    log = create_logger('logingest')

    def bind(self, context):
        """
        Bind the context to the middleware pipeline,
        returning the context
        """
        self.log.info(context)

        # just a pass-through
        return context
