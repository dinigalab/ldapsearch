# ldapsearch
command line tool for ldapsearch
usage: ldapsearch.py [-h] [-H HOST] [-d [DN]] [-p [PASSWORD]] [-f FILTER]
                     [-b BASE] [-a [ATTRIBUTE [ATTRIBUTE ...]]]
                     [-o OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  <hostname/IP>: LDAP server hostname or IP address
  -d [DN], --dn [DN]    <User_DN> : User DN for LDAP binding
  -p [PASSWORD], --password [PASSWORD]
                        <Password> : Password for LDAP Binding
  -f FILTER, --filter FILTER
                        <Search_Filer> : LDAP search filter
  -b BASE, --base BASE  <Base> : LDAP basedn
  -a [ATTRIBUTE [ATTRIBUTE ...]], --attribute [ATTRIBUTE [ATTRIBUTE ...]]
                        <attribute> : LDAP search attribute
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        <outputfile> : output csv file (default './ldap-
                        result.csv')
