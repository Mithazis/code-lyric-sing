#  cara menjalankan 
#  pastikan sudah install python
#  tinggal click kanan kemudian run python
#  atau buka terminal kemudian copas : python somebody-pleasure.py


import time
import os
import sys

TEXT_SPEED = 0.02
term_width = 70
INDENT = 2

lyrics = [
    "won lebih tu gatel loh",
    "laris soup yoooh",
    "gak lalap tuh oh uwis mekso",
    "deram najis sembari seplesoo",
    "ai oubes bicendi, en lain",
    "naik ayu su filem tigi sorakah",
    "bisa napi.. hapines",
    "kena gerah hapineees..",
    "aneh opo bi nen njelimet sorene ri",
    "ifen nih fel gatel arif kaum panik :v"
    ]

pause_words = {
    "loh": 0.6, "yoooh": 1, "mekso": 0.7, "seplesoo": 0.7, "oubes":0.7, "bicendi": 0.6, "lain": 0.5, "sorakah": 1.0, "napi": 1.2, "hapines": 0.3,
}

pause_per_baris = {
    8: {
        "ri": 0.1
    }
}

slow_words = {}

slow_per_baris = {
    1: {"yoooh": 0.2},
    2: {"mekso": 0.1},
    3: {"seplesoo": 0.1},
    4: {"bicendi": 0.2, "lain": 0.1},
    5: {"hapines": 0.1,},
    7: {"opo": 0.1, "bi":0.1, "njelimet": 0.2, "sorene": 0.1},
    7: {"waktunya": 0.2, "kan": 0.1, "datang": 0.3}
}

baris_delays = { i: 0.0 for i in range(8) }
baris_delays[ 0

]

double_lines_at = [0,1 , 2,3 , 6]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def drop_tear(col, start_row=1, end_row=2):
    for row in range(start_row, end_row + 1):
        sys.stdout.write(f"\033[{row};{col}H💧")
        sys.stdout.flush()
        time.sleep(0.05)
        sys.stdout.write(f"\033[{row};{col}H ")
        sys.stdout.flush()

def print_char_with_love_once(char, col, love_row=1, text_row=3, heart="💔"):
    sys.stdout.write(f"\033[{love_row};1H{heart}")

    love_col = col + INDENT

    if love_col != 1:
        sys.stdout.write(f"\033[{love_row};2H{' ' * (term_width - 1)}")
        sys.stdout.write(f"\033[{love_row};{love_col}H{heart}")
        drop_tear(love_col, start_row=love_row+1, end_row=love_row+2)

    sys.stdout.write(f"\033[{text_row};{love_col}H{char}")
    sys.stdout.flush()

def print_line_at_position(line, line_index, love_row=1, text_row=3, heart="💔"):
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
                print_char_with_love_once(c, col, love_row, text_row, heart)
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
        heart_icon = "💔" if i < len(lyrics) - 1 else "💞"
        if i in double_lines_at and i + 1 < len(lyrics):
            clear()
            print_line_at_position(lyrics[i], i, love_row=1, text_row=3, heart=heart_icon)
            time.sleep(baris_delays.get(i, 1.5))
            print_line_at_position(lyrics[i+1], i+1, love_row=4, text_row=6, heart=heart_icon)
            time.sleep(baris_delays.get(i+1, 1.5))
            i += 2
        else:
            clear()
            print_line_at_position(lyrics[i], i, love_row=1, text_row=3, heart=heart_icon)
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
