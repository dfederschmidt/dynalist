class Error(Exception):
    pass

class InvalidTokenError(Error):
    def __init__(self, message):
            self.message = message

class RateLimitedError(Error):
    def __init__(self, message):
            self.message = message