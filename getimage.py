import requests,threading,os
from random import choice
name_folder = input('Enter folder name (./) : ')# اذ بتسوي فولدر بمكان السكربت اكتب  ./folder

try:
    if not os.path.exists(name_folder+'/'):
        os.makedirs(name_folder+'/')
except OSError:
    print ('Error: Creating directory. ' +  name_folder)
            



name = input('Image Key :  ')

stri = 'zxcvbnmasdfghjklqwertyuiop1234567890'

def get_pa(num):
    url = f'https://unsplash.com/napi/search/photos?query={name}&xp=&per_page=20&page={num}'
    
    imgGet = requests.get(url)
    json_img = imgGet.json()  

    to = json_img['total']# total image 
    json_img = json_img["results"]# posts

    if to ==0:
        exit()
    for i in json_img:

        na = i['alt_description'] # name
       

        img_url = requests.get( i['urls']['raw'])
        if na ==None:
            

            a = ''.join([choice(stri) for i in range(10) ])
            with open(f'{name_folder}/'+a+'.png','wb') as img_fil :

                img_fil.write(img_url.content)
        else:
            
            with open(f'{name_folder}/'+na+'.png','wb') as img_fil :

                img_fil.write(img_url.content)

the = []

for i in range(1,100):
    t = threading.Thread(target=get_pa,args=(i,))
    t.daemon =True
    t.start()
    the.append(t)
    
for i in the:
    i.join()