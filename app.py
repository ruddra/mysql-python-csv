import subprocess
import sys
import datetime
try:
    sql_cmd = "mysql -uUserName -pPassword -e 'SELECT * FROM csv_test.test;'"
    result_success = subprocess.check_output(
            [sql_cmd], shell=True)
    data = result_success.decode('utf-8')
    csv_data = ''
    for item in data.split('\n'):
        csv_data += '{0}\r\n'.format(item.replace('\t', ','))
    filename = 'report_{0}.csv'.format(datetime.datetime.now().strftime('%d-%m-%Y:%H:%M:%S'))
    csv_out = open(filename, 'w')
    csv_out.write(csv_data)
    csv_out.close()

except Exception as e:
    print(e)

