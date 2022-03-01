import os

print('writing files')

for dir in [x[0] for x in os.walk(os.getcwd())]:
    print('writing кабанчик into ' + dir)
    try:
        open(dir + '/кабанчик.mp4', 'a+').close()
    except:
        print('failed. skipped.')

print('done')
input('press enter to exit...')
