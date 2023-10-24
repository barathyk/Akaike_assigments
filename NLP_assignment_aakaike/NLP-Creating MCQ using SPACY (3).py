#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install spacy # installing spacy for text processing')


# In[2]:


# importing libraries that are necessory
import spacy
import random
# !python -m spacy download en_core_web_sm # python package to be downloaded for text processing


# In[3]:


# creating object for loding the english language model
nlp = spacy.load("en_core_web_sm")


# In[12]:


# function to get text as input and no of questions
def get_mca_questions(context: str, num_of_questions):
    doc = nlp(context)

    # function block for gerating the mcq question format
    def generate_mcq_with_multiple_ans(question, correct_ans, options, num_of_options=4):
            options = correct_ans + options
            random.shuffle(options)

            mcqs = {
                "question": question,
                "options": options,
                "correct_answers": correct_ans
            }

            return mcqs

    # function block to generate question,options and correct answers
    def generate_variety_question():
        sentence = random.choice(list(doc.sents))
        blank_word = random.choice([token for token in sentence if not token.is_punct])

        question_text = sentence.text.replace(blank_word.text, "______")
        correct_answers = [blank_word.text]

        other_options = [token.text for token in doc if token.is_alpha and token.text != correct_answers[0]]
        num_correct_options = random.randint(1, 2)  # Generate 1 or 2 correct options
        correct_answers.extend(random.sample(other_options, num_correct_options))

        num_other_options = min(4 - num_correct_options, len(other_options))
        other_options = random.sample(other_options, num_other_options)

        mcq = generate_mcq_with_multiple_ans(question_text, correct_answers, other_options)
        return mcq

    questions = [generate_variety_question() for _ in range(num_of_questions)]

    mca_questions = []
    # iterating over the question ,option and coorects ans
    for i, question in enumerate(questions, start=1):
        question_txt = f"Question{i}: {question['question']}\n"
        options_txt = ""
        for j, option in enumerate(question['options']):
            options_txt += f"{j+1}. {option}\n"

        correct_options = " , ".join([f"({chr(97+question['options'].index(ans))})" for ans in question['correct_answers']])
        correct_options_str = f"Correct Options: {correct_options}"

        mca_question = f"{question_txt}{options_txt}{correct_options_str}\n"
        mca_questions.append(mca_question)
    return mca_questions

# iterating thorugh the total question one by one and printing it
context = input("Enter the paragraph: ")
num_of_questions = int(input("Enter the number of questions: "))
mca_questions = get_mca_questions(context, num_of_questions)
for question in mca_questions:
    print(question)


# In[ ]:




