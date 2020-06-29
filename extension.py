import os
for root,dirs,files in os.walk('/root/devops_task3'):
    print(files)
    for file in files:
        if file.endswith('.html'):
          os.system("kubectl create -f /root/devops_task3/service.yml")
          os.system("kubectl create -f /root/devops_task3/jenkins_pvc.yml")
          os.system("kubectl create -f /root/devops_task3/deploy.yml")
    
