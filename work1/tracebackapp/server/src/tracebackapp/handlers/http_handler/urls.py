from tracebackapp.handlers.http_handler.handler import ProductCompletionHandler

url = [
    (r'/tracebackapp/product/completion/(?P<start_time>.*)/(?P<end_time>.*)', ProductCompletionHandler),
]
