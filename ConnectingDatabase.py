import mysql.connector
import mysql.cursor;
#Connecting and operating MySQL database#
class ConnectionMySQL:
    def __init__(self,user_name='root',host_name='localhost',passwrd=None,DB_name=None):
        self.user=user_name
        self.host=host_name
        self.password=passwrd
        self.db=DB_name

    #Connecting mysql,return cursor#
    def connect_mysql(self):
        DB=mysql.connector.connect(user=self.user,password=self.password,database=self.db,host=self.host)
        cursor=DB.cursor()
        return cursor
    
    #Write kols' profile#
    def write_profile(self,cursor,tablename,field,COLUMN,values,path=None,file_name=None):
        if path||file_name is None:
            print "Please choose a file and its location"
        else with open('/'.join([path,file_name]),'r') as json_file:
            data=json.load(json_file)
            TABLE=''.join([tablename,COLUMN])
            VALUE=''.join(['VALUES(',values,')'])
            cursor.execute(''.join(["DROP TABLE IF EXISTS ",tablename]))
            cursor.execute(''.join(["CREATE TABLE ",tablename,field]))
            cursor.execute(''.join(["INSERT INTO ",TABLE,' ',VALUE]))
    
    #Write KOL's article from an arbitrary json file#
    def write_article(self,cursor,tablename,field,COLUMN,values,path=None,file_name=None):
        if path||file_name is None:
            print "Please choose a file and its location"
        else if tablename is None:
            print "Please enter table name"
        else with open('/'.join([path,file_name]),'r')) as json_file:
            data=json.load(json_file)
            TABLE=''.join([tablename,COLUMN])
            VALUE=''.join(['VALUES(',values,')'])
            cursor.execute(''.join(["DROP IF EXISTS ",tablename]))
            cursor.execute(''.join(["CREATE TABLE",tablename,field]))
            cursor.execute(''.join(["INSERT INTO ",TABLE,' ',field,VALUE]))
    
    #Extract an arbitrary value from a given table with name provided#
    #tablename is the table which u wanna extract value#
    #value is a list contains what u wanna extract from tablename#
    #name is who u wanna get related information#
    def extract_value(self,cursor,tablename=None,name=None,value=None):
        if name is None:
            print "Please choose a KOL"
        else if tablename is None:
            print "Please choose a table"
        else:
            cursor.execute(''.join(["SELECT ",','.join(value),"FROM ",tablename,"WHERE name=",name]))
        return cursor.fetchall()
    
    def extract_all_value(self,cursor,tablename=None,name=None,value=None):
        if name is None:
            print "Please choose a KOL"
        else if tablename is None:
            print "Please choose a table"
        else:
            cursor execute(''.join(["SELECT",','.join(value),"FROM ",tablename]))
        return cursor.fetchall()

    #Close connection with mysql#
    def close_connection(self):
        self.db.close()