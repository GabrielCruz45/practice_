# 50 Data Structure Exercises — Interview Prep (Python) · Part 1 of 2

Fifty problems, ordered roughly easiest to hardest, moving through structures in the order most interview-prep tracks use: arrays/strings → hashing → linked lists → stacks/queues → trees → heaps → graphs → tries. These are the fundamentals tested across SWE, ML engineering, and data engineering interviews, and they're increasingly showing up in data analyst interviews at bigger companies too — so this is worth having regardless of which direction you end up chasing. Descriptions are short on purpose; look up anything unfamiliar as you go.

**One rule for all 50:** before you call an exercise done, state the time and space complexity of your solution (comment it, say it out loud, whatever). That habit matters more than any single problem on this list.

**Python cheat-sheet:**

| Structure | Python tool |
|---|---|
| Array / List | `list` |
| Stack | `list` (`.append()` / `.pop()`) |
| Queue | `collections.deque` (never a plain list — `.pop(0)` is O(n)) |
| Hash Table / Set | `dict` / `set` |
| Counting | `collections.Counter` |
| Auto-initializing dict | `collections.defaultdict` |
| Heap / Priority Queue | `heapq` (min-heap only — negate values to fake a max-heap) |
| Linked List / Tree / Graph / Trie | no built-in — you write the class |

---

## 1. Arrays & Strings
The foundation everything else builds on. Get comfortable with in-place manipulation and pointers before anything fancier.

- [ ] **1. Reverse an array in place** — Reverse a list without slicing (`[::-1]`) or building a new list. *(Easy · two-pointer swap, O(1) space)*
- [ ] **2. Palindrome check** — Determine if a string reads the same forwards and backwards, ignoring case and non-alphanumeric characters. *(Easy · two-pointer)*
- [ ] **3. Rotate an array by k positions** — Rotate a list right by `k` steps, in place. *(Easy-Medium · try the three-reversal trick)*
- [ ] **4. Remove duplicates from a sorted array** — In place, return the new length. *(Easy · two-pointer / write-index)*
- [ ] **5. Merge two sorted arrays** — Merge into one sorted array. *(Easy-Medium · two-pointer merge)*
- [ ] **6. Pair with target sum (sorted array)** — Find two numbers that add to a target using O(1) extra space. *(Medium · two-pointer — contrast with #9)*
- [ ] **7. Max sum subarray of size k** — Find the maximum sum of any contiguous subarray of exactly `k` elements. *(Medium · fixed sliding window)*
- [ ] **8. Longest substring without repeating characters** — Find the length of the longest substring with no repeats. *(Medium · variable sliding window + hash set)*

## 2. Hashing — Dictionaries & Sets
The single highest-leverage tool in these interviews. Reach for a hash map fast and a lot of "Easy"/"Medium" problems fall quickly.

- [ ] **9. Two Sum** — Find indices of two numbers in an unsorted array that add to a target, in one pass. *(Easy · hash map storing complements — THE classic)*
- [ ] **10. First non-repeating character** — Find the first character in a string that doesn't repeat. *(Easy · hash map counting)*
- [ ] **11. Valid Anagram** — Determine if two strings are anagrams of each other. *(Easy · Counter)*
- [ ] **12. Group Anagrams** — Given a list of strings, group the anagrams together. *(Medium · hash map keyed by a sorted-string or char-count signature)*
- [ ] **13. Find all duplicates in an array** — Return every element that appears more than once, O(n) time. *(Easy-Medium · set)*
- [ ] **14. Longest Consecutive Sequence** — In an unsorted array, find the length of the longest run of consecutive integers, in O(n). *(Medium · hash set — resist the urge to sort)*
- [ ] **15. Subarray Sum Equals K** — Count the contiguous subarrays that sum to `k`. *(Medium-Hard · prefix sum + hash map)*

## 3. Linked Lists
No slicing to hide behind — this is where you actually manipulate pointers.

- [ ] **16. Implement a singly linked list** — `Node` and `LinkedList` classes with `append`, `prepend`, `delete(value)`, and traversal/print. *(Easy · foundation for everything below)*
- [ ] **17. Reverse a linked list, iteratively** — In place, O(1) extra space. *(Easy-Medium)*
- [ ] **18. Reverse a linked list, recursively** — Same result, recursive this time. *(Medium · think about what happens on the call stack)*
- [ ] **19. Detect a cycle** — No extra space. *(Medium · Floyd's fast/slow pointers)*
- [ ] **20. Find the middle node** — One pass. *(Easy-Medium · fast/slow pointers)*
- [ ] **21. Merge two sorted linked lists** — Merge by relinking existing nodes, not building a new list. *(Medium)*
- [ ] **22. Remove the nth node from the end** — Single pass. *(Medium · two-pointer with a gap)*

## 4. Stacks & Queues
LIFO and FIFO, and the handful of problems that show up again and again because of it.

- [ ] **23. Implement a stack** — Using a plain list: `push`, `pop`, `peek`, `is_empty`. *(Easy)*
- [ ] **24. Implement a queue** — Using `collections.deque`: `enqueue`, `dequeue`, `peek`. *(Easy · know why a plain list is the wrong choice here)*
- [ ] **25. Valid Parentheses** — Check whether a string of `()[]{}` is balanced. *(Easy-Medium · classic stack application)*
- [ ] **26. Implement a queue using two stacks** — No deque allowed. *(Medium · structural puzzle)*
- [ ] **27. Evaluate Reverse Polish Notation** — Evaluate a postfix expression using a stack. *(Medium)*
- [ ] **28. Sliding Window Maximum** — Find the max of every size-`k` window as it slides across an array, better than O(nk). *(Hard · monotonic deque)*

## 5. Trees
Recursion stops being abstract once you're climbing a tree with it.

- [ ] **29. Build a binary tree** — Define a `TreeNode` class and construct a small tree by hand. *(Easy)*
- [ ] **30. Traversals: pre/in/post-order** — Implement all three, recursively. *(Easy-Medium · bonus: redo one iteratively with an explicit stack)*
- [ ] **31. Level-order traversal (BFS)** — Traverse level by level using a queue. *(Medium)*
- [ ] **32. Max depth of a binary tree** — Return its height. *(Easy)*
- [ ] **33. Same Tree** — Check whether two binary trees are structurally identical with matching values. *(Easy)*
- [ ] **34. Implement a Binary Search Tree** — `insert` and `search`, preserving the BST property. *(Medium)*
- [ ] **35. Validate a Binary Search Tree** — Check whether a tree satisfies the BST property. *(Medium · watch out — checking only against immediate children isn't enough)*
- [ ] **36. Lowest Common Ancestor (BST)** — Find the LCA of two given nodes. *(Medium)*

## 6. Heaps / Priority Queues
For "give me the top/smallest/running k" problems. Underused by candidates, loved by interviewers.

- [ ] **37. Implement a min-heap from scratch** — Array-based: `heapify_up`, `heapify_down`, `insert`, `extract_min`. *(Medium-Hard · the one everyone's tempted to skip — don't)*
- [ ] **38. K largest elements** — Return the k largest elements of a list, using `heapq`. *(Easy-Medium)*
- [ ] **39. Kth Largest Element in an Array** — Return just the kth largest, unsorted input. *(Medium)*
- [ ] **40. Merge K Sorted Lists** — Merge k sorted lists into one, using a heap. *(Hard)*
- [ ] **41. Find Median from Data Stream** — Support adding numbers and finding the median in O(log n). *(Hard · two heaps, one max one min)*

## 7. Graphs
The most general structure on this list — most of the others are technically special cases of a graph.

- [ ] **42. Represent a graph** — Build an adjacency list (dict of lists) and an adjacency matrix for the same graph; implement `add_edge`. *(Easy)*
- [ ] **43. BFS traversal** — Breadth-first from a given start node. *(Easy-Medium)*
- [ ] **44. DFS traversal** — Depth-first, both recursively and iteratively (explicit stack). *(Medium)*
- [ ] **45. Count connected components** — In an undirected graph. *(Medium)*
- [ ] **46. Detect a cycle in an undirected graph** — DFS-based (or Union-Find, if you want a preview of the algorithms set). *(Medium)*
- [ ] **47. Detect a cycle in a directed graph** — DFS with a recursion-stack / coloring scheme. *(Medium-Hard · the undirected trick won't work here)*
- [ ] **48. Number of Islands** — In a 2D grid of `1`s (land) and `0`s (water), count the islands. *(Hard · grid as an implicit graph, BFS/DFS)*

## 8. Tries & Combined Structures — Capstone
Two problems, but the ones interviewers reach for when they want to see everything above working together.

- [ ] **49. Implement a Trie** — `insert`, `search`, `starts_with` for a prefix tree. *(Medium-Hard)*
- [ ] **50. Design an LRU Cache** — `get` and `put` in O(1), fixed capacity, evicting the least-recently-used entry on overflow. *(Hard · hash map + doubly linked list — ties the whole list together)*

---

Once these are solid, I'll build the 50 algorithms exercises — sorting, searching, recursion, DP, greedy, backtracking — as a natural Part 2.
