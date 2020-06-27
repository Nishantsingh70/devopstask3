import os
for root,dirs,files in os.walk('/root/devops_task3'):
    print(files)
    for file in files:
        if file.endswith('.php'):
          os.system("kubectl create -f jenkins_pvc.yml")
          os.system("kubectl create -f /root/devops_task3/deploy.yml")
          os.system("kubectl expose deploy myweb-deploy --type=NodePort --port=80")
        elif file.endswith('.html'):
          os.system("kubectl create -f jenkins1_pvc.yml")
          os.system("kubectl create -f /root/devops_talk3/deploy1.yml")
          os.system("kubectl expose deploy myweb-deploy1 --type=NodePort --port=80")
            
