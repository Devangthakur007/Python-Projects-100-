def mad_libs():
    print("Welcome to the Mad Libs Generator!")
    print("Please enter the request words to complete the story.\n")

    # Collect the fraking inputs
    noun1 = input("Enter a noun (e.g., dog, robot): ")
    adjective1 = input("Enter am adjective(e.g., shiny, noisy): ")
    verb1 = input("Enter a verb ending in -ing (e.g., dancing, flying): ")
    place = input("Enter a place (e.g., park, kitchen): ")
    plural_noun = input("Enter a plural noun (e.g., bananas, shoes): ")
    adjective2 = input("Enter another adjective (e.g., weird, massive): ")


    # have to buils so i am building a story using multi-line f-string

    story = f""" 
    ---Mad libs story---

    one day, a {adjective1} {noun1} was seen doing {verb1} around the {place}.
    Out of nowhere, a group of {plural_noun} appeared!
    It was completely {adjective2}, but everyone had a great time watching it happen. 
    """
    # Doing that much typing so do you think i do not add print statement :(

    print(story)

    # see you are wrong sike :)

mad_libs()