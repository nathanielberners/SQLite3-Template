#!/bin/python

#   SQLite3 Template - program stub for developing SQLite3 backed programs.
#   Uses path checking, database checking and error handling.
#   Supports user access limiting (free-for-all unless one or more usernames are configured).
#
#   Written by Nathaniel Berners - nathanieljb@pm.me
#
#   Error handling is provided by the function errors(). It's use is thus:
#       errors( errnum, erritem, errmessage, dbconn, errexit )
#           errnum - is the error number to report (to assist in bug hunting); manually defined or None
#           erritem - is the item for which the error is called, or None
#           errmessage - provide a message to print on error
#           dbconn - The SQLite3 database connection object, or None
#           errexit - an integer to trigger an exit: 0 = continue program, >=1 = exit
#
#   User access is controlled with the userNames([]) tuple. If empty, the program will run for anyone.
#       Supply a system login username as a tuple element to enable access control.

### CONFIGURATION ###########################################################################################

# Tuples - immutable configurations
programName = ( [ "SQLite3 Template" ] )  # The name of the program
dataPath    = ( [ "sqlite3template" ] )  # Path to data directory
fileDepends = ( [ "sqlite3template.db" ] )  # Files required to run, first tuple MUST be the SQLite3 db file
dbTables    = ( [ "sqlite3template" ] )  # Table names used in the SQLite3 databse
userNames   = ( [  ] )  # Add an OS login username (or more) to control access

### CHECKS AND INIT #########################################################################################

# Initial Imports
import  os, sys

# Expand paths
fullPath = ( [ os.path.expanduser( dataPath[ 0 ] + "/" ) ] )

# Define error handling function
def errors( errnum, erritem, errmessage, dbconn, errexit ):
    if errnum:
        print( "!!! Error " + errnum + ": ", end="" )
    print( erritem + errmessage )
    if dbconn == True:
        dbConn.close()
    if errexit != 0:
        sys.exit( 1 )

# Terminal clearing
def clearTerm():
    os.system( "cls||clear" )
    if len( programName ) != 0:
        header = programName[ 0 ]
    else:
        header = "Sqlite3 Program"
    print( header + "\n" )
clearTerm()

# Check permissions if userNames tuple is populated
if len( userNames ) >= 1:
    getUser = os.getlogin()
    if not getUser in userNames:
        errors( "1", "", "Permission denied to user: " + getUser, None, 1 )

# File path checks
if not os.path.exists( fullPath[ 0 ] ):
    errors( "2", fullPath[ 0 ], " does not exist", None, 1 )
for i in range( len( fileDepends ) ):
    if not os.path.exists( fullPath[ 0 ] + fileDepends[ i ] ):
        errors( "3", fullPath[ 0 ] + fileDepends[ i ], " does not exist", None, 1 )

# Import SQLite3
import  sqlite3     as  sql

# Database connection
dbConn  = sql.connect( fullPath[ 0 ] + fileDepends[ 0 ] )
try:
    dbCurs = dbConn.cursor()
except:
    errors( "4", None, "Database connection failed", dbConn, 1 )

# Test database sanity
tabletest = 0
for i in range( len( dbTables ) ):
    dbTest = dbCurs.execute( "SELECT name FROM sqlite_master WHERE type='table' AND name='"+dbTables[ i ]+"'" )
    if dbTest.fetchone() is None:
        tabletest += 1
        errors( "", dbTables[ i ], " table missing", None, 0 )
if tabletest > 0:
    errors( "5", "", "Database sanity check failed", dbConn, 1 )

### FUNCTIONS ###############################################################################################


### PROGRAM RUN #############################################################################################


### END PROGRAM #############################################################################################

print( "Program End." )
dbConn.close()
sys.exit( 0 )
