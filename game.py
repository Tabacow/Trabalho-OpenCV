from os import startfile
import numpy as np
import time
import keyboard

class Game:

    def __init__(self, vision, controller, heroes):
        self.vision = vision
        self.controller = controller
        self.heroes = heroes
        self.state = 'no status'
        self.working_time = 0 # working_time is set on seconds!
        self.shift_count = 0

    def run(self):
        
        
        while True:
            self.vision.refresh_frame()

            if(self.state == 'no status'):
                self.state = self.get_initial_state()

            if (self.check_errors()):
                self.reset_game()
            
            if self.state == 'not started' and self.is_connect_screen():
                self.log('Connecting...')
                self.launch_player()
                

            if self.state == 'connecting' and self.is_select_wallet():
                self.log('Authorizing...')
                self.login_metamask()
                self.state = 'authorize'

            if self.state == 'authorize' and self.is_authorize() and self.check_metamask_popup_check():
                self.log('Authorized! Now Loading...')
                self.authorize_metamask()
                self.state = 'in menu'
            
            if self.state == 'in menu' and self.is_menu():
                self.log('in game menu, going to heroes...')
                self.open_heroes()
                self.state = 'heroes opened'

            if self.state == 'heroes opened' and self.is_on_hero_menu():
                self.log('in hero menu, scrolling down...')
                self.state = 'hero menu'

            if self.state == 'hero menu' and self.is_on_hero_menu():
                self.log('hero menu opened!')
                self.state = 'selecting heroes'

            if self.state == 'selecting heroes' and self.is_heroes_resting():
                self.log('selecting heroes...')
                okay = self.send_heroes_to_work()
                if(okay):
                    self.state = 'lets go to work!'
                if(not okay):
                    self.reset_game()
                

            if self.state == 'lets go to work!' and self.is_on_hero_menu():
                self.log('selecting heroes...')
                self.exit_heroes()
                self.state = 'going to game'

            if self.state == 'going back to menu' and self.is_in_game():
                self.log('going back to menu...')
                self.from_game_to_menu()
                self.state = 'in menu'

            if self.state == 'going back to menu' and not self.is_in_game():
                self.log("something went wrong, reseting...")
                self.reset_game()

            if self.state == 'going to game' and self.is_menu():
                self.log('going to game...')
                self.go_to_game()
                self.state = 'im on game'

            if(self.state == 'im on game' and self.is_new_map()):
                self.log('going to next map...')
                self.go_to_next_map()
                
            if(self.state == 'im on game' and self.is_in_game()):
                self.log('im gamming... >:(')
                self.counting_work_time()
                if(self.working_time == 0 ):
                    self.heroes.change_all_to_false()
                    self.heroes.print_hero_status()
                    self.state = 'going back to menu'

            time.sleep(1)

#    def round_starting(self, player):
#        matches = self.vision.find_template('%s-health-bar' % player)
#        return np.shape(matches)[1] >= 1

    def launch_player(self):
        # Try multiple sizes of goalpost due to perspective changes for
        # different opponents
        scales = [1.2, 1.1, 1.05, 1.04, 1.03, 1.02, 1.01, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95]
        matches = self.vision.scaled_find_template('connect-wallet', threshold=0.75, scales=scales)
        if(np.shape(matches)[1] >= 1):
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+60,y+20)
            time.sleep(0.2)
            self.controller.left_mouse_click()
            time.sleep(0.5)
            self.state = 'connecting'
    
    def login_metamask(self):
        matches = self.vision.find_template('metamask', threshold=0.8)
        if(np.shape(matches)[1] >= 1):
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+45,y+20)
            time.sleep(0.2)
            self.controller.left_mouse_click()
            time.sleep(0.2)
        else:
            matches = self.vision.find_template('metamask-dark', threshold=0.8)
            if(np.shape(matches)[1] >= 1):
                x = matches[1][0]
                y = matches[0][0]
                self.controller.move_mouse(x+45,y+20)
                time.sleep(0.2)
                self.controller.left_mouse_click()
                time.sleep(0.2)
        time.sleep(0.2)

    def authorize_metamask(self):
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('enter')
            time.sleep(0.2)
    
    def open_heroes(self):
        matches = self.vision.find_template('heroes', threshold=0.9)
        x = matches[1][0] + 10
        y = matches[0][0] + 10
        self.controller.move_mouse(x,y)
        time.sleep(0.2)
        self.controller.left_mouse_click()
        time.sleep(0.2)

    def counting_work_time(self):
        time_period = 60
        self.working_time = self.working_time - time_period
        time.sleep(time_period)
        self.log("there is still " + str(self.working_time/time_period) + " minutes left...")
        self.shift_count += 1
        if((self.shift_count % 5) == 0):
            if(self.check_errors() or not self.is_in_game):
                self.reset_game()
                return
            self.from_game_to_menu()
            time.sleep(3)
            self.vision.refresh_frame()
            matches_go_to_game = self.vision.find_template_and_print('game', threshold=0.7) # se der pau, olha a foto res.png
            if(self.check_errors() or not self.is_menu()):
                self.reset_game()
                return
            self.log("found game")
            x = matches_go_to_game[1][0]
            y = matches_go_to_game[0][0]
            self.controller.move_mouse(x+30,y+30)
            time.sleep(0.4)
            self.controller.left_mouse_click()
            
  
    def send_heroes_to_work(self):
        self.log("now im selecting heroes...")
        self.vision.refresh_frame()
        match = self.vision.find_template('heroes-header', threshold=0.95)
        x = match[1][0] + 75
        y = match[0][0] + 75
        self.controller.move_mouse(x,y)
        time.sleep(0.2)
        scroll = 0
        okay = True
        while(not self.heroes.is_all_heroes_working() and self.is_on_hero_menu()):
            okay = self.find_heroes_in_vision()
            if(not okay):
                return okay
            while(scroll < 20):
                self.controller.mouse_scroll(0,-100)
                time.sleep(0.1)
                scroll += 1
            scroll = 0
        self.log("found all heroes...")
        return okay


    def find_heroes_in_vision(self):
        hero_count = 1
        while(hero_count <= 15):
            self.vision.refresh_frame()
            if (self.check_errors()):
                self.log("SOMETHING WENT WRONG, IM GOING TO RESET!")
                return False
                
            self.log("looking for hero " + str(hero_count))
            match_hero = self.vision.find_template(str(hero_count), threshold=0.95)
            if(np.shape(match_hero)[1] >= 1):
                match_work = self.vision.find_template('work-off', threshold=0.9)
                x = match_work[1][0] + 10
                y = match_hero[0][0] + 10
                self.controller.move_mouse(x,y)
                time.sleep(0.2)
                self.controller.left_mouse_click()
                time.sleep(1)
                self.heroes.change_status(hero_count, True)
                self.log("found hero " + str(hero_count))
            hero_count += 1
            time.sleep(0.1)
        self.heroes.print_hero_status()
        return True

        


    def exit_heroes(self):
        matches = self.vision.find_template('exit-heroes', threshold=0.9)
        x = matches[1][0]
        y = matches[0][0]
        self.controller.move_mouse(x,y)
        time.sleep(0.4)
        self.controller.left_mouse_click()

    def go_to_game(self):
        if(self.working_time == 0):
            self.working_time = 3300
            self.shift_count = 0
        else:
            self.log("there is still " + str(self.working_time) + " seconds of working time left!!!")
        matches = self.vision.find_template('game', threshold=0.6)
        x = matches[1][0]
        y = matches[0][0]
        self.controller.move_mouse(x+30,y+30)
        time.sleep(0.4)
        self.controller.left_mouse_click()

    def check_errors(self):
        self.vision.refresh_frame()
        match_unknown = self.vision.find_template('unknown', threshold=0.7)
        match_overloaded = self.vision.find_template('overloaded', threshold=0.7)
        match_abnormal_disconection = self.vision.find_template('abnormal-disconection', threshold=0.7)
        match_socket_1 = self.vision.find_template('socket-1', threshold=0.7)
        match_manual = self.vision.find_template('manual', threshold=0.7)
        match_communication_error = self.vision.find_template('communication-error', threshold=0.7)
        is_error_unknown =  np.shape(match_unknown)[1] >= 1
        is_error_overloaded =  np.shape(match_overloaded)[1] >= 1
        is_error_abnormal_disconetion =  np.shape(match_abnormal_disconection)[1] >= 1
        is_error_socket_1 =  np.shape(match_socket_1)[1] >= 1
        is_error_manual =  np.shape(match_manual)[1] >= 1
        is_error_communication_error =  np.shape(match_communication_error)[1] >= 1
        return is_error_unknown or is_error_overloaded or is_error_abnormal_disconetion

    def from_game_to_menu(self):
        matches = self.vision.find_template('go-back', threshold=0.6)
        if(np.shape(matches)[1] >= 1):
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+20,y+20)
            time.sleep(0.4)
            self.controller.left_mouse_click()

    #def is_everyone_sleeping(self):
    #    blank_sleep = self.vision.count_item_on_image(object="blank-sleep")
    #    one_z = self.vision.count_item_on_image(object="one-z-sleep")
    #    two_z = self.vision.count_item_on_image(object="two-z-sleep")
    #    three_z = self.vision.count_item_on_image(object="three-z-sleep")
    #    total = blank_sleep + one_z + two_z + three_z
    #    self.log("i found " + str(total) + ' sleepyheads!') 
    #    return total == 15

    def go_to_next_map(self):
        matches = self.vision.find_template('new-map', threshold=0.6)
        x = matches[1][0]
        y = matches[0][0]
        self.controller.move_mouse(x+20,y+20)
        time.sleep(0.4)
        self.controller.left_mouse_click()

    def get_initial_state(self):
        self.log("getting initial state...")
        if(self.working_time > 0):
            self.log("there is still game time")
            return "going to game"
        else:
            if(self.is_connect_screen()):
                self.log("not started? no problem! starting...")
                return "not started"
            if(self.is_menu()):
                self.log("hmm the menu? can i get some spaghetti and meatballs?")
                return "in menu"
            if(self.is_on_hero_menu()):
                self.log("heroes menu? lets send em to work!")
                return "hero menu"
            if(self.is_in_game()):
                self.log("looks like you're in the game, thats not allowed >:(, im going back to the menu!")
                return "going back to menu"
    
    def is_select_wallet(self):
        matches = self.vision.find_template('select-wallet', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_authorize(self):
        matches = self.vision.find_template('metamask-popup', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_heroes_resting(self):
        matches = self.vision.find_template('work-off', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_menu(self):
        matches = self.vision.find_template('game-screen', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_on_hero_menu(self):
        matches = self.vision.find_template('heroes-header', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_in_game(self):
        matches = self.vision.find_template('in-game-chest-and-options', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def is_connect_screen(self):
        matches = self.vision.find_template('connect-screen', threshold=0.9)
        return np.shape(matches)[1] >= 1
        
    def is_new_map(self):
        matches = self.vision.find_template('next-map', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def check_metamask_popup_check(self):
        matches = self.vision.find_template('metamask-popup-check', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def check_bomb_crypto_logo(self):
        matches = self.vision.find_template('bomb-crypto-logo', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def log(self, text):
        print('[%s] %s' % (time.strftime('%H:%M:%S'), text))

    def reset_game(self):
        keyboard.press_and_release('F5')
        self.state = 'not started'