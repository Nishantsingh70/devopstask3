import os
for root,dirs,files in os.walk('/root/devops_task3'):
    print(files)
    for file in files:
        if file.endswith('.html'):
           os.system('''if kubectl get deploy | grep myweb-deploy
                 then
                 kubectl delete all --all
                 kubectl delete pvc --all
                 kubectl create -f /root/devops_task3/deploy.yml
                 else
                 kubectl create -f /root/devops_task3/service.yml
                 kubectl create -f /root/devops_task3/jenkins_pvc.yml
                 kubectl create -f /root/devops_task3/deploy.yml''')
           
          
