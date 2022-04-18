import requests
import random
import json
import re


# Global Variables
URL = 'https://pokeapi.co/api/v2/'
GENERATIONS = [False, False, False, False, False, False, False]
POSSIBlE_GENS = []
DIFFICULTY = 'EASY'
SCORE = 0
GAME_OVER = False
USED_PKMN = []
TOTAL_POSSIBLE_PKMN = 0


def toggleGeneration(index):
    global TOTAL_POSSIBLE_PKMN

    # Switch unselected gen to selected
    if not GENERATIONS[index]:
        GENERATIONS[index] = True
        TOTAL_POSSIBLE_PKMN = TOTAL_POSSIBLE_PKMN + getAmountInGen(index)

    # Switch selected gen to unselected
    elif GENERATIONS[index]:
        GENERATIONS[index] = False
        TOTAL_POSSIBLE_PKMN = TOTAL_POSSIBLE_PKMN - getAmountInGen(index)


def getGenRange():
    POSSIBlE_GENS = [i for i, j in enumerate(GENERATIONS) if j]

    selectedGen = random.choice(POSSIBlE_GENS)

    if selectedGen == 0:
        return [1, 151]

    elif selectedGen == 1:
        return [152, 251]

    elif selectedGen == 2:
        return [252, 386]

    elif selectedGen == 3:
        return [387, 493]

    elif selectedGen == 4:
        return [494, 649]

    elif selectedGen == 5:
        return [650, 721]

    elif selectedGen == 6:
        return [722, 809]


def getAmountInGen(gen):
    if gen == 0:
        return 151

    elif gen == 1:
        return 100

    elif gen == 2:
        return 135

    elif gen == 3:
        return 107

    elif gen == 4:
        return 156

    elif gen == 5:
        return 72

    elif gen == 6:
        return 88


# Get a random Pokemon's data
def getRandPokemonJSON(correctAnswer, difficulty):
    gen = getGenRange()

    # Get random Pokemon that hasn't been used
    if correctAnswer:
        pokedexNum = random.choice([i for i in range(gen[0], gen[1]+1) if i not in USED_PKMN])

    # Get a random pokemon; doesn't matter if it's been used
    else:
        pokedexNum = random.randint(gen[0], gen[1])

    if difficulty == 0:
        # Append that number to end of API URL
        url = URL + 'pokemon/' + str(pokedexNum)

        # Send GET request and return JSON of that Pokemon's data
        return requests.get(url=url)

    elif difficulty == 1:
        # Append that number to end of API URL
        url = URL + 'pokemon-species/' + str(pokedexNum)

        # Send GET request and return JSON of that Pokemon's data
        return requests.get(url=url)


def checkAnswer(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        global SCORE
        SCORE = SCORE + 1
        return True
    else:
        return False


# This function is uses recursion to generate false answer choices for easy difficulty questions
# It takes in a list containing the all current choices (index 0 is always the correct answer), the correct answer's
# primary type, and the correct answer's secondary type (if it has no secondary type, the string "none" is passed in)
def getRandAnswerEasy(choices, ansPrimary, ansSecondary):
    falseData = getRandPokemonJSON(False, 0)

    # Due to the way indexing JSON files works, these are two 'if statements' that are basically the exact same
    # One is for comparing a random Pokemon with two types, and one for if it only has 1 type
    if len(falseData.json()['types']) == 2:
        # Check if random Pokemon is already in list OR if its TWO types are the same as the correct answer
        if (falseData.json()['species']['name'] in choices) or \
                (falseData.json()['types'][0]['type']['name'] == ansPrimary) or \
                (falseData.json()['types'][1]['type']['name'] == ansSecondary):
            temp = getRandAnswerEasy(choices, ansPrimary, ansSecondary)
        else:
            temp = falseData.json()['species']['name']
        return temp

    if len(falseData.json()['types']) == 1:
        # Check if random Pokemon is already in list OR if its ONE type is the same as the correct answer
        if (falseData.json()['species']['name'] in choices) or \
                (falseData.json()['types'][0]['type']['name'] == ansPrimary):
            temp = getRandAnswerEasy(choices, ansPrimary, ansSecondary)
        else:
            temp = falseData.json()['species']['name']
        return temp


def getRandAnswerHard(choices):
    falseData = getRandPokemonJSON(False, 1)

    if falseData.json()['name'] in choices:
        temp = getRandAnswerHard(choices)
    else:
        temp = falseData.json()['name']
    return temp


def newQuestionEasy():
    # Gets a random Pokemon's data
    answerData = getRandPokemonJSON(True, 0)

    # Sets its name
    answerName = answerData.json()['species']['name']

    # Add to list of used Pokemon
    USED_PKMN.append(answerData.json()['id'])

    # Sets its primary type
    answerTypePrimary = answerData.json()['types'][0]['type']['name']
    answerTypeSecondary = 'none'

    # Sets its secondary type if it has one (it is kept as 'none' if it doesn't)
    if len(answerData.json()['types']) == 2:
        answerTypeSecondary = answerData.json()['types'][1]['type']['name']

    # Puts correct answer choice into a list
    AnswerChoices = [answerName]

    # Puts 3 incorrect answer choices into the list
    AnswerChoices.append(getRandAnswerEasy(AnswerChoices, answerTypePrimary, answerTypeSecondary))
    AnswerChoices.append(getRandAnswerEasy(AnswerChoices, answerTypePrimary, answerTypeSecondary))
    AnswerChoices.append(getRandAnswerEasy(AnswerChoices, answerTypePrimary, answerTypeSecondary))

    # Randomize the order of the answer choices
    random.shuffle(AnswerChoices)

    # Finds the index of the correct answer choice (0-3)
    AnswerIndex = AnswerChoices.index(answerName)

    # String for the question itself
    Question = "This Pokémon's typing is " + answerTypePrimary.upper() + '/' + answerTypeSecondary.upper()

    return [Question, AnswerChoices, AnswerIndex]


def newQuestionHard():
    # Gets a random Pokemon's data
    answerData = getRandPokemonJSON(True, 1)

    # Sets its name
    answerName = answerData.json()['name']

    # Add to list of used Pokemon
    USED_PKMN.append(answerData.json()['id'])

    # Sets its Pokedex entry description
    language = answerData.json()['flavor_text_entries'][0]['language']['name']
    answerDescription = ''
    if not language == 'en':
        for x in answerData.json()['flavor_text_entries']:
            if x['language']['name'] == 'en':
                answerDescription = x['flavor_text']
                break
    else:
        answerDescription = str(answerData.json()['flavor_text_entries'][0]['flavor_text'])

    # Puts correct answer choice into a list
    AnswerChoices = [answerName]

    # Puts 3 incorrect answer choices into the list
    AnswerChoices.append(getRandAnswerHard(AnswerChoices))
    AnswerChoices.append(getRandAnswerHard(AnswerChoices))
    AnswerChoices.append(getRandAnswerHard(AnswerChoices))

    # Randomize the order of the answer choices
    random.shuffle(AnswerChoices)

    # Finds the index of the correct answer choice (0-3)
    AnswerIndex = AnswerChoices.index(answerName)

    # String for the question itself
    Question = str(answerDescription)
    Question = Question.replace(answerName, '_________')
    Question = Question.replace(answerName.upper(), '_________')
    Question = Question.replace(answerName.capitalize(), '_________')
    Question = Question.replace(u'\f', u'\n')
    Question = Question.replace('\n', ' ')

    return [Question, AnswerChoices, AnswerIndex]
