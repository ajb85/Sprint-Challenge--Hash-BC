#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(length): # O(n)
        weight = weights[i]
        pair_weight = limit - weight
        pair_index = hash_table_retrieve(ht, pair_weight)
        if(pair_index != None):
            pairs = (i, pair_index) if i > pair_index else (pair_index, i)
            print_answer(pairs)
            return pairs
        hash_table_insert(ht, weight, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)