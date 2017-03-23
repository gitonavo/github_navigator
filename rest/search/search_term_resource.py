from rest.navigator import resource_route, GitHubNavigatorResource, HttpError
from rest.navigator import api
from services.search import SearchService


@resource_route(api, '/navigator')
class SearchTermResource(GitHubNavigatorResource):
    _search_service = SearchService()

    def get(self):
        if self.has_no_args:
            raise HttpError("Must add arguments in the query!")

        term = self.request.args.get('search_term', '')

        print('Handling search request for term {}'.format(term))

        return self._search_service.search_term(term)
