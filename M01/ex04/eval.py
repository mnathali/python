from functools import reduce

class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        return sum(map(lambda s: s[0] * len(s[1]), zip(coefs, words)))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        dct = dict(enumerate(map(len, words)))
        return sum([dct[i] * coefs[i] for i in dct])


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))