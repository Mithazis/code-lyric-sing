#  cara menjalankan 
#  pastikan sudah install python
#  tinggal click kanan kemudian run python
#  atau buka terminal kemudian copas : python perfect.py


import time
import os
import sys

TEXT_SPEED = 0.07

lyrics = [
    "Cause we were just kids when we fell in love",
    "not knowin' what it was",
    "I will not give you up this time",
    "Oh darling, just kiss me slow, your heart is all I own",
    "And in your eyes, you're holding mine",
    "Baby, I'm dancin' in the dark with you between my arms",
    "Barefoot on the grass",
    "while listenin' to our favourite song",
    "When you said you looked a mess",
    "I whispered underneath my breath",
    "But you heard it, Darling, you look perfect tonight"
]

term_width = 70

pause_words = {
    "love": 1.0, "was": 1.0, "time": 1.0, "own": 1.0, "mine": 1.2, "arms": 1, "song": 0.5, "grass": 0.7, "mess": 1, "tonight": 5
}

pause_per_baris = {
    2: {"up": 1.0},
    3: {"slow,": 0.7},
    4: {"eyes,": 0.5},
    5: {"i'm": 1, "dark": 1.5},
}

slow_words = {}

slow_per_baris = {
    0: {"fell": 0.2, "in": 0.1 },
    1: {"knowin'":0.1, "what": 0.2, "it": 0.1},
    2: {"give": 0.2, "you": 0.2, "up": 0.1, "time": 0.5},
    3: {"just": 0.1, "kiss": 0.2, "me": 0.1, "heart": 0.1, "is": 0.2, "all": 0.1},
    4: {"eyes,": 0.2, "mine": 0.3},
    5: {"baby,": 0.2, "i'm": 0.3, "dancin'": 0.3},
    6: {"barefoot": 0.2, "on": 0.2},
    7: {"our": 0.2},
    8: {"said": 0.2, "looked": 0.1},
    9: {"underneath": 0.1},
    10: {"you": 0.2, "heard": 0.2, "darling,": 0.1, "look": 0.2, "perfect": 0.2}
}

baris_delays = {
    0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 3.0
}

double_lines_at = [6,7 , 8]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_char_with_love_once(char, col, love_row=2, text_row=3):
    sys.stdout.write(f"\033[{love_row};1H{' ' * term_width}")
    sys.stdout.write(f"\033[{love_row};{col}H❤️")
    sys.stdout.write(f"\033[{text_row};{col}H{char}")
    sys.stdout.flush()

def print_line_at_position(line, line_index, love_row=2, text_row=3):
    col = 1
    word_buffer = ""
    line += " "

    for char in line:
        word_buffer += char
        if char == " ":
            word_clean = word_buffer.strip().lower()

            delay = TEXT_SPEED
            if line_index in slow_per_baris:
                delay = slow_per_baris[line_index].get(word_clean, delay)
            else:
                delay = slow_words.get(word_clean, delay)

            for c in word_buffer:
                print_char_with_love_once(c, col, love_row, text_row)
                col += 1
                time.sleep(delay)

            if line_index in pause_per_baris:
                for key, d in pause_per_baris[line_index].items():
                    if key in word_clean:
                        time.sleep(d)

            for key, d in pause_words.items():
                if key in word_clean:
                    time.sleep(d)

            word_buffer = ""

def animate_lyrics(lyrics):
    i = 0
    while i < len(lyrics):
        if i in double_lines_at and i + 1 < len(lyrics):
            clear()
            print_line_at_position(lyrics[i], i, love_row=2, text_row=3)
            time.sleep(baris_delays.get(i, 1.5))
            print_line_at_position(lyrics[i+1], i+1, love_row=4, text_row=5)
            time.sleep(baris_delays.get(i+1, 1.5))
            i += 2  
        else:
            clear()
            print_line_at_position(lyrics[i], i, love_row=2, text_row=3)
            time.sleep(baris_delays.get(i, 1.5))
            i += 1

clear()
sys.stdout.write("\033[?25l")  
sys.stdout.flush()
print("\n")
try:
    animate_lyrics(lyrics)
finally:
    sys.stdout.write("\033[?25h")  
    sys.stdout.flush()