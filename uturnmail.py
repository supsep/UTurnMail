import email, boto.sqs, sys, time, smtplib
from random import randrange
from pprint import pprint

msg = email.message_from_file(sys.stdin)
timestamp = "Id: "+  str(randrange(10))+" Time: " + time.strftime("%c")
sender = "From : " +  msg.get_unixfrom()
payload = "Message: "
for item in msg.get_payload():
        payload += item.as_string(False)

logFile=open('/mnt/spool/uturnmail/script_logs/uno.txt', 'w')
#pprint(sender, logFile)
#pprint(payload, logFile)
#pprint(timestamp, logFile)

result = timestamp + sender + payload
logFile.write(result)

del logFile, msg, item, payload, sender 

#<----------------------------------------------------------------------------->
#Will implement save email to a file first to examine it
#AMAZON SQS
#conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ465WWFWWSIUEKIQ', aws_secret_access_key='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')
#Get the queue
#queue = conn.get_queue('myqueue')
#message = "Time of Python Exec." +  time.strftime("%c") + "\n" + vars(msg)
#<------------------------------------------------------------------------------>

client = smtplib.SMTP('127.0.0.1', 10025)
client.sendmail("sepehr.tah@gmail.com", "sept@uturnmail.com", result)
client.quit()
del client

sys.exit(0)

