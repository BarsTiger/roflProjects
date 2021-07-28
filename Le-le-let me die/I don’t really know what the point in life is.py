import time, subprocess, sys, os

try:
    import vlc
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-vlc'])
    import vlc

toxin = vlc.MediaPlayer("https://github.com/BarsTiger/roflProjects/raw/master/files/toxin.mp3")
toxin.play()

time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(17)
print("Я...")
time.sleep(2)
print("Гуль")
time.sleep(1)
print("Ле ле лет ми дай")
time.sleep(0.5)

while True:
    i = 1000
    while i != 6:
        print(str(i) + " - 7 = " + str(i - 7))
        i -= 7
        time.sleep(0.01)
