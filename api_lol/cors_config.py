from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'access-control-allow-methods',
)
