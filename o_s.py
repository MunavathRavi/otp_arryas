# operting system
# CLI = cammand line interface
#linux cammand
import os
# adders. = path =. locatin or adders
# path  : two type are the path 
# 1 = absulat
# 2 = relative
# getcwd =. get current working directory(folder)
print(os.getcwd())
# print(os.listdir())
# #mkdir  =. makedirectory

#os.makedirs("python")
# os.rmdir("python")
# useing in os module
# getcwd() =  it used to addres in folder
# chdir =  change to onther folder
# listdir =  it show the hoe many floder in os models
#mkdir = create a directory
# makedirs =  nextsd folder
# rkdis =. remove the folder
#os.removedirs
#os.remove("sample.text") = remove the file in os models
# shall scripting
# os.rename("operatin system.py","o_s.py") =. rename the file name in os models
#print(os.stat("o_s.py"))
# extera add th the file 
#path = os.path.join(os.getcwd(),"sample")
#os.chdir(path)
# print(os.path.isfile("./pyyton"))
# # os.path.isfile =. is cheek the file are not
# os.path.isdir =  is cheek the folder are not
# print(os.path.abspath("o_s.py"))
# print(os.environ.get("path"))
# print(os.name)
# print(os.getpid())
# devlepoment / bulid face
# producation / deployment



# system model:
import sys
print(sys)
# wa can excude the cammand it used the sys
# cli  =. cammand line intrface (we can see the applocations)
# gui = 
# argv. = is is list of stor a cammand line argument pass the script
# print(sys.argv)
# print(sys.path) = it used the where the comg a python model uesd the __path__
#sys.stdout.write("hellow world") it execed the os out put
#sys.stderr.write("sample texr ") it used the error handling it execud the frist
#print(sys.version) it show what pyhton can used and when it dewload
print(sys.platform)
name = "python"
if "win" in sys.platform:
    print(name)
else:
    print("not camperable")
#sys.setrecursionlimit =  it used limit the in global line
sys.modules =  "location"
print(sys.version_info)