#This script checks to make sure the pytweet script is running.

# find service pids
pgrep pytweet
 
#if we get no pids, service is not running
 
if [ $? -ne 0 ]
then
 service pytweet start
 echo "pytweet started or restarted."
fi