import os
upload_id=input("Enter UploadID for multipart upload: ")
key=input("Input Key name for multipart upload: ")
file_name=("Input file part name (No numbers :")
bucket=input("Input AWS Bucket name: ")
end_point = input("Input the total number of file parts: ")
file_path = input("Input file path of file_parts: ")

command_name = None
print("Uploading file parts...")
for i in range(int(end_point)):
    upload_num = str(i+1)
    if (i+1) < 100 :
        if(i+1) < 10:
            upload_num = "00"+ str(upload_num)
        else:
            upload_num = "0"+str(upload_num)
    code= os.system(('cmd /c aws s3api upload-part --bucket ' + bucket + " --key " + key + " --part-number " + str(i+1) +" --body " + file_path + key +"." + upload_num + " --upload-id " + upload_id))
    code=code+1
    if code !=0:
        print(i+1)
        exit(code)
print("Done..")
