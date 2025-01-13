import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos,file)

def list_all(videos):
    print( "-." * 40)
    for index, vid in enumerate (videos, start=1):
        print(f"{index}. {vid['name']} | Duration: {vid['time']}")
    print( "-." * 40)

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manger | Choose an Option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all(videos)
            case "2":
                add_video(videos)
            case "3":
                print("fuck off dude")
                #update_details(videos)
                pass
            case "4":
                print("fuck off dude")
                #delete_video(videos)
                pass
            case "5":
                break
            case _:
                print("Invalid Choice | Try Again")
                
if __name__ == "__main__":
    main()