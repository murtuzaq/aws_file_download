import json


def main():
    with open('pressure.json') as json_file:
        data = json.load(json_file)
        print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
