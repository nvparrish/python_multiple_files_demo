import outclass
import subfolder.inclass

def main():
    object1 = outclass.OutClass(True)
    object1.display()

    object2 = subfolder.inclass.InClass(True)
    object2.display()

if __name__ == "__main__":
    main()
