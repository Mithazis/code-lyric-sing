#  cara menjalankan 
#  pastikan sudah install python
#  tinggal click kanan kemudian run python
#  atau buka terminal kemudian copas : python Indah_cintaku.py


import time
import os
import sys
import threading


TEXT_SPEED = 0.07  # Kecepatan huruf muncul (semakin kecil, semakin cepat)

# Lirik lagu
lyrics = [
    "Sudahkah kau yakin untuk mencintaiku",
    "Ku ingin hanya satu tuk selamanya",
    "Kutak melihat dari sisi sempurnamu",
    "Tak perduli kelemahanmu",
    "Yang ada aku jatuh cinta karena hatimu",
    
    "Cintaku tak pernah memandang siapa kamu",
    "Tak pernah menginginkan kamu lebih",
    "Dari apa adanya dirimu selalu",
    
    "Cintaku terasa sempurna karena hatimu",
    "Selalu menerima kekuranganku",
    "Sungguh indah cintaku ❤️"
]

# Jeda antar baris (detik), sesuai indeks baris
baris_delays = {
    0: 0.0,
    1: 0.0,
    2: 0.0,
    3: 0.0,
    4: 0.0,
    5: 0.0,
    6: 0.0,
    7: 0.0,
    8: 0.0,
    9: 0.0,
    10: 0.0 
}

# Kata-kata yang selalu punya delay (di baris manapun)
pause_words = {
    "yakin": 1.4,
    "kutak": 1.0,
    "aku": 1.0,
    "selamanya": 1.0,
    "sempurnamu": 1.0,
    "kelemahanmu": 1.8,
    "cinta": 1.5,
    "lebih": 1.5,
    "dirimu" : 1.5,
    "kekuranganku": 1.5
}

# Kata-kata yang muncul lambat
slow_words = {
    "sudahkah": TEXT_SPEED * 1.5,
    "mencintaiku": TEXT_SPEED * 1.5,
    "selamanya": TEXT_SPEED * 3,
    "kutak": TEXT_SPEED * 4,
    "melihat": TEXT_SPEED * 1.5,
    "sempurnamu": TEXT_SPEED * 1.2,
    "perduli": TEXT_SPEED * 1.2,
    "kelemahanmu": TEXT_SPEED * 3,
    "aku": TEXT_SPEED * 2.5,
    "jatuh": TEXT_SPEED * 2.5,
    "cintaku": TEXT_SPEED * 3,
    "memandang": TEXT_SPEED * 1.5,
    "kamu": TEXT_SPEED * 3,
    "menginginkan": TEXT_SPEED * 1.5,
    "lebih": TEXT_SPEED * 2.0,
    "selalu": TEXT_SPEED * 1.5,
    "hatimu": TEXT_SPEED * 2,
    "adanya": TEXT_SPEED * 3,
    "dirimu": TEXT_SPEED * 2.5,
    "sempurna": TEXT_SPEED * 2,
    "kekuranganku": TEXT_SPEED * 2.5
}

# Delay hanya untuk kata tertentu di baris tertentu

pause_per_baris = {
    2: {  # Baris ke-3
        "dari": 1.2
    },
    4: { 
        "hatimu": 0.1
    },
    5: {
        "kamu": 1.5,
        "cintaku": 0.005
    },
    7: {
        "selalu": 1.0
    },
    8: {
        "cintaku": 0.005,
        "hatimu": 2.2
    },
    10: {
        "❤️": 1
    }
}

term_width = 45

love_active = True

def love_animation():
    pos = 0
    direction = 1
    while love_active:
        sys.stdout.write("\033[s")
        sys.stdout.write("\033[1;1H")
        bar = " " * pos + "❤️" + " " * (term_width - pos)
        sys.stdout.write(bar[:term_width])
        sys.stdout.write("\033[u")        
        sys.stdout.flush()

        pos += direction
        if pos >= term_width - 2 or pos <= 0:
            direction *= -1
        time.sleep(0.05)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_char_by_char(text, slow=None):
    delay = slow if isinstance(slow, float) else TEXT_SPEED
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def animate_lyrics(lyrics):
    for i, line in enumerate(lyrics):
        sys.stdout.write("\033[3;1H")
        sys.stdout.write(" " * term_width)
        sys.stdout.write("\033[3;1H")
        sys.stdout.flush()

        sys.stdout.write("   ")

        words = line.split()
        for word in words:
            word_lower = word.lower()

            slow_delay = None
            for slow_key in slow_words:
                if slow_key in word_lower:
                    slow_delay = slow_words[slow_key]

            print_char_by_char(word + " ", slow=slow_delay)

            if i in pause_per_baris:
                for key_word, key_delay in pause_per_baris[i].items():
                    if key_word in word_lower:
                        time.sleep(key_delay)

            for pause_key in pause_words:
                if pause_key in word_lower:
                    time.sleep(pause_words[pause_key])

        print()
        time.sleep(baris_delays.get(i, 1.5))


clear()
love_thread = threading.Thread(target=love_animation)
love_thread.daemon = True
love_thread.start()

try:
    animate_lyrics(lyrics)
finally:
    love_active = False
    time.sleep(0.5)
    clear()