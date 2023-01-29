should_continue = True
highest_amount = 0
while should_continue:
    name = input('What is your name? ')
    amount = int(input('How much are you willing to pay for this product? $'))
    if amount > highest_amount:
        winner_name = name
        highest_amount = amount
    if input('If there is any other person willing to bid type "y" else press "n"  ') == "y":
        should_continue = True
    else:
        print(
            f'The winner of the bid is {winner_name} who is willing to pay ${highest_amount} for the product')
        should_continue = False
