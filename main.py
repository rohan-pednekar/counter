from model import Reader


if __name__ == "__main__":
    file: str = 'static/text.txt'
    reader: Reader = Reader(file)
    
    word = 'lorem'
    print('{word}: {count}'.format(word=word, count=reader.get_word_count(word)))