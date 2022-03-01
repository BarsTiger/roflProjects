import os

print("Cabanchik remover by BarsTiger")
input("Do you REALLY want to remove all cabanchik's from this folder? Press enter to continue or CTRL+C to cancel.")
print('removing files')

for dir in [x[0] for x in os.walk(os.getcwd())]:
    print('removing кабанчик from ' + dir)
    for file in os.listdir(dir):
        if file == 'кабанчик.mp4':
            try:
                os.remove(os.path.join(dir, file))
            except:
                print('failed. skipped.')

print('done')
input('press enter to exit...')
