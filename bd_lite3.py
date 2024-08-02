import sqlite3
import re


class Bd_lite3:


    def __init__(self):

        self.__conn = sqlite3.connect('data_words.db')
        self.__cur = self.__conn.cursor()
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS data_words(itemID INTEGER PRIMARY KEY NOT NULL, English TEXT, Russian TEXT, Percent REAL)''')          
    
    def close_bd(self):

        self.__cur.close()
   
    def isExists(self, en):

        self.__cur.execute('''SELECT * FROM data_words WHERE English == ?''', (en,))

        if self.__cur.fetchall() == []:

            return False
        
        return True
    
    def get_index_en_word(self, en):
            
            self.__cur.execute('''SELECT itemID FROM data_words WHERE English == ?''', (en,))        
            return self.__cur.fetchone()
    
    def get_answer_from_bd(self, text): 

        if re.compile(r'[A-Za-z]+').findall(text) != []:

            self.__cur.execute('''SELECT ItemID FROM data_words WHERE English LIKE ?''', (text,))
            Itemid_en = self.__cur.fetchone()            
            self.__cur.execute('''SELECT Russian, Percent FROM data_words WHERE ItemID LIKE ?''', (Itemid_en[0],))
            answer_ru = self.__cur.fetchall()
            return answer_ru, Itemid_en[0]
        
        if re.compile(r'[А-Яа-я]+').findall(text) != []:

            self.__cur.execute('''SELECT ItemID FROM data_words WHERE Russian LIKE ?''', (text,))
            Itemid_ru = self.__cur.fetchone()            
            self.__cur.execute('''SELECT English, Percent FROM data_words WHERE ItemID LIKE ?''', (Itemid_ru[0],))
            answer_en = self.__cur.fetchall()
            return answer_en, Itemid_ru[0]
        
        return

    def get_all_database(self, finder=""):

        if finder == "":

            self.__cur.execute('''SELECT * FROM data_words''')
            return self.__cur.fetchall()
        
        if re.compile(r'[A-Za-z]+').findall(finder) != []:

            self.__cur.execute('''SELECT * FROM data_words WHERE English LIKE ?''', (finder+"%",))
            return self.__cur.fetchall()
        
        if re.compile(r'[А-Яа-я]+').findall(finder) != []:

            self.__cur.execute('''SELECT * FROM data_words WHERE Russian LIKE ?''', (finder+"%",))
            return self.__cur.fetchall()
        
        return []
    
    def get_word_from_bd(self, lan, index):

        if lan == "English":

            self.__cur.execute('''SELECT English FROM data_words WHERE itemID == ?''', (index,))

        else:

            self.__cur.execute('''SELECT Russian FROM data_words WHERE itemID == ?''', (index,))

        return self.__cur.fetchall()
    
    def add_word_in_bd(self, en, ru):

        self.__cur.execute('''INSERT INTO data_words(English, Russian, Percent) VALUES (?, ?, ?)''',(en, ru, 0.01))              
        self.__conn.commit()         
        
    def update_word_in_bd(self, index, en, ru):

        self.__cur.execute('''UPDATE data_words SET English = ?, Russian = ? WHERE itemID == ?''', (en, ru, index))
        self.__conn.commit()

    def update_percent_in_bd(self, point, index):

        self.__cur.execute('''UPDATE data_words SET Percent = ? WHERE itemID == ?''', (point, index))
        self.__conn.commit()

    def delete_word_from_bd(self, index):

        self.__cur.execute('''DELETE FROM data_words WHERE itemID == ?''', (index,))
        self.__conn.commit()