def RPS_Winner(one, two):
    if (one == two):
        return "tie"
    elif (one == "rock" and two == "scissors"):
        return "Player 1"
    elif (one == "scissors" and two == "paper"):
        return "Player 1"
    elif (one == "paper" and two == "rock"):
        return "Player 1"
    return "Player 2"

print(RPS_Winner("paper", "scissors"))
