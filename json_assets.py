import json

def main():
    with open('pressure.json') as json_file:
        data = json.load(json_file)
        data_nodes = data["nodes"]

        asset_list_images = []
        asset_list_icons = []
        for key in data_nodes:
            data_nodes_obj = data_nodes[key]
            #print(data_nodes_obj)

            for obj in data_nodes_obj:
                #print(obj, type(obj))

                if (obj  == "icon") :
                    #create a list of icons
                    asset_list_icons.append(data_nodes_obj[obj])
                    #####################################
                    #print each icon identified in the json file to the  screen
                    #print(data_nodes_obj[obj])
                    #####################################
                elif (obj == "image"):
                    # create a list of icons
                    asset_list_images.append(data_nodes_obj[obj])
                    #####################################
                    #print each icon identified in the json file to the  screen
                    #print(data_nodes_obj[obj])
                    #####################################



        #convert list to set to remove duplicate asset and then convert back to list;
        asset_sets_icons = set(asset_list_icons)
        asset_list_icons = list(asset_sets_icons)

        asset_sets_images = set(asset_list_images)
        asset_list_images = list(asset_sets_images)

        print(asset_list_icons)
        print(asset_list_images)


if __name__ == '__main__':
    main()
