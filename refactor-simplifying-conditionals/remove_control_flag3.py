
def backdoor_srcmethod():
    while True:
        print( "Puts the Android Agent inside an Android App APK. The application runs normally, with extra functionality.")

        inputfile = input('APK to Backdoor: ').strip()

        if inputfile == '':
            return False

        print('doing other stuff.')

backdoor_srcmethod()
