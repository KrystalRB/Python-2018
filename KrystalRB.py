import random


answers = ["probably not.", "that you should do the exact opposite of that as soon as possible.", "absolutely!",
           "that it is as inevitable as your death.", "for sure, for sure.",
           "please, for the love of all things good, no.", "maybe.", "come back later, I don't care enough right now.",
           "mayhaps.", "that, based on my knowledge, which is everything, it's a strong potential maybe.",
           "a circle has no beginning."]


name = input("Who goes there? State your name, brave adventurer. ")


while True:
    question = input("Let's cut to the chase, %s. Ask me your question, so that I may bestow my knowledge upon thee. "
                     % name)
    if question == "Quit":
        print("You are a coward and a fool for abandoning me. You're just like your father, %s." % name)
        break
    else:
        print("I have taken your question into consideration, %s, and I believe that the only possible answer is "
              % name + "%s." % random.choice(answers))
