def main():
    words = [
    "able lost darkness learn",
    "road older goes",
    "basic",
    "must seed laid itself hot must",
    "compound decide",
    "trap active paragraph hair review stay written",
    "facing smile vowel chose other",
    "occur shop box metal equal mouse some city"
    ]

    most = (len(phrase.split(" ")) for phrase in words)

    print(max(most))

if __name__ == "__main__" :
    main()