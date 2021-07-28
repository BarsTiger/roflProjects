import time, subprocess, sys

try:
    import vlc
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'vlc'])
    import vlc

toxin = vlc.MediaPlayer("http://your_mp3_url")
toxin.play()

time.sleep(16)
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
