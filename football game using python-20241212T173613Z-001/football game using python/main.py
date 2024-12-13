def result(team1, team2):
    if(team1 > team2):
        return 1

    elif (team1<team2):
        return -1

first_team_list = []
second_team_list = []
round = int(input("Enter Rounds..\n"))
i = 0
# while(i != round):     
for i in range(round):
    first_team_round_1 = int(input(f"Enter your score of first team reached in a {i+1} round: "))
    second_team_round_1 = int(input(f"Enter your score of second team reached in a {i+1} round: "))
    first_team_list.append(first_team_round_1)
    second_team_list.append(second_team_round_1)
    i = i+1


score1 = sum(first_team_list)
score2 = sum(second_team_list)

final = result(score1,score2)

print(f"The score of first team {score1} ")
print(f"The score of second team {score2} ")


if(final == 1):
    print("First team win the match....")

elif(final == -1):
    print("Second team win the match...")

else:
    print("Match draw...")