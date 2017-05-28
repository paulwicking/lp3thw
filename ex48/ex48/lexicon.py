def scan(words_to_scan):
    """
    Scan words in lists, return a tuple with word category if found
    rtype: tuple
    """
    words = words_to_scan.split()
    word_pairs = []
    found = False

    # Our word lists _must_ be all lower-case
    directions = ['north', 'south', 'east', 'west']
    verbs = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    
    for word in words:
        found = False
        for item in directions:
            if word.lower() == item:
                word_pairs.append(tuple(['direction', item]))
                found = True
                break
            else:
                continue

        for item in verbs:
            if word.lower() == item:
                word_pairs.append(tuple(['verb', item]))
                found = True
                break
            else:
                continue

        for item in stop_words:
            if word.lower() == item:
                word_pairs.append(tuple(['stop', item]))
                found = True
                break
            else:
                continue

        for item in nouns:
            if word.lower() == item:
               word_pairs.append(tuple(['noun', item]))
               found = True
               break
            else:
                continue

        if word.isdigit():
            word_pairs.append(tuple(['number', word]))

        elif not found:
            word_pairs.append(tuple(['error', word]))

        else:
           continue
 

    return word_pairs

