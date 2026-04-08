from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"- {self.name}")

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def show(self, indent=0):
        print(" " * indent + f"[{self.name}]")
        for child in self.children:
            child.show(indent + 2)

root = Folder("root")
root.add(File("file1.txt"))

subfolder = Folder("docs")
subfolder.add(File("readme.md"))

root.add(subfolder)

root.show()
