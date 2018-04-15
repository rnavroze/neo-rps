from boa.interop.Neo.Storage import Get, Put, Delete, GetContext

def Main(hand, txn_cost):
    context = GetContext()

    print(hand)
    current_hand = Get(context, "hand")
    # TODO: saving the current account ID so that if they lose, they lose money

    total_amount = 0
    amount = Get(context, "amount")

    if not amount:
        Put(context, "amount", txn_cost)
    else:
        total_amount = amount + txn_cost
    # TODO: deducting the amount from the account

    if not current_hand:
        Put(context, "hand", hand)
        print("Played " + hand + ", waiting for next hand.")
        return 0
    else:
        Delete(context, "hand")
        Delete(context, "amount")

        if (hand == b"rock" and current_hand == b"paper") or (hand == b"paper" and current_hand == b"scissors") or (hand == b"scissors" and current_hand == b"rock"):
            print("You lose! Amount")
            return -txn_cost
            # TODO: adding the amount to the account
        elif (hand == b"scissors" and current_hand == b"paper") or (hand == b"paper" and current_hand == b"rock") or (hand == b"rock" and current_hand == b"scissors"):
            print("You win!")
            return total_amount
            # TODO: handle deducting money from the user
        else:
            print("Draw!")
            return 0
            # TODO: give both people their money back
