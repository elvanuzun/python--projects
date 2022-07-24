import question_list as QL
import classes

question_list = QL.questions_list
quiz = classes.Quiz(question_list)

quiz.showQuestion()