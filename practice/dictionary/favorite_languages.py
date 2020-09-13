favortie_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python"
    }
humans = ["jen", "sarah", "tom", "alan"]
for human in humans:
    if human in favortie_languages.keys():
        print("Thank you.")
    else:
        print("Please enter your favorite language.")