import subprocess
import sys
import os
os.system('python helloshell.py')
output = os.popen('python helloshell.py').read()
subprocess.call(' python printCMD.py')
subprocess.call('cmd /C "type printCMD.py"')
subprocess.call('type printCMD.py', shell=True)#shell  для винды ,но как на линуксе вообще непонятно ,не пашет.
exam = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
exam.communicate()
exam.returncode
exam = subprocess.Popen('python printCMD.py', stdout=subprocess.PIPE)#open file , emulition
exam.stdout.read()
exam.wait()# close of file
subprocess.Popen('python printCMD.py', stdout=subprocess.PIPE).communicate()[0]
os.system('start printCMD.py')#start in python(Pycharm)
os.system('start printCMD.py arg arg')#для параллельной работы ??
os.startfile('test.html')# start in yandex
os.startfile('printCMD.py')# pycharm
"""os.system иной раз блокирует вызывающую программу для параллельгой лучше выше смотреть """
'''os.popen тоже иной раз блокирует'''
for line in os.popen('dir *.py'): print(line,end='')
'''os.popen -c итератором но без next'''
os.chdir('lesson')
print('my os.getcwd()=>', os.getcwd())
print('my sys.path=>', sys.path[:6])
input()
>set PYTHONPATH=C:\lesson\предметные_уроки\Os_и_Python #set - добовляет путь в путь пайтона.
python C:\...\PP4E\Tools\find.py *.cxx C:\PP4thEd\Examples\PP4E# запуск файлов из одного каталога,которые будут работать в другом каталоге.
os.environ.keys()
Точно так же этот механизм действует и в Linux. Вообще говоря, порождаемая программа всегда наследует значения переменных окружения от своих родителей. Порожденными программами являются такие,
которые запускаются средствами Python, например os.spawnv, комбинацией os.fork/exec в Unix-подобных системах, и os.popen, os.system или
с помощью модуля subprocess на ряде других платформ. Все программы,
запущенные таким способом, получают значения переменных окружения, существующие в момент запуска в родительском процессе.1

os.environ['TEMP']-показывает путь в
Еще на заре эпохи компьютеров программисты поняли, что могут воспользоваться такой неиспользуемой вычислительной мощностью, выполняя одновременно несколько программ. Если распределить процессорное время среди множества задач, его мощность не будет тратиться впустую, пока некоторая конкретная задача ждет осуществления внешнего события. Такая технология обычно называется параллельной обработкой (или, иногда, «мультиобработкой» или даже «многозадачностью»), потому что возникает впечатление одновременного выполнения
нескольких заданий параллельно во времени.

