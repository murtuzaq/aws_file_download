import json
import os

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
        print(file)
        ###################################
        with open(file) as json_file:
            data = json.load(json_file)
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

if __name__ == '__main__':
    main()
