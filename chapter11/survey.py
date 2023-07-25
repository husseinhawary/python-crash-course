class AnonymousSurvey:

    def __init__(self, question):
        """
        Store a question and prepare to store a responses.
        :param question:
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """
        Show the survey question
        :return:
        """
        print(self.question)

    def store_response(self, new_response):
        """
        Store a single response to the survey
        :param new_response:
        :return:
        """
        self.responses.append(new_response)

    def show_results(self):
        """
        show all responses that have been given
        :return:
        """
        print("Survey Results: ")
        for response in self.responses:
            print(f"- {response}")
