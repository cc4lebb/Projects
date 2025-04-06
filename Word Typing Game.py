import random
import time 
import difflib

#defined list of sentences 
sentences = [
    "The WiFi connection dropped just as he was about to send the email",
    "The CEO emphasized the importance of teamwork during the meeting",
    "She sent an SOS signal when her boat started sinking",
    "The NASA team launched a rocket to explore distant planets today",
    "Fans are becoming really excited as the NBA finals are set",
    "Finish the task ASAP because we need results extremely fast",
    "Education about AIDS saves lives promotes health and reduces stigma",
    "She shared a funny GIF which lightened the mood instantly",
    "The Navy SEALs executed a flawless mission under extreme pressure",
    "The SWAT team swiftly resolved the crisis ensuring everyones safety",
    "The CIA gathered critical intelligence to prevent a potential global threat",
    "The FBI investigated the case thoroughly uncovering crucial evidence for justice",
    "Please provide your DOB to verify your age and identity",
    "Check the FAQ section for quick answers to common questions",
    "Her high IQ allowed her to solve complex problems effortlessly",
    "We packed the SUV for a weekend road trip with friends",
    "Many claim to have seen a UFO hovering mysteriously at night",
    "HTTP is the foundation of data communication on the World Wide Web",
    "The AFL Grand Final is a major event in Australian sports culture",
    "Conduct a SWOT analysis to identify strengths weaknesses opportunities and threats",
]

#calculate accuracy 
def calc_acc(target_sentence, user_input, strict_mode):
    if strict_mode == False:
        find_acc = (difflib.SequenceMatcher(None, str(target_sentence).lower(), str(user_input).lower()).ratio()) 
        acc = round(find_acc * 100)
        return acc
    else:
        find_acc = (difflib.SequenceMatcher(None, str(target_sentence), str(user_input)).ratio()) 
        acc = round(find_acc * 100)
        return acc

#calculate wpm
def calc_wpm(user_input, time_taken):
    word_count = len(user_input.split())
    wpm = round(word_count/ time_taken)
    return wpm    

#introduction  
print("welcome to my Typing Test!")

while True:
    #amount of rounds
    while True:
        rounds = input('enter a number of rounds (3-20): ')
        if rounds.isdigit(): #boolean expression if "rounds" is a digit
            rounds = int(rounds) #converts rounds into an integer (#i changted something here so if it doesnt work look here.
            if rounds >= 3 and rounds <= len(sentences): #len sentences is the length of how many items there are in the sentence list 
                break 
            else:
                print('invalid') 
        else:
            print('invalid') #if it is not a digit then continue the loop.    

    #strict mode
    while True:
        strict_mode = input('would you like to play in strict mode? (y/n): ').lower() 
        if strict_mode == 'y':
            strict_mode = True
            print(f'The test will be case sensitive and in {rounds} rounds.')
            break
        elif strict_mode == 'n':
            strict_mode = False
            print(f'The test will not be case sensitive and in {rounds} rounds. ')
            break
        else:
            print('please enter a valid input')

    #main game
    accuracy = [] 
    words_per_minute = []

    test_sentences = (random.sample(sentences, rounds))

    for index, i in enumerate(test_sentences, start = 1):
        input('\npress enter to start:  ')
        
        target_sentence = i #print the round according to the indexed round 
        print(f'Round {index} of {rounds}. Your sentence is: ')
        print(f'{target_sentence}') #prints off the sentence 

        start = time.time() #start timer
        user_input = input('')
        finish = time.time() #end timer
        time_taken = (finish - start)/60 #turns seconds into minutes 

        wpm = calc_wpm(user_input, time_taken)
        words_per_minute.append(wpm)

        acc = calc_acc(target_sentence, user_input, strict_mode)
        accuracy.append(acc)

        print(f'wpm: {wpm}, accuracy: {acc}')

    print('\ntest complete!')

    print('Resutls: ')
    max_wpm = max(words_per_minute) #max wpm
    print(f'    highest wpm: {max_wpm} ')
    avg_wpm = round(sum(words_per_minute) / rounds, 2) #sum of the ammount of wpm / amount of rounds 
    print(f'    average wpm: {avg_wpm}')
    
    max_accu = max(accuracy) #max accuracy
    print(f'    highest accuracy: {max_accu}')
    avg_accuracy = round(sum(accuracy) / rounds, 2)
    print(f'    average accuracy: {avg_accuracy}\n')

    print('breakdown: ')
    print('round | WPM | Accuracy') 
    print('-'*25)
    for i in range(rounds): #loop to print each rounds score. 
        print(f'{i+1} | {words_per_minute[i]} | {accuracy[i]}% \n')

    #whether player wants to play again
    play_again = input('would you like to play again? (enter y or yes to continue): ').lower() 
    if play_again == 'y' or play_again == 'yes':
        continue
    else:
        break    