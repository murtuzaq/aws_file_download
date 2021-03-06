import json
import os
import boto3
import botocore

#for now link to aws sandbox account:
#https://myapps.microsoft.com/signin/Chefman AWS Accounts SSO/42dedcdc-66d3-4ac1-824e-7a4086c7a967?tenantId=84970def-d1e8-4a80-a08a-9d374cffcda2

BUCKET_NAME = 'chefiq-icons'
BUCKET_FILE_NAME = '40x40/A_ico-pintobeans-01.png'
LOCAL_FILE_NAME = 'my_image.jpg'

def download_aws_file(bucket, from_dir, to_dir, file):
    s3Client = boto3.client('s3')

    file_path = from_dir + '/' + file;
    print("file --->", file_path)

    #if not os.path.exists(os.path.dirname("icons")):
    #    os.makedirs(os.path.dirname("icons"))

    downloaded_path = to_dir + "/" + file
    try:
        s3Client.download_file(bucket, file_path, downloaded_path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("W: The object does not exist. file =", downloaded_path)
        else:
            print("W: file not downloaded =", downloaded_path)
            raise

def download_new_fw_file(bucket, filename):
    print(bucket)
    print(filename)
    s3Client = boto3.client('s3')
    s3Client.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

    #s3 = boto3.resource('s3')
    print("=================== s3=============")
    #print(s3)
    #s3.meta.client.download_file("chefiq-icons", '40x40/A_ico-pintobeans-01.png', 'my_image.jpg')

    #response = s3Client.get_object(
    #    Bucket= "chefiq-icons",
    #    Key="A_ico-pintobeans-01.png",
    #)
    #print(response)


def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

def download_all_objects_in_folder():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET_NAME)
    objects = my_bucket.objects.filter(Prefix='ico/')
    print("objects", type(objects) )

    for obj in objects:
        print(obj.key)
    #for obj in objects:
    #    path, filename = os.path.split(obj.key)
    #    my_bucket.download_file(obj.key, filename)


def open_json_file( file ):
    print("open json file :", file)
    try:
        with open(file) as json_file:
            # json file may be improperly formatted, and thus crash without a try/catch
            try:
                data = json.load(json_file)
                return data
            except ValueError as e:
                print("E: fail to parse json file")

    except IOError:
        print("E: fail to open file", file)

    return None

def main():

    ###################################
    # create a list of all json files in specified folder
    path_to_json = 'json_files/'
    list_json_files = []
    for file in os.listdir(path_to_json):
        if (file.endswith(".json")):
            list_json_files.append(path_to_json + file)
    ###################################

    list_images = []
    list_icons = []

    for file in list_json_files:
        ###################################
        #print json file found to be parsed
        #print(file)
        ###################################
        data = open_json_file(file)
        if data == None:
            return

        data_nodes = data["nodes"]

        for key in data_nodes:
            data_nodes_obj = data_nodes[key]
            #print(data_nodes_obj)
            for obj in data_nodes_obj:
                #print(obj, type(obj))
                if (obj  == "icon") :
                    #create a list of icons
                    list_icons.append(data_nodes_obj[obj])
                    #####################################
                    #print each icon identified in the json file to the  screen
                    #print(data_nodes_obj[obj])
                    #####################################
                elif (obj == "image"):
                    # create a list of icons
                    list_images.append(data_nodes_obj[obj])
                    #####################################
                    #print each icon identified in the json file to the  screen
                    #print(data_nodes_obj[obj])
                    #####################################



    #convert list to set to remove duplicate asset and then convert back to list;
    set_icons = set(list_icons)
    list_icons = list(set_icons)

    sets_images = set(list_images)
    list_images = list(sets_images)

    #####################################
    # print number of icons and images collected in the list
    print("number of icons:", len(list_icons) )
    print(list_icons)

    print("number of images:", len(list_images) )
    print(list_images)
    ####################################

    ###################################
    # When downloading the amazon S3 bucket, but dont have  permission: error message will be
    #botocore.exceptions.ClientError: An error occurred(403) when calling the HeadObject operation: Forbidden

    #download_new_fw_file(BUCKET_NAME, BUCKET_FILE_NAME)

    #for icon in list_icons:
    #    download_aws_file(BUCKET_NAME,"40x40", "icons", icon)

    for image in list_images:
        download_aws_file("chefiq-images", "100x240", "images", image)

    #download_aws_file("chefiq-images", "100x240", "images", "img-95.jpg")

if __name__ == '__main__':
    main()
