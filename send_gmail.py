#!/usr/bin/python
import string, os, sys, time 
import os.path
import smtplib
from optparse import OptionParser
import optparse

#Sourced from: http://exchange.nagios.org/directory/Plugins/Uncategorized/Operating-Systems/Linux/Nagios-Alerts-via-gmail-and-python/details
"""
This quick and dirty script can be used to send email messages from command line using a gmail account.
It was designed to be a simple replacement for the default mail program (sendmail) used by Nagios.
You must configure this file to work with your gmail account...
Note: this script may be unsecure as the password is stored as plain text in the script.

Requires smtplib, python 2.4.4c1+ and optparse

Usage:
send_gmail.py -a [to address] -s [subject] -b [message body]

New lines can be inserted in the message body by using   \nnn 
Multiple to addresses must be seperated by commas (a space character may preceed and/or follow the comma)

Example:
send_gmail.py -a "someone@somedomain.null,someone@smsgateway.null" -s "This is the subject line..." -b "Body line one\nnnAnd this is line two"

code based on http://mail.python.org/pipermail/python-list/2007-January/423569.html

**Update/Revision History**
2008.04.09 - Version 1.0.1 posted, fixed problem where script would not handle multiple recipents,
smtplib's .sendmail() requires an array to send to multiple addresses. If all addresses are passed as a string, it will only send to the first address.

2008.01.24 - Version 1.0.0 posted

"""
ori_eaddy = 'someone@contoso.com'
ori_pword = 'password'
ori_smtpserver = 'smtp.gmail.com'
ori_smtpport = 587

def prefixhostname(s):
	#takes a string and adds the machine's hostname
	import socket
	h = socket.gethostname()
	s = "Notification from " + h + ": " + s
	return(s)

def sendmail(**kwargs):
	for o in kwargs:
		if o == 'body':
			body = kwargs[o]
		if o == 'subject':
			subject = kwargs[o]
		if o == 'addresses':
			addresses = kwargs[o]
		if o == 'address':
			address = kwargs[o]
		if o == 'smtpserver':
			smtpserver = kwargs[o]
		if o == 'smtpport':
			smtpport = kwargs[o]
		if o == 'fromaddy':
			fromaddy = kwargs[o]
		if o == 'pword':
			pword = kwargs[o]
	try:
		smtpserver
	except:
		smtpserver = 'smtp.gmail.com'
	try:
		smtpport
	except:
		smtpport = 587
	
	server = smtplib.SMTP(smtpserver, smtpport)
	server.set_debuglevel(1) #0 for quiet or 1 for verbosity
	server.ehlo(fromaddy)
	server.starttls()
	server.ehlo(fromaddy)  # say hello again
	server.login(fromaddy, pword)
	
	server.sendmail(fromaddy, addresses, "Subject: " + subject + '\nTo:' + address + '\n\n' + body)
	
	server.quit()

def main():
	p = optparse.OptionParser( )
	p.add_option('--address', '-a', action='store', type='string', help='default is ' + ori_eaddy)
	p.add_option('--body', '-b', action='store', type='string')
	p.add_option('--subject', '-s', action='store', type='string')
	p.add_option('--bodysub', '-d', action='store', type='string', help='string to use as both body and subject, overrides -body and -subject')
	options, arguments = p.parse_args()
	try:   
		body = options.body
	except:
		body = ''
	try:
		address = options.address
	except:
		address = ori_eaddy
	if address == None:
		address = ori_eaddy
	Addresses = address.split(',') #turns string into array by splitting string at commas.
	try:
		subject = options.subject
	except:
		subect = ''
	try:
		bodysub = options.bodysub
	except:
		bodysub = ''
	if options.bodysub:
		body = bodysub
		subject = bodysub
	


	body = '\n'.join(body.split('\\nnn'))
	
	try:
		body = prefixhostname(body)
	except:
		pass

	try:
		subject = prefixhostname(subject)
	except:
		pass

	#now run the sendmail function
	sendmail(body=body,
			address=address,
			addresses=Addresses,
			subject=subject,
			smtpserver=ori_smtpserver,
			smtpport=ori_smtpport,
			fromaddy=ori_eaddy,
			pword=ori_pword)
if __name__ == '__main__':
	main()

