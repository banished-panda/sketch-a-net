# Variables
CC = gcc
CFLAGS = -Wall -Wextra -O2
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin

# Default rule
all: directories net

# Rule for making the directories
directories:
	mkdir -p $(OBJ_DIR) $(BIN_DIR)

# Rule for the program
net: $(OBJ_DIR)/main.o
	$(CC) $(CFLAGS) -o $(BIN_DIR)/net $^

# Rule for object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c -o $@ $<

# Rule to run the program
run: net
	./$(BIN_DIR)/net

# Clean rule
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)
