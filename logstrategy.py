"""
Simple echo strategy to output an "ECHO"
"""


from log import create_logger

from strategy import IStrategy


class Logger(IStrategy):
    """Echo Strategy implementation"""
    log = create_logger('logingest')

    def bind(self, context):
        """
        Bind the strategy to the middleware pipeline,
        returning the context
        """
        self.log.info(context)

        # just a pass-through
        return context
