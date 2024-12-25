from flask import Blueprint, jsonify, request
from app.services.poll_manager import PollManager

poll_manager = PollManager()

vote_routes = Blueprint('vote_routes', __name__)

@vote_routes.route('/polls/<int:poll_id>/vote', methods=['POST'])
def vote(poll_id):
    data = request.get_json()
    option_id = data.get('option_id')
    poll = poll_manager.get_poll(poll_id)

    if not poll:
        return jsonify({"error": "Poll not found"}), 404
    
    vote_success = poll_manager.vote(poll_id, option_id)
    if vote_success:
        return jsonify({"message": "Vote successfully cast"}), 200
    else:
        return jsonify({"error": "Invalid option ID"}), 400

