import ldap
import csv
import argparse
import sys

# Argument definition
# if the option -a is not set for the searchAttribute, it will retrieve all the attribute for the objectClass
# if the option for user DN and password are not set, it will try to connect anonymously
# if the option for output file is not set, the default will be "ldap-result.csv"

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', help='<hostname/IP>: LDAP server hostname or IP address', nargs=1)
parser.add_argument('-d', '--dn', help='<User_DN> : User DN for LDAP binding', nargs='?')
parser.add_argument('-p', '--password', help='<Password> : Password for LDAP Binding', nargs='?')
parser.add_argument('-f', '--filter', help='<Search_Filer> : LDAP search filter', nargs=1)
parser.add_argument('-b', '--base', help='<Base> : LDAP basedn', nargs=1)
parser.add_argument('-a', '--attribute', help='<attribute> : LDAP search attribute', nargs='*')
parser.add_argument('-o', '--outputfile', help='<outputfile> : output csv file (default \'./ldap-result.csv\')', default='ldap-result.csv', nargs=1)

args = parser.parse_args()


if args.host:
	l = ldap.initialize('ldap://%s' % "".join(args.host))
else:
	parser.error("Please enter LDAP server hostname/IP : Option -H")

def connect(user, pwd):
	try:
		l.protocol_version = ldap.VERSION3
		l.simple_bind_s(user, pwd) 
	except ldap.INVALID_CREDENTIALS:
	  print "Your username or password is incorrect."
	except ldap.LDAPError, e:
	  if type(e.message) == dict and e.message.has_key('desc'):
		  sys.exit(e.message['desc'])
	  else: 
		  sys.exit(e)

	
def connect_anonymous():
	try:
		l.set_option(ldap.OPT_REFERRALS, 0)
		l.protocol_version = ldap.VERSION3
		l.simple_bind_s() 
		print('Anonymous connection to server %s ' % "".join(args.host))
	except ldap.LDAPError, e:
	  if type(e.message) == dict and e.message.has_key('desc'):
		  sys.exit(e.message['desc'])
	  else:
		  sys.exit(e)


def search():
	#check if anonymous or not
	if args.dn and args.password:
		connect("".join(args.dn), "".join(args.password))
	elif args.dn and args.password is None:
		sys.exit("please enter password : option -p")
	elif args.dn is None and args.password:
		sys.exit("Please enter DN : option -d")
	else:
		connect_anonymous()
	#check if base exist	
	if args.base:
		basedn = "".join(args.base)
	else:
		sys.exit("Please enter LDAP base search : Option -b")
	#check if filter exist	
	if args.filter:
		searchFilter = "".join(args.filter)
	
	else:
		sys.exit("Please enter LDAP base search : Option -f")
		
	searchAttribute = args.attribute
	#this will scope the entire subtree under selected ldap base
	searchScope = ldap.SCOPE_SUBTREE 
	
	try: 
		result_list = []
		order_keys = []
		temp_keys = []
		
		results = l.search_s(basedn, searchScope, searchFilter, searchAttribute)
		print results
		for dn, entry in results:
			result_list.append(entry)
			temp_keys = entry.keys()
			
		if searchAttribute:
			for key in searchAttribute:
				if not key in order_keys:
					order_keys.append(key)
		else:
			for key in temp_keys:
				if not key in order_keys:
					order_keys.append(key)
					
	except ldap.LDAPError, e:
		if type(e.message) == dict and e.message.has_key('desc'):
		  sys.exit(e.message['desc'])
		else:
		  sys.exit(e)
	
	#check if the result is empty
	if len(result_list) == 0:
		sys.exit("There is no result for your search, please verify your filter!!!")
	return(result_list, order_keys)

def generate_csv(results, keys, fd):
	if results:
		with open(fd,'wb') as fd_output:
			
			spamwriter = csv.writer(fd_output, delimiter=';')
			spamwriter.writerow(keys)
			
			for res in results:
				output_line = []
						
				for key in keys:
					if key in res.keys():
						output_line.append(''.join(res[key]))
					else:
						output_line.append('')
				
				spamwriter.writerow(output_line)
		fd_output.close()
	
	return
	
def main():
	results, keys = search()
	generate_csv(results, keys, "".join(args.outputfile))
	
	return
	
if __name__ == "__main__":
	main()
