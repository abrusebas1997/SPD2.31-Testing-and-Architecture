def calc_area_under_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max(array):
    max_val = array[0]
    for value in array:
        if value > max_val:
            mmax_val = value
    return max_val


li = [5, -1, 43, 32, 87, -100]
print(get_max(li))

############################
def split_word_by_whitespace(sentence):
    return sentence[0:].split(' ')

print(split_word_by_whitespace('If you were a vegetable, you’d be a ‘cute-cumber.'))
