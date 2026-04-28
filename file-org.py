import os
import shutil

print("enter path")
folder = input()
files = os.listdir(folder)

for file in files:

    if file.endswith((".mp4",".avi" , ".mkv" , ".mov")):
        destinaton = os.path.join(folder ,"Videos")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")

    elif file.endswith((".png" , ".jpg" , ".jpeg" ,".gif")) :
        destinaton = os.path.join(folder ,"Images")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")

    
    elif file.endswith((".md" , ".pptx" , ".pdf" , ".docx" ,".txt" )):
        destinaton = os.path.join(folder ,"Documents")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    elif file.endswith((".html" , ".css" , ".js")):
        destinaton = os.path.join(folder ,"Web-prog")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    elif file.endswith(".cpp") :
        destinaton = os.path.join(folder ,"C++prog")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    elif file.endswith(".py") :
        destinaton = os.path.join(folder ,"pythonprog")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    elif file.endswith((".zip", ".rar" ,".tar" , ".gz" , ".7z")) :
        destinaton = os.path.join(folder ,"Compressedfiles")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    elif file.endswith(".iso"):
        destinaton = os.path.join(folder ,"OS")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    else:
        destinaton = os.path.join(folder ,"Other")
        os.makedirs(destinaton , exist_ok=True)
        shutil.move(os.path.join(folder,file) , destinaton)
        print("done")
    
    
    




