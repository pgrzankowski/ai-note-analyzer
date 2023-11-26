from components.FileReader import FileReader
from components.TextBot import TextBot


def main():
    # Get files as concatenated string
    fileReader = FileReader("notes")
    concatenatedNotes = fileReader.getConcatenatedText()

    # Get question
    question = "Show my movies which i havent watched yet"


    # Setup TextBot
    textBot = TextBot(concatenatedNotes)
    response = textBot.getResponse(question)
    print(response)


if __name__ == "__main__":
    main()
