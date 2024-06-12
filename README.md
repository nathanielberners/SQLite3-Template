SQLite3 Tempate - program stub for developing SQLite3 backed programs.                                              
Uses path checking, database checking and error handling.                                                 
Supports user access limiting (free-for-all unless one or more usernames are configured).

Error handling is provided by the function errors(). It's use is thus:                                    
  errors( errnum, erritem, errmessage, dbconn, errexit )                                                
  errnum - is the error number to report (to assist in bug hunting); manually defined or None       
  erritem - is the item for which the error is called, or None                                      
  errmessage - provide a message to print on error                                                  
  dbconn - The SQLite3 database connection object, or None                                          
  errexit - an integer to trigger an exit: 0 = continue program, >=1 = exit
  
User access is controlled with the userNames([]) tuple. If empty, the program will run for anyone.        
  Supply a system login username as a tuple element to enable access control.
