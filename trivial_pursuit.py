#The function check_winner takes as input a tuple
# with at least 2 lists, but up to a maximum of 6.
#Each list represents one player's current progress
#toward gathering six pieces.
#If no player has all 6 pieces, check_winner should return
#the string, "Keep playing!"

def check_winner(progress):

  for i in range(len(progress)):
    if len(progress[i]) == 6:
      return "Player {} wins!".format(i + 1)
  return "Keep playing!"

winning_player = ["Red", "Orange", "Yellow", "Purple", "Green", "Blue"]
losing_player_a = []
losing_player_b = ["Red", "Orange"]
losing_player_c = ["Yellow", "Purple", "Green", "Blue"]

print(check_winner((winning_player, losing_player_a, losing_player_b)))
print(check_winner((losing_player_a, losing_player_b, losing_player_c)))
print(check_winner((losing_player_b, losing_player_c, winning_player)))