from collections import deque

def is_one_letter_diff(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
        if count > 1:
            return False
    return count == 1

def bfs_word_ladder(start, end, word_list):
    if end not in word_list:
        print("End word not in dictionary. No transformation possible.")
        return

    queue = deque([[start]])  # Queue stores paths
    visited = set([start])

    while queue:
        path = queue.popleft()
        word = path[-1]
        if word == end:
            print("Shortest transformation path found:")
            print(" → ".join(path))
            return
        for next_word in word_list:
            if next_word not in visited and is_one_letter_diff(word, next_word):
                visited.add(next_word)
                new_path = list(path)
                new_path.append(next_word)
                queue.append(new_path)

    print("No valid transformation found.")
  
if __name__ == "__main__":
    print("WORD LADDER PUZZLE SOLVER USING BFS ALGORITHM")
    print("--------------------------------------------")
    start_word = "hit"
    end_word = "cog"
    dictionary = {"hot", "dot", "dog", "lot", "log", "cog"}

    bfs_word_ladder(start_word, end_word, dictionary)
