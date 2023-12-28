# ask you question series by series
# ask you to input the answers
# at last tells you your score and places where you were wrong.


#pseudo code
# asks questions with four option 
# takes input in string
# stroes the input in dictionary where the keys are the right answers
# checks the keys and values

answers = {}
wrong_values = []
correct_answers = []

print("Welcome to python quiz!\n\nAnswer the question that are given below and check your python mastery.\nLet's get started.... \n")

#question 1

print("Q1. What is the correct way to comment multiple lines in Python?")
print(" a) '# Comment'\n b) '/* Comment */'\n c) ''' Comment '''\n d) '// Comment'\n") 
ans1 = input("Your answer(a/b/c/d): ").lower()
q1_correct_answer = 'q1_d'




#note!! this method is too complex compared to direct enter the value set
# user_answers.append(f"q1_{ans1}")  # adds the users answer into the user_answers list
# correct_answers.append(q1_correct_answer) # adds the users answer into the correct_answers list.



answers[q1_correct_answer] = f"q1_{ans1}"  

#question 2

print("\nQ2. Which of the following data types is mutable?")
print(" a) 'int'\n b) 'float'\n c) 'list'\n d) 'tuple'\n") 
ans2 = input("Your answer: ").lower()
q2_correct_answer = 'q2_c'

answers[q2_correct_answer] = f"q2_{ans2}"  


# user_answers.append(f'')
# correct_answers.append(q2_correct_answer)


#question 3

print("\nQ3. How is an exception handled in Python?")
print(" a) 'Using if-else statements'\n b) 'Using try-except blocks'\n c) 'Using for loops'\n d) 'Using while loops'\n") 
ans3 = input("Your answer: ").lower()
q3_correct_answer = 'q3_b'


answers[q3_correct_answer] = f"q3_{ans3}"  

# user_answers.append(f'q_{ans3}')
# correct_answers.append(q3_correct_answer)


#question 4

print("\nQ4. What does the 'len()' function return?")
print(" a) 'The last element of a list'\n b) 'The number of elements in a list '\n c) 'The maximum value in a list'\n d) 'The sum of elemnets in a list'\n") 
ans4 = input("Your answer: ").lower()
q4_correct_answer = 'q4_b'

answers[q4_correct_answer] = f"q4_{ans4}"  

# user_answers.append(f'q4_{ans4}')
# correct_answers.append(q4_correct_answer)


#question 5

print("\nQ5. Which of the following is not a valid variable name in Python?")
print(" a) 'my_variable'\n b) '_variable'\n c) '1_variable'\n d) 'variable_1'\n") 
ans5 = input("Your answer: ").lower()
q5_correct_answer = 'q5_c'

answers[q5_correct_answer] = f"q5_{ans5}"  

# user_answers.append(f'q5_{ans5}')
# correct_answers.append(q5_correct_answer)



correct = 0 # to check the correct answers

for index, (key, value) in enumerate(answers.items()):
    
    if key == value:
        correct += 1
    else: 
        wrong_values.append(index)



print("\nTotal questions = 5")
print(f"You have {correct} correct answers.\n")
# print(answers)

if wrong_values:

    print("You have wrong answer in:")
    for wrong_value in wrong_values:
        print(f'Q.{wrong_value+1}')
else:
    print("Congrats, you have all right answers.")

