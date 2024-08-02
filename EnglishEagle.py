import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow,QAbstractItemView
from PySide6 import QtCore, QtGui

from AllPages import Ui_MainWindow
import bd_lite3


class MainWindow(QMainWindow):

       
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bd = bd_lite3.Bd_lite3()

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)        
        
        self.init_main_page()
        self.init_add_words_page()
        self.init_edit_words_page()
        self.init_statistics_page()
        self.init_learn_page()
               
        self.show()

    def closeEvent(self, event):
        
        self.bd.close_bd()
       
#############################################     init      ########################################## 

    def init_main_page(self):
        
        self.ui.button1add.clicked.connect(self.bn_set_page_add)
        self.ui.button1edit.clicked.connect(self.bn_set_page_edit)
        self.ui.button1status.clicked.connect(self.bn_set_page_statistics)
        self.ui.button1learn.clicked.connect(self.bn_set_page_learn)
        self.ui.button1exit.clicked.connect(self.bn_go_out)
        
    def init_add_words_page(self):

        self.ui.button2back.clicked.connect(self.bn_back_from_add_page)
        self.ui.button2addword.clicked.connect(self.bn_add_word_add_page)
        self.ui.lineEdit2addEnglish.setMaxLength(45)
        self.ui.lineEdit2addRussian.setMaxLength(50)
        self.ui.lineEdit2addEnglish.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[a-z \- \']{100}")))
        self.ui.lineEdit2addRussian.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[а-я \- \']{100}")))
        self.ui.label2green_mark.hide() 

    def init_edit_words_page(self):

        self.ui.button3back.clicked.connect(self.bn_back_from_edit_page)
        self.ui.button3change.clicked.connect(self.bn_change_word_edit_page)
        self.ui.button3delete.clicked.connect(self.bn_delete_word_edit_page)
        self.ui.button3save.clicked.connect(self.bn_save_word_edit_page)
        self.ui.lineEdit3reEnglish.setMaxLength(45)
        self.ui.lineEdit3reRussian.setMaxLength(50)
        self.ui.lineEdit3find.setMaxLength(50)
        self.ui.lineEdit3reEnglish.setReadOnly(True)
        self.ui.lineEdit3reRussian.setReadOnly(True)
        self.ui.lineEdit3reEnglish.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[a-z \- \']{100}")))
        self.ui.lineEdit3reRussian.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[а-я \- \']{100}")))
        self.ui.lineEdit3find.textEdited.connect(self.refresh_list_of_edit_page)

    def init_statistics_page(self):

        self.ui.button4back.clicked.connect(self.bn_back_from_statistic_page)
        self.ui.lineEdit4find.setMaxLength(50)
        self.ui.lineEdit4find.textEdited.connect(self.refresh_list_of_statistic_page)
        self.ui.listWidget4status.setSelectionMode(QAbstractItemView.NoSelection)

    def init_learn_page(self):

        self.ui.button5check.clicked.connect(self.bn_check_word_learn_page)
        self.ui.button5finish.clicked.connect(self.bn_back_from_learn_page)
        self.ui.lineEdit5translate.setMaxLength(50)

################################################     timers      ########################################

    def timer_of_bn_set_learn_page(self):

        self.ui.button1add.setStyleSheet("background-color:")

    def red_timer_of_bn_add_word_add_page(self):

        self.ui.lineEdit2addEnglish.setStyleSheet("border:")
        self.ui.lineEdit2addRussian.setStyleSheet("border:")
        self.ui.label2message.setText("")

    def green_timer_of_bn_add_word_add_page(self):

        self.ui.lineEdit2addEnglish.setStyleSheet("border:")
        self.ui.lineEdit2addRussian.setStyleSheet("border:") 
        self.ui.label2green_mark.hide()
        self.ui.lineEdit2addEnglish.clear()
        self.ui.lineEdit2addRussian.clear()

    def green_timer_of_bn_save_word_edit_page(self):

        self.ui.lineEdit3reEnglish.setStyleSheet("border:")
        self.ui.lineEdit3reRussian.setStyleSheet("border:")        
        self.ui.lineEdit3reEnglish.setReadOnly(True)
        self.ui.lineEdit3reRussian.setReadOnly(True)

    def red_timer_of_bn_save_word_edit_page(self):

        self.ui.lineEdit3reEnglish.setStyleSheet("border:")
        self.ui.lineEdit3reRussian.setStyleSheet("border:")
        
    def red_timer_of_bn_check_word_learn_page(self):

        self.ui.lineEdit5translate.setStyleSheet("border:")
    
    def green_timer_of_bn_check_word_learn_page(self):

        self.ui.lineEdit5translate.setStyleSheet("border:")
        self.ui.lineEdit5translate.setReadOnly(False)
        self.ui.lineEdit5translate.clear()
        self.generate_new_word_learn_page()
        self.ui.lineEdit5translate.setFocus()
 
#################################################    main_page   #############################################
        
    def bn_set_page_add(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAdd)
        self.ui.lineEdit2addEnglish.setFocus()

    def bn_set_page_edit(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageEdit)
        self.refresh_list_of_edit_page()
        self.ui.listWidget3_showdata.setCurrentRow(0)
        self.ui.lineEdit3find.setFocus()

    def bn_set_page_statistics(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageStatus)
        self.refresh_list_of_statistic_page()        
        self.ui.lineEdit4find.setFocus()

    def bn_set_page_learn(self):

        if self.bd.get_all_database() == []:  

            if self.ui.button1add.styleSheet() != "background-color: #c095e4":

                QtCore.QTimer.singleShot(1000, self.timer_of_bn_set_learn_page) 

            self.ui.button1add.setStyleSheet("background-color: #c095e4")
            return
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLearn)
        self.generate_new_word_learn_page()

    def bn_go_out(self):

        app.quit()
                
##########################        pageADD            ##########################################################
    
    def bn_back_from_add_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)
        self.ui.lineEdit2addEnglish.clear()
        self.ui.lineEdit2addRussian.clear()

    def bn_add_word_add_page(self):
        
        self.en = self.ui.lineEdit2addEnglish.text().strip()
        self.ru = self.ui.lineEdit2addRussian.text().strip()

        if self.ui.lineEdit2addEnglish.text() == "" or self.ui.lineEdit2addRussian.text() == "" or self.ui.lineEdit2addEnglish.text().isspace() \
                                                    or self.ui.lineEdit2addRussian.text().isspace() or self.bd.isExists(self.en):
            
            self.ui.lineEdit2addEnglish.clear()
            self.ui.lineEdit2addRussian.clear() 

            if self.ui.lineEdit2addEnglish.styleSheet() != "border: 1px solid #FF0000":   

                QtCore.QTimer.singleShot(1000, self.red_timer_of_bn_add_word_add_page)  

            self.ui.lineEdit2addEnglish.setStyleSheet("border: 1px solid #FF0000")                       
            self.ui.lineEdit2addRussian.setStyleSheet("border: 1px solid #FF0000")

            if self.bd.isExists(self.en):

                self.ui.label2message.setText("Already added")     
                      
            return
                
        self.ui.lineEdit2addEnglish.setStyleSheet("border: 1px solid #00CC00")
        self.ui.lineEdit2addRussian.setStyleSheet("border: 1px solid #00CC00")
        self.ui.label2green_mark.show()        
        self.bd.add_word_in_bd(self.en, self.ru)            
        QtCore.QTimer.singleShot(1000, self.green_timer_of_bn_add_word_add_page)      

############################    pageEDIT    ####################################################################

    def refresh_list_of_edit_page(self):

        self.ui.listWidget3_showdata.clear()        
        search_word_edit_page = self.ui.lineEdit3find.text().strip().lower()        
        new_list = []

        for list_from_bd in self.bd.get_all_database(search_word_edit_page):    
                    
            new_list.append(f'{list_from_bd[1]:14} - {list_from_bd[2]}')   

        new_list.sort()
        self.ui.listWidget3_showdata.addItems(new_list)

    def bn_change_word_edit_page(self):

        if self.ui.listWidget3_showdata.count() != 0 and self.ui.listWidget3_showdata.currentRow() != (-1):

            en_word = self.ui.listWidget3_showdata.currentItem().text().split(" - ")[0].strip()
            ru_word = self.ui.listWidget3_showdata.currentItem().text().split(" - ")[1].strip()
            self.ui.lineEdit3reEnglish.setText(en_word)
            self.ui.lineEdit3reRussian.setText(ru_word)
            self.ui.lineEdit3reEnglish.setReadOnly(False)
            self.ui.lineEdit3reRussian.setReadOnly(False)
            return
                
        return
    
    def get_en_word_from_lineEdit3reEnglish_edit_page(self):

        if self.ui.listWidget3_showdata.count() != 0 and self.ui.listWidget3_showdata.currentRow() != (-1):

            return self.ui.listWidget3_showdata.currentItem().text().split(" - ")[0].strip()
        
        return
        
    def bn_delete_word_edit_page(self):
        
        if self.ui.listWidget3_showdata.count() != 0 and self.ui.listWidget3_showdata.currentRow() != (-1):

            currow = self.ui.listWidget3_showdata.currentRow()
            enWordEditPage = self.ui.listWidget3_showdata.currentItem().text().split(" - ")[0].strip()            
            self.bd.delete_word_from_bd(self.bd.get_index_en_word(enWordEditPage)[0])
            
            self.refresh_list_of_edit_page()

            if currow == 0:

                self.ui.listWidget3_showdata.setCurrentRow(currow)

            else:

                self.ui.listWidget3_showdata.setCurrentRow(currow - 1)

            self.ui.lineEdit3reEnglish.clear()
            self.ui.lineEdit3reRussian.clear()
            self.ui.lineEdit3reEnglish.setReadOnly(True)
            self.ui.lineEdit3reRussian.setReadOnly(True)

        return
    
    def bn_save_word_edit_page(self):
        
        if not self.ui.lineEdit3reEnglish.isReadOnly():

            if self.ui.lineEdit3reEnglish.text() == "" or self.ui.lineEdit3reRussian.text() == "" or self.ui.lineEdit3reEnglish.text().isspace() \
                                                    or self.ui.lineEdit3reRussian.text().isspace():    
                           
                if self.ui.lineEdit3reEnglish.styleSheet() != "border: 1px solid #FF0000": 
                                  
                    QtCore.QTimer.singleShot(1000, self.red_timer_of_bn_save_word_edit_page)

                self.ui.lineEdit3reEnglish.setStyleSheet("border: 1px solid #FF0000")                       
                self.ui.lineEdit3reRussian.setStyleSheet("border: 1px solid #FF0000") 
                return
                        
            en_word = self.ui.lineEdit3reEnglish.text().strip()
            ru_word = self.ui.lineEdit3reRussian.text().strip()            
            index = self.bd.get_index_en_word(self.get_en_word_from_lineEdit3reEnglish_edit_page())[0]
            self.bd.update_word_in_bd(index, en_word, ru_word)            
            currow = self.ui.listWidget3_showdata.currentRow()
            self.refresh_list_of_edit_page()            
            self.ui.lineEdit3reEnglish.setStyleSheet("border: 1px solid #00CC00")
            self.ui.lineEdit3reRussian.setStyleSheet("border: 1px solid #00CC00")
            self.ui.lineEdit3reEnglish.clear()
            self.ui.lineEdit3reRussian.clear()
            QtCore.QTimer.singleShot(1000, self.green_timer_of_bn_save_word_edit_page)            
            self.ui.listWidget3_showdata.setCurrentRow(currow)            
            
        return
    
    def bn_back_from_edit_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)              
        self.ui.lineEdit3find.clear()
        self.ui.lineEdit3reEnglish.clear()
        self.ui.lineEdit3reRussian.clear()
        self.ui.lineEdit3reEnglish.setReadOnly(True)
        self.ui.lineEdit3reRussian.setReadOnly(True)

############################    pageSTATISTICS  #######################################################

    def refresh_list_of_statistic_page(self):

        self.ui.listWidget4status.clear()
        search_word_statistic_page = self.ui.lineEdit4find.text().strip().lower()
        new_list = []

        for list_from_bd in self.bd.get_all_database(search_word_statistic_page):  

            new_list.append(f'{list_from_bd[1]:14} - {list_from_bd[2]:14} - {list_from_bd[3]:.0%}') 

        new_list.sort()
        self.ui.listWidget4status.addItems(new_list)

    def bn_back_from_statistic_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)
        self.ui.lineEdit4find.clear()

#############################  pageLEARN    ##########################################################

    def generate_new_word_learn_page(self):

        list_weight = [] 
        list_id = [] 

        for list_from_bd in self.bd.get_all_database():   

            list_weight.append(100 - list_from_bd[3] * 100)
            list_id.append(list_from_bd[0])

        word_id = random.choices(list_id, weights=list_weight, k =1)
        language = random.choices(["English", "Russian"])
        self.ui.label5word.setText(self.bd.get_word_from_bd(language[0], word_id[0])[0][0])

    def bn_check_word_learn_page(self):
        
        if self.ui.button5check.text() == "Проверить":
            
            if self.ui.lineEdit5translate.text() == "" or self.ui.lineEdit5translate.text().isspace():    
                             
                    if self.ui.lineEdit5translate.styleSheet() != "border: 1px solid #FF0000":

                        self.ui.lineEdit5translate.clear()
                        QtCore.QTimer.singleShot(1000, self.red_timer_of_bn_check_word_learn_page)

                    self.ui.lineEdit5translate.setStyleSheet("border: 1px solid #FF0000")
                    self.ui.lineEdit5translate.setFocus()                
                    return      

            answer, answer_id = self.bd.get_answer_from_bd(self.ui.label5word.text())  

            if self.ui.lineEdit5translate.text().strip() == answer[0][0]:

                self.ui.lineEdit5translate.setStyleSheet("border: 1px solid #00CC00") 
                self.ui.lineEdit5translate.setReadOnly(True)                
                num_percent = answer[0][1]

                if num_percent < 1:

                    num_percent += 0.01 

                self.bd.update_percent_in_bd(num_percent, answer_id) 
                QtCore.QTimer.singleShot(500, self.green_timer_of_bn_check_word_learn_page)                
                return
            
            else:

                self.ui.lineEdit5translate.setStyleSheet("border: 1px solid #FF0000") 
                QtCore.QTimer.singleShot(1000, self.red_timer_of_bn_check_word_learn_page)               
                self.ui.lineEdit5translate.setReadOnly(True)                
                self.ui.lineEdit5translate.setText(answer[0][0])
                self.ui.label5message.setText("Correct answer")
                num_percent = answer[0][1]

                if num_percent > 0.03:

                    num_percent -= 0.02

                self.bd.update_percent_in_bd(num_percent, answer_id)
                self.ui.button5check.setText("Далее")
                return
            
        else:

            self.ui.label5message.setText("")
            self.ui.lineEdit5translate.setReadOnly(False)
            self.ui.lineEdit5translate.setStyleSheet("border:")
            self.ui.lineEdit5translate.clear()
            self.ui.button5check.setText("Проверить")
            self.ui.lineEdit5translate.setFocus()
            self.generate_new_word_learn_page()

    def bn_back_from_learn_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)
        self.ui.lineEdit5translate.clear()
        self.ui.button5check.setText("Проверить")
        self.ui.label5message.setText("")
        self.ui.lineEdit5translate.setReadOnly(False)

#####################################################################################################

if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = MainWindow()      
    sys.exit(app.exec())