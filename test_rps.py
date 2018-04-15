from boa.interop.Neo.Storage import Get, Put, Delete, GetContext
from boa.interop.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.interop.Neo.Blockchain import GetTransaction, GetHeight, GetBlock
from boa.builtins import breakpoint
from boa.interop.Neo.Runtime import Log

NEO = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
GAS = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'


def Main(hand):
    context = GetContext()

    Log("Neo")
    # txn_cost = get_asset_attachments()
    # Log(txn_cost)

    print("Playing " + hand)
    current_hand = Get(context, "hand")

    amount = Get(context, "amount")
    # if not amount:
    #     Put(context, "amount", txn_cost)
    # else:
    #     Put(context, "amount", txn_cost + amount)

    if not current_hand:
        Put(context, "hand", hand)
        print("Played " + hand + ", waiting for next hand.")
        return True
    else:
        battle = Get(context, "hand")
        if (hand == "rock" and battle == "paper") or (hand == "paper" and battle == "scissor") or (hand == "scissor" and battle == "rock"):
            print("You lose!")
        elif (hand == "scissor" and battle == "paper") or (hand == "paper" and battle == "rock") or (hand == "rock" and battle == "scissor"):
            print("You win!")
        else:
            print("Draw!")

        Delete(context, "hand")
        Delete(context, "amount")
        return True


#
# def get_asset_attachments():
#     """
#     Gets information about NEO and Gas attached to an invocation TX
#
#     :return:
#         list: A list with information about attached neo and gas
#     """
#
#     block = GetBlock(GetHeight())
#     varia = block["tx"][0]
#     # test = block.tx[0]
#     breakpoint()
#     #
#     # for a in block.tx:
#     #     print(a)
#     #     breakpoint()
#
#     return True
#     # for txn in txns:
#     #     tx = GetTransaction(txn)
#     #     references = tx.References
#     #
#     #     receiver_addr = GetExecutingScriptHash()
#     #     # sender_addr = None
#     #     sent_amount_neo = 0
#     #     sent_amount_gas = 0
#     #
#     #     if len(references) > 0:
#     #
#     #         reference = references[0]
#     #         # sender_addr = reference.ScriptHash
#     #         for output in tx.Outputs:
#     #             if output.ScriptHash == receiver_addr:
#     #                 if output.AssetId == NEO:
#     #                     sent_amount_neo += output.Value
#     #                 if output.AssetId == GAS:
#     #                     sent_amount_gas += output.Value
#     #
#     #     return sent_amount_neo
#     # return [receiver_addr, sender_addr, sent_amount_neo, sent_amount_gas]
#

#
# def Main(operation, arg, val):
#
#
#     print("context")
#     print(context)
#
#     if operation == 'sget':
#
#         return Get(context, arg)
#
#     elif operation == 'sput':
#
#         Put(context, arg, val)
#         return True
#
#     elif operation == 'sdel':
#
#         Delete(context, arg)
#         return True
#
#     return 'unknown operation'
