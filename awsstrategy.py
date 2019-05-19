"""
Simple AWS strategies
"""
import json

import boto3

from strategy import IStrategy


def serialize(data):
    """Serialize the aforementioned data"""
    return json.dumps(data)


class Firehose(IStrategy):
    """
    Firehose strategy - puts data from the API onto an AWS firehose.

    Parameters:
        *apiname (optional) - Defaults to 'logingest'. Used as the key under
            context["strategy"], data is the pulled from ['data'].
        *region (optional) - Region name of the AWS firehose. Default: us-east-1
    """
    def __init__(self, stream_name='logingest', apiname='logingest', region='us-east-1'):
        self.name = stream_name
        self.apiname = apiname

        self.firehose = boto3.client('firehose', region_name=region)

    def bind(self, context):
        """
        Bind the strategy to the middleware pipeline,
        returning the context.
        """
        self.firehose.put_record(
            **self._parametize(context["strategy"][self.apiname]["data"]))
        return context

    def _parametize(self, data):
        """
        Parameterizes the context's data in a way that's familiar to Firehose.
        """
        return {
            "DeliveryStreamName": self.name,
            "Record": {
                "Data": serialize(data)
                }
            }
