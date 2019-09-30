import math


def letter_freq(txt):
    liten = txt.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?',
             '!', '@', '#', '$', '%', '^', '&', ')', '(']
    result = {}
    for i in range(len(alpha)):
        if liten.count(alpha[i]) != 0:
            result[ord(alpha[i])] = liten.count(alpha[i])

    return result


def entropy(message):
    """
    n_i is number of occurences of letter i
    (i is the UT F -8 code for the letter)
    n is number of letters in message
    p_i is frequency of the letter in the message
    """
    n_i = letter_freq(message)
    n = len(message)
    h = 0
    for i in n_i.values():
        p_i = float(i) / n
        """Entropy is then defined as h:"""

        h += -p_i * math.log(p_i, 2)

    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
