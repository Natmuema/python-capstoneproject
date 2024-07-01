import random

# List of words for the game
words = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", 
    "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", 
    "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", 
    "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", 
    "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", 
    "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", 
    "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", 
    "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", 
    "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", 
    "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", 
    "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", 
    "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", 
    "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", 
    "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", 
    "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", 
    "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", 
    "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", 
    "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", 
    "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", 
    "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", 
    "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", 
    "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", 
    "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", 
    "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", 
    "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", 
    "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"
]

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to get a valid letter guess from the user
def get_guess(guessed_letters):
    while True:
        try:
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single letter.")
            if guess in guessed_letters:
                raise ValueError("You have already guessed that letter.")
            return guess
        except ValueError as e:
            print(e)

# Main game function
def play_game():
    word = choose_word(words)
    guessed_letters = set()
    attempts_remaining = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts_remaining > 0:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess: {display_word(word, guessed_letters)}")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word!")
                return
        else:
            attempts_remaining -= 1
            print(f"Incorrect guess. Attempts remaining: {attempts_remaining}")
            print(display_word(word, guessed_letters))

    print(f"Sorry, you lost! The word was '{word}'.")

# Start the game
if __name__ == "__main__":
    play_game()
