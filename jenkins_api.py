
import csv

def List_job(jenkins_url,jenkins_user,jenkins_pass):

    import jenkins

    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    user = server.get_whoami()
    jobs = server.get_jobs()

    job_stats=[]
    for i in jobs: 
        job_name= i['name'], 
        job_url= i['url'] , 
        job_status= i['color']
        job_stats.append([job_name,job_url,job_status])
    return job_stats

# c=List_job('http://45.33.11.12:8080','utrains','devops')
# print(c)

# with open("example.txt", 'a') as f:
#     # w means in write mode, a means append
#     content = "adding data into file\n"
#     f.write(content)
# with open("example.txt", 'r') as file:
#     content = file.read()
#     print(content)

data=List_job('http://45.33.11.12:8080','utrains','devops')

with open("jenkins_object.csv", 'w') as j:
    write_row =csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])
    #write_row.writerow(data)
    for item in data:
        write_row.writerow(item)