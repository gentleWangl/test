import random
from matplotlib import pyplot as plt

def next_state(now_state, matrix):
    p = random.uniform(0, 1)
    if p <= matrix[now_state][0]:
        return 0
    elif p <= matrix[now_state][0] + matrix[now_state][1]:
        return 1
    else:
        return 2

matrix = [[0.2, 0.6, 0.2], [0.3, 0, 0.7], [0.5, 0, 0.5]]
state_sum = [0] * 3
steps = 100001
now_state = 0  # Hamburger
probablity = [[] for _ in range(3)]  # Correctly initialize the list of lists

for step in range(1, steps):
    now_state = next_state(now_state, matrix)
    state_sum[now_state] += 1
    for i_state in range(3):
        probablity[i_state].append(state_sum[i_state] / step)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(list(range(steps - 1)), probablity[0], label='Hamburger', linewidth=2)
plt.plot(list(range(steps - 1)), probablity[1], label='Pizza', linewidth=2)
plt.plot(list(range(steps - 1)), probablity[2], label='Hot Dog', linewidth=2)

# Adding titles and labels
plt.title('Probability Distribution Over Time for Each State')
plt.xlabel('Steps')
plt.ylabel('Probability')

# Adding grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Adding legend with a shadow
plt.legend(title='States', shadow=True, loc='upper right')

# Show plot
plt.show()

# Print final probabilities
print(f"Humburger: {state_sum[0] / (steps - 1):.5f}\t Pizza: {state_sum[1] / (steps - 1):.5f}\t Hot Dog: {state_sum[2] / (steps - 1):.5f}")



