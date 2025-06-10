import mysql.connector
import Utils.getEnvSettings




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





# connection = dbConnection()
# if (isinstance(connection, dict)):
#     print(connection)
# else:
#     print("Connection established")


