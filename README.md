# 💖 Love Score Calculator

A fun Python script that calculates a "Love Score" between two names based on the number of matching letters with the words **TRUE** and **LOVE**. Inspired by the classic love compatibility games, this project is purely for entertainment!

---

## 📌 Overview

The program analyzes two names by:
1. Concatenating them.
2. Counting how many times the letters in the word `"TRUE"` and `"LOVE"` appear in the combined name.
3. Summing the counts for each word.
4. Combining the two sums to generate a final "Love Score".

> For example:  
> `Kanye West` + `Kim Kardashian`  
> will produce a love score like `57`.

---

## 🧮 How It Works

### 🔹 `count(test_word, name1, name2)`
- Converts both names to lowercase and combines them.
- Loops through each character in `test_word` (i.e., `"TRUE"` or `"LOVE"`).
- Counts how many times each letter appears in the combined name.
- Returns a list of counts per letter.

### 🔹 `calculate_love_score(name1, name2)`
- Calls `count()` twice: once with `"TRUE"` and once with `"LOVE"`.
- Adds the counts separately for `"TRUE"` and `"LOVE"`.
- Combines them into a string (e.g., 5 and 7 becomes `"57"`).
- Returns the final score as a string.

---

## 🖥️ Example Output

```python
print(calculate_love_score("Kanye West", "Kim Kardashian"))
# Output: 57
```

## 👨‍💻 Author
Arghyajyoti Samui  

GitHub: @Arghyajyoti007  

## Note: This project is just for fun and has no scientific basis! 😄
