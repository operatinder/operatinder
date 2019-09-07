from flask import current_app
from flask_restplus import Resource, Api

from .db import get_db

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def init_app(app):

    api = Api(app)

    @api.route('/api')
    class HelloWorld(Resource):
        def get(self):
            return {'answer': 'Nothing realy here ... Maybe try /api/segments'}

    @api.route('/api/segments')
    class AllSegments(Resource):

        def get(self):
            db = get_db()
            db.row_factory = dict_factory
            all_segments = db.execute(
                'SELECT id, label, tape, url, start_tc, end_tc FROM segments'
            ).fetchall()
            return {'answer': all_segments}

