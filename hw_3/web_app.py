import error_handlers
import routes


def app(environ, start_response):
    clean_path = environ['PATH_INFO'].strip('/')
    if clean_path not in routes.app_routes:
        return error_handlers.page_not_found(start_response)

    handler = routes.app_routes[clean_path]
    return handler(environ, start_response)
