from flask import Blueprint, jsonify, request
from app.services.poll_manager import PollManager

poll_manager = PollManager()

poll_routes = Blueprint('poll_routes', __name__)

@poll_routes.route('/polls', methods=['POST'])
def create_poll():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    options = data.get('options')

    if not title or not options:
        return jsonify({"error": "Title and options are required"}), 400

    poll = poll_manager.create_poll(title, description, options)
    return jsonify({
        "poll_id": poll.id,
        "title": poll.title,
        "options": [option.text for option in poll.options]
    }), 201


@poll_routes.route('/polls/<int:poll_id>', methods=['GET'])
def get_poll(poll_id):
    poll = poll_manager.get_poll(poll_id)
    if not poll:
        return jsonify({"error": "Poll not found"}), 404

    return jsonify({
        "poll_id": poll.id,
        "title": poll.title,
        "description": poll.description,
        "options": [option.text for option in poll.options],
        "results": poll.get_results()
    })

