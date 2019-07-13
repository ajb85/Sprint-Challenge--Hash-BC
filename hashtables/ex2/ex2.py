#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    for ticket in tickets: # O(n)
        hash_table_insert(ht, ticket.source, ticket.destination)

    start = "NONE"

    for i in range(len(route)):
        route[i] = hash_table_retrieve(ht, start)
        start = route[i]

    return route