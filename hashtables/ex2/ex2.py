#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create dict for tickets with source as key and desti
    tickets_lookup = {}
    # create list for combined route
    combined_route = []
    # add each ticket into dict with sources as key and destination as value
    for ticket in tickets:
        tickets_lookup[ticket.source] = ticket.destination

    # add the first ticket to the route by finding source of none
    prev_ticket = tickets_lookup["NONE"]
    combined_route.append(prev_ticket)
    # set next_ticket based off of original
    next_ticket = tickets_lookup[prev_ticket]
    i = 0
    # loop over tickets and add to route list
    while i < len(tickets)-1:
        combined_route.append(next_ticket)
        prev_ticket = next_ticket
        next_ticket = tickets_lookup[next_ticket]
        i += 1

    return combined_route
