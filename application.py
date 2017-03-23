from flask import Flask


class GitNavApp(object):
    def __init__(self):
        print('Starting GitHub Navigator app.')
        self.app = Flask(__name__)
        self.app.config.update({
            'DEBUG': True,
            'TESTING': True
        })

        self.import_apis()

    def import_apis(self):
        from rest.navigator import NavigatorApi

        NavigatorApi(self.app)

gitnav_app = GitNavApp()
app = gitnav_app.app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, debug=app.config['DEBUG'])
