
! usr bin/ env bash
echo -e "wsgi process"

ps -ef|grep nice_uwsgi.ini |grep -v grep

sleep 0.5

echo -e '/n --- going to close --- '

ps -ef|grep nice_uwsgi.ini | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

echo -e '/n -- check if kill is correct'

/envs/nice/bin/uwsgi --ini nice_uwsgi.ini& >/dev/null

echo -e '----- starting ----'
sleep 1

ps -ef | grep nice_uwsgi.ini | grep -v grep


