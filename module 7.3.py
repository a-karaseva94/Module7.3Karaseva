# Задача "Найдёт везде"

class  WordsFinder:

    def __init__(self, *args):
        self.args = args
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        self.all_line = []
        self.all_words = {}
        for file_n in self.file_names:
            with open(file_n, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for ele in line:
                        if ele in punc:
                            line = line.replace(ele, "")
                    line = line.split()
                    self.all_line = self.all_line + line
            self.all_words.update({file_n: self.all_line})
            return self.all_words

    def find(self, word):
        find_word = {}
        find_word_ch = 1
        self.word = word.lower()
        for file_n, self.all_line in self.get_all_words().items():
            find_word_ch += self.all_line.index(self.word)
            find_word.update({file_n: find_word_ch})
            return find_word

    def count(self, word):
        count_word = {}
        count_word_ch = 0
        self.word = word.lower()
        for file_n, self.all_line in self.get_all_words().items():
            for i in range(len(self.all_line)):
                if self.all_line[i] == self.word:
                    count_word_ch += 1
            count_word.update({file_n: count_word_ch})
            return count_word


# Пример выполнения программы
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Пример выполнения программы
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

# Пример выполнения программы
finder3 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))