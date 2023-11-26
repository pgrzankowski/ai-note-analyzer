import os

class FileReader:
    """
    Reads each file from given folder and returns
    text from them in one concatenated string.
    """
    def __init__(self, fileFolder):
        self.fileFolder = fileFolder
        self.textFromFiles = []
        self.readFiles()

    def readFiles(self):
        for filename in os.listdir(self.fileFolder):
            file_path = os.path.join(self.fileFolder, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as text_file:
                    self.textFromFiles.append(
                        "File: " + text_file.name + "\n" +
                        text_file.read() + "\n"
                    )
    
    def getConcatenatedText(self):
        concatenatedText = ""
        for text in self.textFromFiles:
            concatenatedText += text
        return concatenatedText
