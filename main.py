#国土地理院標高タイルの数値データのダウンロードと画像表示(https://www.kunihikokaneko.com/dblab/map/kokudo.html)を
#参考に、AsciiGridをmatplotlibで表示するプログラムを作ってみました。
# -*- coding: utf-8 -*-
import sys
import os.path
import glob
import configparser
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import QApplication, QEventLoop, QCursor
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from form import Ui_Dialog
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource

class Form(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        config = configparser.ConfigParser()
        config.read('AscPlot.ini')
        self.ui.LoadFilePath.setText(config['フォーム']['読み込みファイル'])
        self.ui.RowNum.setValue(int(config['フォーム']['行数']))
        self.ui.ColNum.setValue(int(config['フォーム']['列数']))
    def LoadFileSelect_Click(self):
        path = QFileDialog.getOpenFileName(None, "", "")[0]
        self.ui.LoadFilePath.setText(path)

    def reject(self):
        config = configparser.ConfigParser()
        config.read('AscPlot.ini')
        config['フォーム']['読み込みファイル'] = self.ui.LoadFilePath.text()
        config['フォーム']['行数'] = str(self.ui.RowNum.value())
        config['フォーム']['列数'] = str(self.ui.ColNum.value())
        with open('AscPlot.ini', 'w') as configfile:
            config.write(configfile)
        sys.exit(0)

    def exec(self):
        file = self.ui.LoadFilePath.text()

        if not (os.path.exists(file) and (os.path.isfile(file))):
            QtWidgets.QMessageBox.information(None, "エラー", "指定したファイル「" + file + "」が見つかりませんでした。", QMessageBox.Ok)
            return
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        try:
            Z = pd.read_table(file, sep=' ', header=None, skiprows=6, engine = 'python') #「Initializing from file failed」エラー回避のためengineにpython指定
            Z[Z == -9999] = np.nan
            X, Y = np.meshgrid(np.linspace(0,1,self.ui.RowNum.value()), np.linspace(0,1,self.ui.ColNum.value()))
            #2D表示
            plt.imshow(Z)
            plt.show()
            #3D表示
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z)
            plt.show()
            #3D表示 色付き
            ax = plt.axes(projection='3d')
            Z = Z.get_values()
            ls = LightSource()
            rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
            surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb, linewidth=0, antialiased=False, shade=False)
            plt.show()
        finally:
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(None, "終了", "終了しました。", QMessageBox.Ok)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())