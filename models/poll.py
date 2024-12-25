class Poll:
    def __init__(self, title, description):
        self.id = None
        self.title = title
        self.description = description
        self.options = []  # List of Option objects
        self.votes = {}  # Dictionary to keep track of votes

    def add_option(self, option):
        self.options.append(option)
        self.votes[option.id] = 0

    def get_results(self):
        return {option.text: self.votes[option.id] for option in self.options}
