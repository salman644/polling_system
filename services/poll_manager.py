from app.models.poll import Poll
from app.models.option import Option

class PollManager:
    def __init__(self):
        self.polls = {}
        self.poll_counter = 0

    def create_poll(self, title, description, options):
        poll = Poll(title, description)
        for option_text in options:
            option = Option(option_text)
            poll.add_option(option)
        self.poll_counter += 1
        poll.id = self.poll_counter
        self.polls[poll.id] = poll
        return poll

    def get_poll(self, poll_id):
        return self.polls.get(poll_id)

    def vote(self, poll_id, option_id):
        poll = self.get_poll(poll_id)
        if not poll:
            return None
        if option_id in [option.id for option in poll.options]:
            poll.votes[option_id] += 1
            return True
        return False

