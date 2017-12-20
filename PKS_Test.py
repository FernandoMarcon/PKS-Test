from PKS_Kernel import core
import sys
import os
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from grafico import plot_cdf, plot_pdf
import pylab as pl

# get the directory of this script
path = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(os.path.join(path,"pks_window.ui"))[0]                 # Load the UI
 
class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.msgBox = QtWidgets.QMessageBox
        self.log_location = ''
        self.dic_frequencias = {}
        self.dic_poisson = {} 

        self.window = QtWidgets.QMainWindow()
        self.window.setGeometry(100, 100, 750, 600)
        self.pic = QtWidgets.QLabel(self.window)
        self.pic.setGeometry(0,0 , 800, 600)
        self.window.setWindowTitle("Cumulative Distribution Functions")
        
        self.pushButton_open.clicked.connect(self.showDialog)  # Bind the event handlers
        self.pushButton.clicked.connect(self.run)
        self.pushButton_showGraph.clicked.connect(self.showGraph)
        
    
    def showDialog(self, nexus_file_path):
             
        self.nexus_file_path, _filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Nexus File', 
                '.',
                "Nexus File (*.nexus *.nex)")
        print self.nexus_file_path
        self.lineEdit_open.setText(self.nexus_file_path)

    def get_inputs(self):
          
        percentage = 0
        confidence = 0

        if self.radioButton_90.isChecked():
            confidence = 0.90
        elif self.radioButton_95.isChecked():
            confidence = 0.95
        else:
            confidence = 0.99
            
        if self.radioButton_standard.isChecked():
            percentage = 30
        else:
            try:
                other = self.lineEdit_other.text()
                percentage = float(other)
            except:
                self.msgBox.warning(self,
                            "Warning",
                            "Please, set the percentage of trees to be analysed and press Start button again.")
                percentage = 30
        
        return percentage, confidence
    
    def showGraph(self):
        pixmap = QtGui.QPixmap(self.log_location + 'plot.png')
        self.pic.setPixmap(pixmap)
        self.window.show()
        
    def run(self, nexus_file_path):
        
        nexus_file_path = str(self.lineEdit_open.text())
        percentage, confidence = self.get_inputs()
        
        
        numberBestTrees, meanLnL, self.meanTree, self.log_location , varLnL, varTrees, D, testResult, criticalValue,observedMutations, expectedMutations, n = core(nexus_file_path, percentage, confidence)
        
        plot_p = plot_cdf(expectedMutations,observedMutations,self.meanTree,self.log_location)
        
        #Set all the values
        self.lineEdit_max.setText(str(meanLnL))
        self.lineEdit_mean.setText(str(varLnL))
        self.lineEdit_lambda.setText(str(self.meanTree))
        self.lineEdit_varMut.setText(str(varTrees))
        self.lineEdit_dValue.setText(str(D))
        self.lineEdit_conc.setText(testResult)
        self.lineEdit_TreeQuant.setText(str(numberBestTrees)+" ("+str(n)+")")
        self.critical_line.setText(str(criticalValue))
        
        
app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

