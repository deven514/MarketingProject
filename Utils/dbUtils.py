import mysql.connector
import Utils.getEnvSettings
import warnings



def dbConnection():
    dbHost = 'localhost'
    dbUser = Utils.getEnvSettings.getEnvironmentVariable("DBUSER")
    dbPassword = Utils.getEnvSettings.getEnvironmentVariable("DBPWD")
    if (dbUser == None or dbPassword == None):
        raise Exception("Database Information not set")
    db = 'sentiment_analysis'
    try:
        mydb = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword,database=db)  #Connect to the database
        if(mydb):
            return mydb
    except Exception as e:
        return {"Error 001":  "Cannot connect to the Database.  Please contact your system administrator."}



def execStatement(dbConnection, sqlQuery):
    dbCursor = dbConnection.cursor()
    dbCursor.execute(sqlQuery)
    return dbCursor

def callStoredProc(procName, args = None ):
    warnings.filterwarnings("ignore")
    connection = dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        rows = []
        cursor = connection.cursor()
        if (args == None):
            cursor.callproc(procName)
        else:
            cursor.callproc(procName, args)
        for result in cursor.stored_results():
            rows.append(result.fetchall())
        cursor.close()
        connection.close()
        return rows[0]




def callStoredUpdateProc(procName, args):
    warnings.filterwarnings("ignore")
    connection = dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        cursor = connection.cursor()
        cursor.callproc(procName, args)
        row = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()
        return row

