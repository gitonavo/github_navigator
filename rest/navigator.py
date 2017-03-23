import flask
from flask_restful import Api, Resource

api = Api()


def resource_route(api, rule, **options):
    def routed_resource(cls):
        api.add_resource(cls, rule, **options)

    return routed_resource


@api.representation('text/html')
def output_html(data, code, headers=None):
    # resp = flask.Response(format_data(data), mimetype='text/html', headers=headers)
    resp = flask.make_response(data, code)
    resp.status_code = code
    return resp


class HttpError(Exception):
    code = 500

    def __init__(self, message="", code=None, **kwargs):
        super(Exception, self).__init__(message, **kwargs)

        if code:
            self.code = code


class GitHubNavigatorResource(Resource):
    def __init__(self):
        self.request = flask.request

    @property
    def has_no_args(self):
        return self.request.args is None


# noinspection PyUnresolvedReferences
class NavigatorApi(object):
    """
    Provides the resources needed for the GitHub Navigator app
    """
    def __init__(self, app):
        from search.search_term_resource import SearchTermResource
        api.init_app(app)
