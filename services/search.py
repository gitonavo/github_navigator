import requests
from flask import render_template
from rest.navigator import output_html, HttpError

# TODO put this in config file
GITHUB_URL = 'http://api.github.com'


class SearchService(object):

    @classmethod
    def search_term(cls, term):

        payload = {'q': term, 'sort': 'created', 'order': 'desc', 'per_page': 5}
        headers = {
            "Authorization": "Basic Z2l0b25hdm86R2lUME5hdjA=",
            "Content-Type": "application/json"
        }
        try:
            r = requests.get(GITHUB_URL + '/search/repositories', params=payload, headers=headers)
        except (requests.Timeout, requests.HTTPError) as he:
            raise HttpError(str(he))

        rjson = r.json()
        total_count = rjson.get('total_count', 0)
        items = rjson.get('items', {})

        for item in items:
            branches_url = item.get('branches_url', '')
            if branches_url:
                branches_url = branches_url[:-9] + '/master'
                master_r = requests.get(branches_url)
                if master_r.status_code == 403:
                    item['commit'] = {'error': master_r.text}
                else:
                    master_rjson = master_r.json()
                    commit = master_rjson.get('commit', {})
                    item['commit'] = commit

        print('Got response {}'.format(rjson))
        m_template = render_template('template.html', search_term=term, total_count=total_count, items=items)
        resp = output_html(m_template, 200)
        return resp
