# from itertools import count
from functools import reduce
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):
    # def mapper(self, _, line):
    #     yield "chars", len(line)
    #     yield "words", len(line.split())d
    #     yield "lines", 1
    
    # 1. Map semua kata (alphanumeric) yang ada di Script tersebut dengan standard uppercase. 
    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            self.increment_counter('group', 'lines', 1)
            yield (word.upper(), len(word))

    # 2. Hitung total dari setiap kata yang muncul di Script tersebut. 
    def combiner_counter_words(self, word, line):
        self.increment_counter('group', 'combiners', 1)
        yield (word, sum(line))
    
    # 3. Cari kata yang paling banyak disebutkan di Script tersebut.
    def reduce_find_max_words(self, word, word_counts):
        self.increment_counter('group', 'reducer_1', 1)
        yield word, max(word_counts)

    # 4. buat counter di proses mapper dan reducer.
    # def reducer_count_words(self, words, counts):
    #     self.increment_counter('groups', 'reducer_2', 1)
    #     yield None, (sum(counts), words)


    # def reducer(self, key, value):
    #     yield key, sum(value)

    def steps(self):
        return[
            MRStep(
                mapper=self.mapper_get_words,
                combiner=self.combiner_counter_words,
                reducer=self.reduce_find_max_words)
        ]

if __name__ == '__main__':
    MRWordFrequencyCount.run()