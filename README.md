
This is a script modified from here:
 http://exchange.nagios.org/directory/Plugins/Uncategorized/Operating-Systems/Linux/Nagios-Alerts-via-gmail-and-python/details
 
 I modified it so it can use an anonymouse Gmail SMTP server instead of having to authenticate every time. To set up your Google Apps for anonymous SMTP pushes you can follow this guide.
 
 https://support.google.com/a/answer/176600?hl=en
 http://community.spiceworks.com/topic/391232-an-smtp-relay-to-google-apps-gmail
 

Usage: send_gmail.py [options]

Options:
  -h, --help            show this help message and exit
  -a ADDRESS, --address=ADDRESS
                        default is someone@contoso.com
  -b BODY, --body=BODY
  -s SUBJECT, --subject=SUBJECT
  -d BODYSUB, --bodysub=BODYSUB
                        string to use as both body and subject, overrides
                        -body and -subject
