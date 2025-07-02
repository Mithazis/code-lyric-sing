#  cara menjalankan 
#  pastikan sudah install python
#  tinggal click kanan kemudian run python
#  atau buka terminal kemudian copas : you-ill-be-in-my-heart.py


import time
import os
import sys

TEXT_SPEED = 0.07

lyrics = [
    "Don't listen to them 'Cause what do they know",
    "We need each other, to have, to hold",
    "They'll see in time, I know",
    
    "When destiny calls you, you must be strong",
    "I may not be with you",
    "But you've got to hold on",
    "They'll see in time, I know",
    "We'll show them together",
    
    "cause you'll be in my heart",
    "Yes you'll be in my heart",
    "From this day on",
    "Now and forever more"
]

term_width = 70
INDENT = 2

pause_words = { }

pause_per_baris = {
    0: {"them": 1, "know" : 1},
    1: {"other": 1, "hold": 0.5},
    2: {"time,": 3, "know":4},
    3: {"you,": 1, "strong": 1},
    4: {"you": 1},
    5: {"on": 1},
    6: {"time,": 3, "know":1.7},
    8: {"heart": 2},
    9: {"heart": 2},
    10: {"on": 1},
    11: {"more": 1}
}

slow_words = {}

slow_per_baris = {
    1: {"to": 0.1, "hold": 0.2},
    2: {"see": 0.1, "in": 0.1, "i": 0.2, "know": 0.2},
    3: {"strong": 0.1},
    6: {"i": 0.2, "know": 0.2},
    7: {"show": 0.1, "together": 0.1},
    8: {"be": 0.1, "in": 0.2, "my": 0.2, "heart": 0.1},
    9: {"be": 0.1, "in": 0.2, "my": 0.2, "heart": 0.1},
    10: {"this": 0.1, "day": 0.1, "on":0.1},
    11: {"forever": 0.2, "more": 0.2}
    }

baris_delays = {
    0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2
}

double_lines_at = [4,5, 10]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_char_with_love_once(char, col, love_row=2, text_row=3):
    sys.stdout.write(f"\033[{love_row};1H❤️")

    love_col = col + INDENT

    if love_col != 1:
        sys.stdout.write(f"\033[{love_row};2H{' ' * (term_width - 1)}")
        sys.stdout.write(f"\033[{love_row};{love_col}H❤️")

    sys.stdout.write(f"\033[{text_row};{love_col}H{char}")
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