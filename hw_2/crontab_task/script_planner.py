from crontab import CronTab
from config import CRON_USER


cron = CronTab(user=CRON_USER)

first_job = cron.new(command='python script.py')
first_job.hour.every(3)

second_job = cron.new(command='python script.py')
second_job.hour.on(15)
second_job.minute.on(15)

third_job = cron.new(command='python script.py')
third_job.dow.on('SUN')
third_job.hour.on(0)

cron.write()

iter2 = cron.find_comment('comment')
for job in cron:
    print(job)
