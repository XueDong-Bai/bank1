# -*- coding:utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('hello world')
    label.show()
    sys.exit(app.exec_())

    '''
    QTDesigner
program:D:\Dev\pycharm\workspace\bank1\venv\Lib\site-packages\PySide2\designer.exe
arguments:
working directory :$ProjectFileDir$
PyUIC
program:D:\Dev\pycharm\workspace\bank1\venv\Scripts\python.exe
arguments:$FileName$ -o $FileNameWithoutExtension$.py
working directory :$ProjectFileDir$

PyRcc
program:D:\Dev\pycharm\workspace\bank1\venv\Lib\site-packages\PySide2\pyside2-rcc.exe
arguments:$FileName$ -o $FileNameWithoutExtension$_rc.py
working directory :$ProjectFileDir$
    
    
    '''