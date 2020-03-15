class DSN:
    def __init__(self, schema: str, host: str, port: int):
        self.__schema = schema
        self.__host = host
        self.__port = port

    @property
    def schema(self):
        return self.__schema

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @classmethod
    def parse(cls, dsn: str) -> 'DSN':
        schema, dsn_url = dsn.split('://')
        host, port = dsn_url.split(':')
        return cls(schema, host, int(port))
