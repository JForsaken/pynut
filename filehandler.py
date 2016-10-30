class FileHandler:
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileInstance = open(filePath, "w")

        print("\nOpening file ...\n")

    def write(self, text):
        if text and text != -1:
            print(text)
            self.fileInstance.write(text + '\n')

    def dispose(self):
        self.fileInstance.close()
        print('Disposing file ...')
