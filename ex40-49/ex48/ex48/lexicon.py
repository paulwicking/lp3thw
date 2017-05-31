def scan(words_to_scan):
    """
    Scan words in lists, return a tuple with word category if found
    rtype: tuple
    """
    words = words_to_scan.split()
    word_pairs = []

    dictionary = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'west': 'direction',
                  'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb',
                  'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop', 'at': 'stop', 'it': 'stop',
                  'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun'}

    def convert_to_number(string):
        try:
            return int(string)
        except ValueError:
            return None

    for word in words:
        if not convert_to_number(word):
            result = dictionary.get(word.lower(), 'error')
            # yield word_pairs((result, word))
            word_pairs.append((result, word))
        else:
            # yield(('number', word))
            word_pairs.append(('number', word))

    return word_pairs
