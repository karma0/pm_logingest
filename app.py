from flask import Flask
from flask_restful import Resource, Api

from strategy import StrategyMixin
from awsstrategy import Firehose
from logstrategy import Logger


app = Flask(__name__)
api = Api(app)


class LogIngest(Resource, StrategyMixin):
    middleware_strategies = (
        Logger(),
        Firehose(),
    )

    def get(self, message, *args, **kwargs):
        return self._process_message(message, *args, **kwargs)

    def put(self, message, *args, **kwargs):
        return self._process_message(message, *args, **kwargs)

    def _process_message(self, message):
        try:
            context = self.create_context(message)
            for strategy in self.middleware_strategies:
                context = strategy.bind(context)
            status = "Success."
        except:
            # TODO: more descriptive
            status = "Failure."
        return {'status': status}


api.add_resource(LogIngest, '/<string:message>')


if __name__ == '__main__':
     app.run(port=8080)
