import matplotlib.pyplot as plt

# Encoder and decoder node positions
encoder_y = [4, 3, 2, 1]
decoder_y = [4, 3, 2, 1]

encoder_x = 0.2
decoder_x = 0.8

plt.figure(figsize=(10, 6))
plt.title("Transformer Encoder-Decoder Architecture (Red = Attention)")

# Draw encoder nodes
for i, y in enumerate(encoder_y):
    plt.scatter(encoder_x, y, s=600, color='blue', edgecolor="black")
    plt.text(encoder_x, y, f"Encoder L{i+1}", ha="center", va="center", fontsize=10)

# Draw decoder nodes
for i, y in enumerate(decoder_y):
    plt.scatter(decoder_x, y, s=600, color='green', edgecolor="black")
    plt.text(decoder_x, y, f"Decoder L{i+1}", ha="center", va="center", fontsize=10)

# Draw vertical encoder & decoder connections
for i in range(3):
    plt.plot([encoder_x, encoder_x], [encoder_y[i], encoder_y[i+1]], color="black")
    plt.plot([decoder_x, decoder_x], [decoder_y[i], decoder_y[i+1]], color="black")

# Draw attention connections (red dashed lines)
for ey in encoder_y:
    for dy in decoder_y:
        plt.plot([encoder_x, decoder_x], [ey, dy], "--", color="red", linewidth=1)

plt.xlim(0, 1)
plt.ylim(0.5, 4.5)
plt.axis("off")
plt.show()