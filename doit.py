import os
import re
path_of_the_directory = "/Users/kenhung/tt/tttt"
# print("Files and directories in a specified path:")
name = []
notWorking = []
# timer
import time
def downloadImage(fileType):
    for root, dirs, files in os.walk(path_of_the_directory):
        for i in files:
            if(i.endswith(".html")):
                filename = os.path.join(root, i)
                with open(filename) as file:
                    for line in file:
                        if(line.rstrip().__contains__("cdn.shopify.com/s/files")):
                            # fileType
                            
                            if(len(re.findall(r'cdn.shopify.com/s/files.*.'+fileType, line.rstrip()))) > 0:
                                # Download the image to the image folder directory
                                orgString = re.findall(r'cdn.shopify.com/s/files.*.'+fileType, line.rstrip())[0]
                                # print(jj)
                                imageDownloadUrl = "http://" +orgString.split("."+fileType)[0]+"."+fileType
                                imageName = imageDownloadUrl.split("/")[-1]
                                # download the image to image folder
                                if(imageDownloadUrl not in name):
                                    # print(imageDownloadUrl)
                                    # print(imageName)
                                    # Download image to image folder 
                                    # os.system("wget " + imageDownloadUrl+ " -O /Users/kenhung/tt/tttt/image/" + imageName)
                                    name.append(imageDownloadUrl)
def updateString(fileType):
    for root, dirs, files in os.walk(path_of_the_directory):
        for i in files:
            if(i.endswith(".html")):
                filename = os.path.join(root, i)
                with open(filename) as file:
                    orgList = []
                    newList = []
                    for line in file:
                        if(line.rstrip().__contains__("cdn.shopify.com/s/files")):
                            if(len(re.findall(r'cdn.shopify.com/s/files.*.'+fileType, line.rstrip()))) > 0:
                                orgString = "https://"+re.findall(r'cdn.shopify.com/s/files.*.'+fileType, line.rstrip())[0]
                                # print(orgString)
                                imageDownloadUrl = orgString.split("."+fileType)[0]+"."+fileType
                                print(imageDownloadUrl)
                                imageName = imageDownloadUrl.split("/")[-1]
                                newImagePath = "https://codemug-hk.github.io/oldiesoldies/images/" + imageName
                                # rename the image in the html file
                                if(newImagePath.__contains__("width")):
                                    # print(newImagePath)
                                    # notWorking.append(orgString)
                                    # get the string before {width}
                                    orgString = (orgString.split("{width}")[0])
                                    newImagePath = newImagePath.split("{width}")[0]
                                    orgList.append(orgString)
                                    newList.append(newImagePath)
                                else:
                                    print(imageDownloadUrl)
                                    orgList.append(imageDownloadUrl)
                                    newList.append(newImagePath)
                                    # print(newImagePath)
                                    



                                    
                                    # print(newImagePath)
                try:
                    
                    fin = open(filename, "rt")
                    #read file contents to string
                    data = fin.read()
                    #replace all occurrences of the required string
                    for orgString, newImagePath in zip(orgList, newList):
                        data = data.replace(orgString, newImagePath)
                    #close the input file
                    fin.close()
                    #open the input file in write mode
                    fin = open(filename, "wt")
                    #overrite the input file with the resulting data
                    fin.write(data)
                    #close the file
                    fin.close()
                    # if(len(orgList) > 0):
                    #     print(filename)
                    # replace the string in the html file using using perl
                    #"perl -pe 's/<!--New Posts Go Below This Line-->/`cat newpost.txt`/ge' index.html > index-new.html"

                    
                    for orgString, newImagePath in zip(orgList, newList):
                        # sed -i '' "s|${STRING1}|${STRING2}|g" FILE
                        # print("sed -i '' 's/"+orgString+"/"+newImagePath+"/g' "+filename)
                        # os.system("sed -i '' 's/"+orgString+"|"+newImagePath+"/g' "+filename)
                        print("gsed -i '' 's/"+orgString+"/"+newImagePath+"/g' "+filename)
                        # os.system("perl -pe 's/"+orgString+"/cat"+newImagePath+"/ge' "+filename+" > "+filename)
                        # os.system("gsed -i '' 's/"+orgString+"/"+newImagePath+"/g' "+filename)
                        os.system("perl -pe 's/"+orgString+"/"+newImagePath+"/ge' "+filename+" > "+filename)
                        # os.system("perl -pe 's/"+orgString+"/"+newImagePath+"/ge' "+filename+" > "+filename)
                    


                except Exception as e: 
                        print("Error: ")
                        print(e)
                        notWorking.append(orgString)
                                    # print("sed -i '' 's/"+orgString+"/"+newImagePath+"/g' "+filename)
                                    # os.system("sed -i '' 's/"+orgString+"/"+newImagePath+"/g' "+filename)
    # for i in notWorking:
    #     print(i)
                                



# print("Total number of images: " + str(jj))

downloadImage("png")
downloadImage("jpg")
downloadImage("jpeg")
downloadImage("gif")
downloadImage('avif')
downloadImage('webp')
downloadImage('svg')


updateString("png")
updateString("jpg")
updateString("jpeg")
updateString("gif")
updateString('avif')
updateString('webp')
updateString('svg')
