from random import shuffle

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, session
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

bp = Blueprint('vote', __name__)


@bp.route('/')
def index():
    try:
        db = get_db()
        db.row_factory = lambda cursor, row: row[0]
        all_snippets = db.execute(
            'SELECT id FROM snippets'
        ).fetchall()
        current_app.logger.info(all_snippets, type(all_snippets))
        voted_snippets = db.execute(
            f'SELECT DISTINCT snippet_id FROM votes WHERE voter_id = {g.user["id"]}'
        ).fetchall()
        current_app.logger.info(voted_snippets)
        remaining_snippets = list(set(all_snippets) - set(voted_snippets))
        current_app.logger.info(remaining_snippets)
        next_snippet = None
        if remaining_snippets:
            shuffle(remaining_snippets)
            next_snippet = remaining_snippets[0]
        current_app.logger.info(next_snippet)
        return render_template('vote/index.html', snippet=next_snippet)
    except:
        return redirect(url_for('auth.login'))

@bp.route('/vote', methods=['POST'])
@login_required
def vote():
    if request.method == 'POST':
        snippet = request.form['snippet']
        vote = request.form['action']
        # body = request.form['body']
        error = None

        # if not title:
        #     error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO votes (voter_id, snippet_id, vote)'
                ' VALUES (?, ?, ?)',
                (g.user['id'], snippet, vote))
            db.commit()
            return redirect(url_for('vote.index'))

    return render_template('vote/index.html')