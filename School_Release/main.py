import sys


class SysManager:  # I control, manage, and keep track of the file system!
    def __init__(self) -> None:
        self.tree = []

    def mkdir(self, name: str, location: str | Folder):
        if name != "":
            if location != "":
                print(self.tree)
                location_idx = self.tree.index(location)
                name_idx = self.tree[
                    location_idx
                ]  # FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCKKKKKK
                if self.tree[location_idx][name] not in self.tree:
                    self.tree[location_idx].append(name)
                else:
                    print(
                        "I am too lazy to code automatic appending the number of repetitive objects right now"
                    )
                return
            else:
                self.tree.append(name)
                return
        else:
            print("You must specify a name!")
            return

    def touch(self, name: str, location: str):
        pass

    def rm(self):
        pass

    def ls(self, location: str):  # No flags for you!
        for item in self.tree[self.tree.index(location)]:
            pass

    def pwd(self):  # Not sure if this will get implemented!
        pass


class Folder:
    def __init__(self, name: str | Folder) -> None:
        self.name = name
        self.kids = []


class File:
    def __init__(self, name: str, payload) -> None:
        self.name = name
        self.payload = payload


def main():
    god = SysManager()

    def init():
        god.mkdir("Users", "")
        god.mkdir("Eric", "Users")

    init()
    running = True
    while running:
        user_input = input("[/]$ ").strip().lower()
        if "exit" in user_input:
            if user_input == "exit":
                sys.exit()
            else:
                exit_code = user_input.split(" ")[1]
                sys.exit(int(exit_code))
        elif "mkdir" in user_input:
            split_input = user_input.split(" ")
            god.mkdir(split_input[1], split_input[2])


main()
