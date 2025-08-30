import microbit # Do not change these to star imports, the test code neds them
import utime    # like this to work properly!
import radio

# Global constants

ROCK = microbit.Image('00000:09990:09990:09990:00000')
PAPER = microbit.Image('99999:90009:90009:90009:99999')
SCISSORS = microbit.Image('99009:99090:00900:99090:99009')
RPS = (b'R', b'P', b'S')

MYID = b'4c' 

def choose_opponent():
    # """ Return the opponent id from button presses
    #
    # Returns
    # -------
    # byte string:
    #     A two-character byte string representing the opponent ID
    #
    # Notes
    # -------
    # Button A is used to increment a digit of the ID
    # Button B is used to 'lock in' the digit and move on
    # """
    #
    # This function is complete.
    
    # Initialization
    num = [0]*2
    idx = 0
    
    # Main loop over digits
    while idx < len(num):
        microbit.sleep(100)
        # Display only the last character of the hex representation (skip the 0x part)
        microbit.display.show(hex(num[idx])[-1], wait=False)
        # The button increments the digit mod 16, to make sure it's a single hex digit
        if microbit.button_a.was_pressed():
            num[idx] = (num[idx] + 1)%16
        # Show a different character ('X') to indicate a selection
        if microbit.button_b.was_pressed():
            microbit.display.show('X')
            idx += 1
    microbit.display.clear()
    
    # Make sure we return a byte string, rather than a standard string.
    return bytes(''.join(hex(n)[-1] for n in num), 'UTF-8')

def choose_play():
    # Returns the play selected from button presses
    #
    # Returns
    # -------
    # byte string:
    #     A single-character byte string representing a move, 
    # as given in the RPS list at the top of the file.
    # 

    choice = None
    set_count = 0

    while microbit.button_b.was_pressed() == False:
        microbit.sleep(100)
        microbit.display.show('x') # default display if nothing pressed yet
        if microbit.button_a.was_pressed():
             microbit.display.show(microbit.Image(RPS[set_count].decode('utf-8')))
             choice = RPS[set_count]
             set_count = set_count + 1
             if set_count == len(RPS):
                set_count = 0

        if microbit.button_b.was_pressed(): # confirmation
             microbit.sleep(100)
             microbit.display.show('k')
             break
    microbit.display.clear()

    return choice

def send_choice(opponent_id, play, round_number):
    # """ Sends a message via the radio
    #
    # Parameters
    # ----------
    # opponent_id  : byte string
    #     The id of the opponent
    # play         : byte string
    #     One of b'R', b'P', or b'S'
    # round_number : int
    #     The round that is being played
    #
    # Returns
    # -------
    # int:
    #     Time that the message was sent
    # """

    msg1 = (opponent_id + MYID + play).decode()
    msg2 = str(round_number)
    radio.send(msg1+msg2)
    send_time  = utime.ticks_ms()

    return send_time

def send_acknowledgement(opponent_id, round_number):
    # """ Sends an acknowledgement message
    #
    # Parameters
    # ----------
    # opponent_id  : bytes
    #     The id of the opponent
    # round_number : int
    #     The round that is being played
    # """
    #
    msg = (opponent_id + MYID + b'X') +str(round_number).encode()
    send_time  = utime.ticks_ms()
    radio.send_bytes(msg)

    return send_time

def parse_message(opponent_id, round_number):
    # """ Receive and parse the next valid message
    #
    # Parameters
    # ----------
    # opponent_id  : bytes
    #     The id of the opponent
    # round_number : int
    #     The round that is being played
    #
    # Returns
    # -------
    # bytes :
    #     The contents of the message, if it is valid
    # None :
    #     If the message is invalid or does not need further processing
    #
    # Notes
    # -----
    # This function sends an acknowledgement using send_acknowledgement() if
    # the message is valid and contains a play (R, P, or S), using the round
    # number from the message.
    # """
    msg = radio.receive_bytes()
    if not msg:
        return None
    
    if (len(msg) <= 9) and (len(msg) >= 6):
        action = msg[4:5]
        if (MYID == msg[0:2] and opponent_id == msg[2:4]):
            if (action in RPS):
                received_rd = msg[5:len(msg)]
                if received_rd == str(round_number).encode():
                    # also updating for acknowledge
                    send_acknowledgement(opponent_id, received_rd.decode())
                elif received_rd < str(round_number).encode():
                    send_acknowledgement(opponent_id, received_rd.decode())
                    return None
                else:
                    return None
            elif action == b'X':
                return action
            else:
                return None
        else:
            return None
    else:
        return None
    
    return action

def resolve(my, opp):
    # """ Returns the outcome of a rock-paper-scissors match
    # Also displays the result
    #
    # Parameters
    # ----------
    # my  : bytes
    #     The choice of rock/paper/scissors that this micro:bit made
    # opp : bytes
    #     The choice of rock/paper/scissors that the opponent micro:bit made
    #
    # Returns
    # -------
    # int :
    #     Numerical value for the outcome as listed below
    #      0: Loss/Draw
    #     +1: Win
    #
    # Notes
    # -----
    # Input parameters should be one of b'R', b'P', b'S'
    #
    # Examples
    # --------
    # solve(b'R', b'P') returns 0 (Loss)
    # solve(b'R', b'S') returns 1 (Win)
    # solve(b'R', b'R') returns 0 (Draw)
    #
    # """
    #
    # This function is complete.
    
    # Use fancy list indexing tricks to resolve the match
    diff = RPS.index(my) - RPS.index(opp)
    result = [0, 1, 0][diff]
    
    # Display a cute picture to show what happened
    faces = [microbit.Image.ASLEEP, microbit.Image.HAPPY, microbit.Image.SAD]
    microbit.display.show(faces[diff])
    # Leave the picture up for long enough to see it
    microbit.sleep(333)
    return result

def display_score(score, times=3):
    # """ Flashes the score on the display
    #
    # Parameters
    # ----------
    # score : int
    #     The current score
    # times : int
    #     Number of times to flash
    #
    # Returns
    # -------
    # None
    #
    # Notes
    # -----
    # If the score is greater than 9 it scrolls, rather than flashing.
    # """
    #
    # This function is complete.
    
    screen_off = microbit.Image(':'.join(['0'*5]*5))
    if score < 9 and score >= 0:
        microbit.display.show([screen_off, str(score)]*times)
    elif score > 9:
        for n in range(times):
            microbit.display.scroll(str(score))
            microbit.display.show(screen_off)
            microbit.sleep(333)

def main():
    # """ Main control loop"""
    #
    # TODO: fill in parts of code below as marked.
    
    # set up the radio for a moderate range
    radio.config(power=6, queue=50)
    radio.on()
    
    # initialise score and round number
    score = 0
    round_number = 0
    
    # select an opponent
    opponent_id = choose_opponent()
    
    # Run an arbitrarily long RPS contest
    while True:
        # get a play from the buttons
        choice = choose_play()
        # send choice
        send_time = send_choice(opponent_id, choice, round_number)
        
        acknowledged, resolved = (False, False)
        # passive waiting display
        microbit.display.show(microbit.Image.ALL_CLOCKS, wait=False, loop=True)
        while not (acknowledged and resolved):
            # get a message from the radio
            message = parse_message(opponent_id, round_number)
            
            # TODO: if is a play
            if message in RPS:
                # resolve the match and display the result
                result = resolve(choice, message)
                if result == 1:
                    score += 1
                    resolved = True        
                # display the score
                display_score(score)
                continue
                
            # TODO: if is acknowledgement
            if not(radio.get_last_out() == None):
                acknowledged = True
                continue
                
            # TODO: handle situation if not acknowledged
            microbit.sleep(3000)
            if not ( acknowledged and utime.ticks_diff(utime.ticks_ms(),send_time) > 2000 ):
                old_mesg = radio.get_last_out()
                if old_mesg:
                    radio.send_bytes(old_mesg)
                   
        # TODO: Update round number
        round_number += 1

# Do not modify the below code, this makes sure your program runs properly!

if __name__ == "__main__":
    main()
    
    