def main():
    # provide the path where the file is located
    open_mode = open("C:\\Users\\AI\\PycharmProjects\\Logics\\newcorpus2\\MY_Description.txt","r")
    if open_mode.mode == "r":
        content = open_mode.read()
        print("Content to be read:")
        print(content)
     #write the file in the current directory
    write_mode = open("nltk.txt","w+")
    if write_mode.mode == "w+":
        content = write_mode.write(content)
        print("Content is written. Please check the required file:")

if __name__== "__main__":
    main()