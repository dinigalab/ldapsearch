# ldapsearch
command line tool for ldapsearch

I preselected the search scope and set it to subtree.
And I also preselected the LDAP version and set it to version 3.
I wanted just to avoid adding multiple options.


usage: ldapsearch.py [-h HELP] [-H HOST] [-d [DN]] [-p [PASSWORD]] [-f FILTER]
                     [-b BASE] [-a [ATTRIBUTE [ATTRIBUTE ...]]]
                     [-o OUTPUTFILE]

optional arguments:

  -h, --help            show this help message and exit
  
  -H HOST, --host HOST  <hostname/IP>: LDAP server hostname or IP address
  
  -d [DN], --dn [DN]    <User_DN> : User DN for LDAP binding
  
  -p [PASSWORD], --password [PASSWORD] <Password> : Password for LDAP Binding
  
  -f FILTER, --filter FILTER <Search_Filer> : LDAP search filter
  
  -b BASE, --base BASE  <Base> : LDAP basedn
  
  -a [ATTRIBUTE [ATTRIBUTE ...]], --attribute [ATTRIBUTE [ATTRIBUTE ...]] <attribute> : LDAP search attribute
  
  -o OUTPUTFILE, --outputfile OUTPUTFILE <outputfile> : output csv file (default './ldap-result.csv')
