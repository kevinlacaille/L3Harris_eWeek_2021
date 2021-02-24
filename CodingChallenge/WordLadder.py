class Solution:
    def ladderLength(self, A: str, B: str, C: List[str]) -> int:
        from collections import deque
        dicts = set()
        for i in C:
            dicts.add(i)
            
        if B not in dicts:
            return 0

        q = deque()
        q.append(A)
        level = 1

        while q:
            size = len(q)
            for i in range(size):
                curr_word = q.popleft()
                word_char = [i for i in curr_word]

                for j in range(len(word_char)):
                    original_char = word_char[j]
                    for c in range(97,123):
                        if word_char[j] == chr(c):
                            continue
                            
                        word_char[j] = chr(c)
                        new_word = "".join(word_char)
                        
                        if new_word == B:
                            return level+1
                        
                        if new_word in dicts:
                            q.append(new_word)
                            dicts.remove(new_word)

                    word_char[j] = original_char
                    
            level += 1
        return 0