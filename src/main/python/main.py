"""
Main script for the app neuroPsyPatientManager
"""
from PySide2 import QtCore, QtGui
from fbs_runtime.application_context.PySide2 import ApplicationContext

import sys
import logging

from package.main_window import MainWindow

lockfile = QtCore.QLockFile(QtCore.QDir.tempPath() + '/neuroPsyPatientManager.lock')


class AppContext(ApplicationContext):

    def run(self):
        self.window = MainWindow(ctx=self)
        self.window.setMinimumSize(560, 800)
        self.window.show()
        self.window.resize(560, 800)
        return self.app.exec_()


if __name__ == '__main__':
    try:
        if lockfile.tryLock(100):
            appctxt = AppContext()
            appctxt.run()
        else:
            logging.info("Application is already running")
    except Exception as e:
        import traceback

        print(f"My error e is : {e}")
        print(traceback.format_exc())
        input("Appuyez sur une touche pour continuer ...")
