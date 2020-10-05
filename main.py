
import A_STAR as A
import FILEREAD as F
f = F.FileRead()

if __name__ == "__main__":
    A.a_Star(input('Text file path: '), 's', 'g')
else:
    print("Invalid Module")
