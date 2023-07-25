from survey import AnonymousSurvey

question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    language = input("Language: ")
    if language == 'q':
        break
    my_survey.store_response(language)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

