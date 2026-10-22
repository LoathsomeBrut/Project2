# Step 1
print("===== Platform Adventure =====")
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

for i in range(0, 5):
    print(f'\nLevels: {levels[i]} \nCoins: {coins[i]} \nEnemies: {enemies[i]} \nPower-ups: {power_ups[i]}')

# Step 2
player_name = "Hero"
lives = 3
score = 0
total_coins = 0
print("\n===== Player Information =====")
print(f'Player: {player_name} \nLives: {lives} \nScore: {score} \nTotal Coins: {total_coins}')

# Step 3
level_scores = []
for i in range(0, 5):
    score = (coins[i]) * 10 -(enemies[i]) * 5
    if power_ups[i] == "Star":
        score = score + 25
    level_scores.append(score)

print("\n===== Level Scores =====")
for i in range(0, 5):
    print(f'Level: {levels[i]} Score: {level_scores[i]}')

# Step 4
actions = [0, 1, 0, 2, 1]
action_results = []
for i in range(0, 5):
    if actions[i] == 0:
        action_results.append("Collect Coins")
    elif actions[i] == 1:
        action_results.append("Fight Enemies")
    else:
        action_results.append("Use Power-Up")
print("\n===== Adventure Actions =====")
for i in range(0, 5):
    print(f'Level {levels[i]}: {action_results[i]}')

# Step 5
life_history = []
lives = 3
for i in range(0, 5):
    if power_ups[i] == "Star":
        lives = lives
    elif enemies[i] >= 4:
        lives = lives - 1
    elif enemies[i] < 4:
        lives = lives
    life_history.append(lives)

print("\n===== Life History =====")
for i in range(0, 5):
    print(f'After Level {levels[i]}: {life_history[i]} lives')

# Step 6
coin = 0
for i in range(0, 5):
    coin = coin + coins[i]
print("\n===== Coin Collection =====")
print(f'Coins collected: {coin}')
bonus_coin_levels = [coin for coin in coins if coin >= 7]
print(f'Levels with 7 or more coins: {bonus_coin_levels}')

# Step 7
print("\n===== Power-Up Inventory =====")
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
starting_inventory = inventory.copy()

inventory.pop(0)
inventory.pop(0)

print(f'Starting Inventory: {starting_inventory} \nUsed Power-Ups: {used_powerups} \nRemaining Inventory: {inventory}')

# Step 8
print("\n===== Level Analysis =====")
print(f'Total Coins: {(sum(coins))} '
      f'\nMost Coins in one Level: {max(coins)} '
      f'\nFewest Coins in one Level: {min(coins)} '
      f'\nAverage Coins per Level: {sum(coins) / len(coins)} '
      f'\nTotal Enemies: {(sum(enemies))} '
      f'\nMost Enemies in one Level: {max(enemies)} ')

# Step 9
total_level_scores = [score for score in level_scores if score >= 50]
print(f'\n===== High Scores =====')
print(f'Scores of 50 or Higher: {total_level_scores}')

# Step 10
print("\n===== Score History =====")
score_history = []
total_score = 0
for i in range(0, 5):
    total_score = total_score + level_scores[i]
    score_history.append(total_score)
    print(f'After Level {levels[i]}: {score_history[i]}')
print(f'\nFirst Two Scores: {score_history[0:2]}')
print(f'Last Two Scores: {score_history[-2:]}')

# Step 11
print("\n===== Final Status =====")
rank = ""
for i in range(0, 5):
    if lives == 0:
        rank = "Game Over"
    elif total_score >= 250:
        rank = "Adventure Champion"
    elif total_score >= 150:
        rank = "Great Adventure"
    else:
        rank = "Keep Practicing"
print(rank)

# Step 12
print("\n===== Adventure Ranking =====")
print(f'Final Score: {max(score_history)}'
      f'\nFinal Lives: {min(life_history)}'
      f'\nRank: Legend')

