
random_locations = [' San antonio' ,' New Braunfells', ' Dallas' ,' Fort Worth',' Corpus Christie']
random_entertainment = [' Schliterbahn' ,' JFK Memorial' ,' The Alamo' ,' Billy Bobs' ,' Line dancing lessons' ,'the beach',
 ' the gun range' ,' SeaWorld' ,' wine tasting']
random_food = ['The Seafood Place' ,'The Country Food Place' , 'The Italian Food Place' ,'The Pizza Place' ,'The BBQ Place']
random_transporation = [' chariot', ' plane' ,' motorcycle' ,' train' ,' bus' ,' car' ,' horse']

from ast import Return
import random

def greeting():
    #convert to set so it cant repeat
    location_parameter = random.choice(random_locations)
    user_choice = input('Hi we have a trip planed for you, you will be going to' + location_parameter + ' is that okay with you, yes or no?')
    if user_choice == "yes":
           print('perfect!')
    while user_choice != "yes":
        #dont assign it to a variable so it stays random.
        user_choice = input('would' + random.choice(random_locations) + 'work better?')
        # need to be able to say no more than once
    return location_parameter      
result = greeting()

def ride():
    transportation_parameter = random.choice(random_transporation)
    choice_of_transportation = input("we have selected" + transportation_parameter + ' as your means of travel, is that okay, yes or no?')
    #chooses alternative tranportation
    if choice_of_transportation == 'yes':
            print('sounds good ')
    while choice_of_transportation != 'yes':
       choice_of_transportation = input("sorry to hear that, would" + (random.choice(random_transporation)) + ' be more accetable?')
    return transportation_parameter    
vehicle = ride()


def entertainment():
    entertainnment_parameter = random.choice(random_entertainment)
    choice_of_entertainment = input('for your activities we have chosen' +  entertainnment_parameter + ' does that sound good, yes or no?')
   #chooses alternative enterarianment
    if choice_of_entertainment == 'yes':
            print('perfect')
    while  choice_of_entertainment != 'yes':
        choice_of_entertainment = input('that is no problem, would' + random.choice(random_entertainment) + 'sound more fun?')
    return entertainnment_parameter    

fun = entertainment()

def restuaraunts():
    food_parameter = random.choice(random_food)
    choice_of_food = input("the last thing we have chosen for you is your meals, for that we have chosen" + food_parameter + 'does that sound appetizing, yes or no?')
    #chooses alternative food
    if choice_of_food == 'yes':
            print( 'Perfect we have now finished processing your day trip.')
    while choice_of_food != 'yes':
       choice_of_food = input('thats ok how would you like to try' +random.choice(random_food) + 'is that better, yes or no?')
    return  food_parameter   

food = restuaraunts()

def confirmation():
    final_confirmation = print( 'does this look right to you?' )
    print(result)
    print(vehicle)
    print(fun)
    print (food)
    final_confirmation = input('yes or no?')
    if final_confirmation == 'yes':
        print('You are all set then')

final = confirmation()
