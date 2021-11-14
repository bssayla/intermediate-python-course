def main():
  import random
  player_name = input("What is your name? ")
  player_score = 0
  dice_size = int(input("How many sides does your dice have? "))
  dice_rolls = int(input("How many times do you want to roll the dice? "))
  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f"You rolled a {roll} Critical Fail!")
      player_score -= 1
    elif roll == dice_size:
      print(f"You rolled a {roll} Critical Success!")
      player_score += 1
    else:
      print(f'You rolled a {roll}')
  data_base = open("dice_roller_data.txt", "a")
  data_base.write(f"{player_name} rolled {dice_rolls} times with a {dice_size} sided dice for a total of {dice_sum} points.\n")
  print(f'You rolled a total of {dice_sum} your score is {player_score}')
  

if __name__== "__main__":
  main()