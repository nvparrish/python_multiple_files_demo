import outclass
import subfolder.inclass

def main():
    object1 = outclass.OutClass()
    object1.display()

    object2 = subfolder.inclass.InClass()
    object2.display()
    object2.greet_neighbor()

if __name__ == "__main__":
    main()
