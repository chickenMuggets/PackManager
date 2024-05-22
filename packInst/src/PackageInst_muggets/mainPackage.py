import os
class packageMan():
    def install(package,consCall, hasInput):
        if consCall == 1 or consCall == True:
            print('installing package ' + package)
            if hasInput == False or hasInput == 0:
                os.system('pip install ' + package)
            else:
                os.system('pip install ' + package + ' --no-input')
            print(package + ' installed successfully')
        if consCall == 0 or consCall == False:
            if hasInput == False or hasInput == 0:
                os.system('pip install ' + package + ' ' + '-q -q -q ')
            else:
                os.system('pip install ' + package + ' ' + '-q -q -q ' + '--no-input')
    def uninstall(package,consCall, hasInput):
        if consCall == 1 or consCall == True:
            print('uninstalling package ' + package)
            if hasInput == False or hasInput == 0:
                os.system('pip uninstall ' + package + ' -y')
            else:
                os.system('pip uninstall ' + package)
            print(package + ' uninstalled successfully')
        if consCall == 0 or consCall == False:
            if hasInput == False or hasInput == 0:
                os.system('pip uninstall ' + package + ' ' + '-q -q -q ' + '-y')
            else:
                os.system('pip uninstall ' + package + ' ' + '-q -q -q ')

packageMan.install('numpy',0,0)
packageMan.uninstall('numpy',0,0)