class UnauthorizedError(Exception):
    '''Raised when the client is tryint to make a request without being authorized by the server.'''
    pass


class UUIDNotFoundError(Exception):
    '''Raised when '''
    pass


class MissingUUIDError(Exception):
    '''Raised when the message does not have a `uuid` key.'''
    pass


class CheckFailureError(Exception):
    '''Raised when the check fails while the message is being dispatched.'''
    pass


class InvalidRouteType(Exception):
    '''Raised when the route type is not valid.'''
    pass


class ClientRuntimeError(Exception):
    '''Raised when the client returns back `Payloads.error`.'''
    pass