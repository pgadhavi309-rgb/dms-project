class MyFile:
    def __enter__(self):
        self.f = open("myfile.txt", "w")
        return self.f
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print("File closed")

with MyFile() as f:
    f.write("Hello from custom context manager!")
