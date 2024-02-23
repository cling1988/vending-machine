import sys

available_items = ["cola", "pepsi", "milo", "100plus", "latte"]
items_price = {"cola": 10, "pepsi": 10, "milo": 15, "100plus": 8, "latte": 20}
acceptance_notes = [100, 50, 20, 10, 5, 1]
# available_notes = {100: 5, 50: 5, 20: 5, 10: 5, 5: 5, 1: 5}
available_notes = {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 1: 1}


def exchange_note(total_amount):
    result_exchange = []

    for accept_note in acceptance_notes:
        while total_amount >= accept_note:
            if available_notes[accept_note] > 0:
                result_exchange.append(accept_note)
                total_amount -= accept_note
                available_notes[accept_note] -= 1
            else:
                break

    return result_exchange, total_amount


if __name__ == "__main__":
    print("Welcome to ABC vending machine")
    print(f"Available notes in vending machine: {available_notes}")
    print("Menu:")
    for index, item in enumerate(available_items):
        print(f"Select {index} for {item} price {items_price[item]}")
    selected_drink = None
    while selected_drink is None:
        try:
            selected_no = int(input("Please select drink: "))
            selected_drink = available_items[selected_no]
        except (ValueError, IndexError):
            print("Please insert valid menu number")
            selected_drink = None
    print("You entered: " + selected_drink)
    receive_amount = 0
    total_price = items_price[selected_drink]
    received_notes = []
    print(f"Total price: {total_price}")
    print(f"Only accept notes: {acceptance_notes}")
    while total_price > 0:
        try:
            receive = int(input(f"Receive amount:{receive_amount}, remaining amount {total_price}:"))
            if receive in acceptance_notes:
                total_price -= receive
                receive_amount += receive
                received_notes.append(receive)
            else:
                print(f"Invalid note, return note: {receive}")
                print(f"Only accept notes: {acceptance_notes}")
        except ValueError:
            print("Please insert valid amount")

    print(f"Thanks you, receive payment: {receive_amount}")
    for note in received_notes:
        available_notes[note] += 1
    if total_price < 0:
        exchange_amount = total_price * -1
        result, amount = exchange_note(exchange_amount)
        if amount != 0:
            print("Sorry, the machine not enough note to return, transaction cancel")
            print(f"Please receive return: {acceptance_notes}")
            for note in result:
                available_notes[note] += 1
            print(f"Available notes in vending machine: {available_notes}")
            sys.exit()

        for note in result:
            print(f"Please receive return: {note}")
        print(f"Available notes in vending machine: {available_notes}")
