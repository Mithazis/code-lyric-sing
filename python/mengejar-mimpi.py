import time
import os
import sys

TEXT_SPEED = 0.001
term_width = 70
INDENT = 2

lyrics = [
    "Walau hanya mengejar mimpi wo-wo",

    "Meskipun engkau telah pergi",
    "Mungkin takkan kembali",
    "Aku di sini, tetap di sini, Sayangku",
    "Aku masih rindu padamu",
    "Aku masih sayang padamu",
    "Meski kini cintamu bukan aku"
]

pause_words = {}

pause_per_baris = {
    0: {
        "walau":0.5, "mimpi": 2, "wo-wo": 1.3
    },
    1: {
        "pergi": 0.7,
    },
    2: {
        "kembali": 0.7,
    },
    3: {
        "sini,": 0.1, "sayangku": 1.5
    },
    4: {
        "padamu": 0.7,
    },
    5: {
        "padamu": 0.7,
    },
    6: {
        "aku": 3,
    },
}

slow_words = {}

slow_per_baris = {
     0: {
        "walau": 0.1, "mimpi": 0.3
    },
    1: {
        "engkau": 0.02,
    },
    2: {
        "takkan": 0.02,
    },
    3: {
        "sayangku": 0.1
    },
    4: {
        "masih": 0.002,
    },
    5: {
        "masih": 0.02,
    },
    6: {
        "kini": 0.01, "bukan": 0.03
    },
}

baris_delays = {i: 0.0 for i in range(len(lyrics))}
double_lines_at = [2,3, 4]
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
        drop_tear(love_col, start_row=love_row + 1, end_row=love_row + 2)
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

def print_typing_line(text, row=10, col=1, speed=0.03):
    for i, char in enumerate(text):
        sys.stdout.write(f"\033[{row};{col + i}H{char}")
        sys.stdout.flush()
        time.sleep(speed)

def clear_footer(rows):
    for row in rows:
        sys.stdout.write(f"\033[{row};1H{' ' * term_width}")
    sys.stdout.flush()

def animate_lyrics(lyrics):
    i = 0
    while i < len(lyrics):
        heart_icon = "💔" if i < len(lyrics) - 1 else "💞"
        clear()

        if i == 0:
            print_typing_line(footer_line1, row=10)
            print_typing_line(footer_line2, row=11)
        else:
            sys.stdout.write(f"\033[10;1H{footer_line1}")
            sys.stdout.write(f"\033[11;1H{footer_line2}")
            sys.stdout.flush()

        if i in double_lines_at and i + 1 < len(lyrics):
            print_line_at_position(lyrics[i], i, love_row=1, text_row=3, heart=heart_icon)
            time.sleep(baris_delays.get(i, 1.5))
            print_line_at_position(lyrics[i + 1], i + 1, love_row=4, text_row=6, heart=heart_icon)
            time.sleep(baris_delays.get(i + 1, 1.5))
            i += 2
        else:
            print_line_at_position(lyrics[i], i, love_row=1, text_row=3, heart=heart_icon)
            time.sleep(baris_delays.get(i, 1.5))
            i += 1


# Mulai program
clear()
sys.stdout.write("\033[?25l")  # Sembunyikan kursor
sys.stdout.flush()
print("\n")

footer_line1 = "Lagi belajar bahagia tanpa kamu,"
footer_line2 = "padahal dulu kamu alasan bahagianya.💔"

try:
    animate_lyrics(lyrics)
    time.sleep(1)
    clear_footer([10, 11])
finally:
    sys.stdout.write("\033[?25h")  # Tampilkan kembali kursor
    sys.stdout.flush()
