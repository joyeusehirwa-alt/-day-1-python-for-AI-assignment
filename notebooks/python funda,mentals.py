# 1. Five Types & Types Check
s, i, f, b, n = "resnet", 10, 0.95, True, None
print(type(s), type(i), type(f), type(b), type(n))

# 2. Casting (Casting float to int truncates/cuts off the decimal part entirely)
f_val = float("87.65")
i_val = int(f_val)  # Decimals removed: 87.65 becomes 87
print(f"Float: {f_val}, Int: {i_val}")

# 3. f-string Report
model, acc, epoch = "BERT", 0.9345, 15
print(f"Model {model} hit {acc:.2%} accuracy in {epoch} epochs.")

# 4. Conditional
acc, latency = 0.92, 45
if acc >= 0.90 and latency <= 50:
    print("ship it")
elif latency > 50:
    print("too slow")
else:
    print("keep training")

# 5. Loop with enumerate()
scores = [0.72, 0.81, 0.88, 0.93]
for epoch, score in enumerate(scores, start=1):
    print(f"Epoch {epoch}: {score}")

# 6. Collections
loss_list = [0.5, 0.3, 0.2]  # List: ordered & mutable; perfect for sequential metrics
img_shape = (224, 224, 3)    # Tuple: immutable; ideal for fixed image dimensions
params = {"lr": 0.001}       # Dict: key-value pairs; ideal for structured hyperparameters
classes = {"cat", "dog"}     # Set: unique items; ideal for distinct label sets

# 7. Comprehensions
passing = [s for s in scores if s > 0.80]
formatted = {f"ep_{i}": f"{s:.1%}" for i, s in enumerate(scores)}
print(f"Filtered: {passing}\nDict: {formatted}")