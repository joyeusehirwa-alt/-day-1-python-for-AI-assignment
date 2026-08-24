import matplotlib.pyplot as plt

epochs = list(range(1, 9))
train_acc = [0.55, 0.72, 0.84, 0.88, 0.89, 0.89, 0.90, 0.90]
val_acc = [0.50, 0.68, 0.80, 0.81, 0.82, 0.81, 0.82, 0.81]

plt.figure(figsize=(8, 5))
plt.plot(epochs, train_acc, marker='o', label="Training Accuracy")
plt.plot(epochs, val_acc, marker='s', linestyle='--', label="Validation Accuracy")

# Title stating a finding[cite: 1]
plt.title("Validation Accuracy Plateaus After Epoch 4 Indicating Early Overfitting")[cite: 1]
plt.xlabel("Epoch Count")[cite: 1]
plt.ylabel("Accuracy Score")[cite: 1]
plt.legend()[cite: 1]
plt.grid(True, linestyle=':', alpha=0.6)

# Save figure to reports[cite: 1]
plt.savefig("reports/day01_chart.png", dpi=150, bbox_inches="tight")[cite: 1]
plt.show()