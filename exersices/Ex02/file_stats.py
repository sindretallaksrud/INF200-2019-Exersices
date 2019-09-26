def char_counts(textfilename):

    file = open(textfilename)
    text = file.read()
    file.close()

    utf8 = []
    letters = []

    for letter in text:
        letters.append(letter.split())

    """removing white-spaces: add x for all the values x in letters if x has a value"""
    letters_ws = [x for x in letters if x]

    """converts all symbols into UTF-8 format"""
    for key in range(len(letters_ws)):
        utf8.append(ord(letters_ws[key][0]))

    """fill the result list with how many times each number occurs"""
    result = []
    for number in range(256):
        result.append(utf8.count(number))

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
