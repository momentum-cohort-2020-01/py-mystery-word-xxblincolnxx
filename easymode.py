import random


class Game:
    """
    responsibility: run game logic, instantiate other objects
    collaborators: all
    """
    def __init__(self):
        self.game_mode = input('Select difficulty: (E)asy, (N)ormal, (H)ard    ').upper()
        self.possible_words = Words(self.game_mode).words_list
        self.number_guesses = 0
        self.guessed = []
        self.target = self.draw_word(self.possible_words)
        self.play_game()
       
        
    def play_game(self):
        """
        """
        current_board = ' '.join([self.test_target_word(letter) for letter in self.target])
        while self.number_guesses < 10:
            if  '_' in current_board or self.number_guesses < 1:
                print(f'{10 - self.number_guesses} TRIES REMAINING')
                current_board = ' '.join([self.test_target_word(letter) for letter in self.target])
                print(f'Curent Bord: {current_board}')
                self.take_turn()
            else:    
                break
        if '_' in current_board:
            print('YOU LOSE. THATS ALL.')
        else:
            print('YOU WIN!')

    def draw_word(self, possible_words):
        """
        Picks random word that meets criteria of list.
        """
        random_index = random.randint(0, len(possible_words)-1)
        return possible_words[random_index] 
    
    def take_turn(self):
        """
        Propt guess from user. Loops again if letter is already guessed. Returns the letter guessed and appends guessed letters.
        """
        print('')
        whole_word = input('Do you know the word? It will cost 2 guesses. (Y/N)').upper()
        if whole_word == 'Y':
            whole_guess = input('ENTER GUESS   ').upper()
            if whole_guess == self.target:
                self.guessed = whole_guess.split()
                print('THATS CORRECT!')
            else:
                print('You\'re wrong... dumb dumb. That\'ll cost you two guesses!')
                self.number_guesses += 2
        else:
            guess = input('Guess any letter!').upper()
            if guess in self.guessed:
                print('You already guessed that letter, dummy!')
                self.take_turn()
            else: 
                if guess in self.target:
                    print('Congrats! You are smart! Or lucky..')
                else:
                    print('I take back anything nice I have ever said about you.')
                self.guessed.append(guess)
                self.number_guesses += 1
                return guess
            

    def test_target_word(self, letter):
        """
        Evaluates the target word against the guessed-letters list. Returns underscore if word does not contain
        the letter. Otherwise, returns the letter. Use this to build the list to display.
        """
        if letter in self.guessed:
            return letter
        else:
            return ('_')


class Words:
    def __init__(self, game_mode):
        self.words_list = []
        with open('words.txt', 'r') as file:
            open_file = file.readlines()    
            if game_mode == 'E':
                self.words_list = [word.replace('\n','').upper() for word in open_file if len(word) == 7]
                print('You have selected Easy-Mode, your word will have 6 characters.')
            if game_mode == 'N':
                self.words_list = [word.replace('\n','').upper() for word in open_file if len(word) >= 7 and len(word) <= 9]
                print('You have selected Normal-Mode, your word will have 6-8 characters.')
            if game_mode == 'H':
                self.words_list = [word.replace('\n','').upper() for word in open_file if len(word) >= 9]
                print('You have selected Hard-Mode, your word will have 8+ characters.')

    
Game() 
