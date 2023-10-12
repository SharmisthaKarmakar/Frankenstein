def print_payoff_matrix(payoff_matrix):
    print("\tC\t\tD")
    for i in range(len(payoff_matrix)):
        if(i == 0):
            print("C", end="\t")
        else:
            print("D", end="\t")
        for j in range(len(payoff_matrix[i])):
            print(payoff_matrix[i][j], end="\t\t")
        print()

def run_game(payoff_matrix, rounds):
    total_payoff_A = 0
    total_payoff_B = 0
    for i in range(rounds):
        print("Round:", i+1)
        choice_A = input("Enter the choice for player A: ")
        choice_B = input("Enter the choice for player B: ")
        x = ord(choice_A)-3-64
        y = ord(choice_B)-3-64
        payoff_A = payoff_matrix[x][y][0]
        payoff_B = payoff_matrix[x][y][1]
        print("Current payoff:")
        print(f"A = {payoff_A}, B = {payoff_B}")
        total_payoff_A = total_payoff_A + payoff_A
        total_payoff_B = total_payoff_B + payoff_B
        print("Total payoff:")
        print(f"A = {total_payoff_A}, B = {total_payoff_B}")
        print('-'*80)
    print("Game has ended. Total payoff:")
    print(f"A = {total_payoff_A}, B = {total_payoff_B}")
    avg_payoff_A = total_payoff_A/rounds
    avg_payoff_B = total_payoff_B/rounds
    print(f"Average payoff after {rounds} rounds:")
    print(f"A = {avg_payoff_A}, B = {avg_payoff_B}")

print("Sankhadip Bera 20CS8010")
print('-'*80)
payoff_matrix=[[(3,3),(0,5)],[(5,0),(1,1)]]
print()
print('-'*80)
print("The payoff matrix:")
print_payoff_matrix(payoff_matrix)
print('-'*80)
print()
rounds = int(input("Enter no. of rounds = "))
run_game(payoff_matrix, rounds)
'''
    C           D
C   (3, 3)      (0, 5)
D   (5, 0)      (1, 1)
'''