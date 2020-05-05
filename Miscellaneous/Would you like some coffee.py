# Basically, no matter what you say...you're going to get coffee >:)

answer = 'Yes'
question = 'Would you like some coffee?  '

while True:
    guess = str(input(question))

    if guess == answer or guess == 'yes':
        print ('Yes? Ok here it is!')
    elif guess == 'No' or guess == 'no':
        print ('No? Oh you meant yes')
    else:
        print ('Huh? Oh you meant yes')
