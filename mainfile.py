import sys
from time import time
from multiprocessing import Pool


def file_read(path: str) -> str:

    f = open(path, "r", encoding="utf-8")
    text = f.read()
    f.close()
    return text


def text_to_list(text: str) -> list:

    text = text.replace('\\s', '').replace('\\w', '')
    text = text.lower()
    text = text.split()
    return text



def find_the_word(key_word: str, path: str) -> None:
    text = file_read(path)
    text = text_to_list(text)

    if key_word in text:
        print(f'Ключевое слово "{key_word}" найдено в {path}')
    else:
        print(f'Ключевое слово "{key_word}" не найдено в {path}')
    return None


def main() -> None:
     
    input_data = sys.argv[1::]
    
    key_word = input_data[0].lower()
    paths = input_data[1:]

    key_word_list = [key_word] * len(paths)
    

    with Pool(4) as p:
        p.starmap(find_the_word, zip(key_word_list, paths))

   
    input("Нажмите Enter")
    return None

#Сахар Tangerine_dessert.txt Chocolate_fondane.txt Banana_witn_cottage_cheese.txt Chocolate_muss.txt Escimo.txt

if __name__ == "__main__":
    main()