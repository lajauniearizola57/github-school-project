import pandas as pd
from sklearn.model_selection import train_test_split

# Load and preprocess data
data = pd.read_csv("student_scores.csv")
X = data.drop(columns="student_id")
y = data["student_id"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation="relu", input_shape=(X.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dropout(0.5)
])

# Compile and train the model
model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])
model.fit(X_train, y_train, epochs=10)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")
