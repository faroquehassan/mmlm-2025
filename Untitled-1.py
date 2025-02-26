# def bayes_theorem():
#     p_spam = 0.2
#     p_non_spam = 0.8
#     p_word_given_spam = 0.7
#     p_word_given_non_spam = 0.10

#     ### calculate p_spam_given_word
#     p_word = p_word_given_spam * p_spam + p_word_given_non_spam * p_non_spam
#     p_spam_given_word = (p_word_given_spam * p_spam )/ (p_word)

#     return p_spam_given_word

# print(f"Probability that email is spam given 'win': {bayes_theorem():.4f}")

import numpy as np
import pandas as pd

#markov process