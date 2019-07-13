# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts: Hash tables (24 points), blockchain (12 points) and a short interview (20 points). There is also a stretch goal in the blockchain section which should only be attempted after the rest of the problems have been completed.

## Interview Questions

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following three questions:

- 1. What is a blockchain and how does it work?
     Blockchains mimic a linked list in appearance (though in reverse, as they link backward) and starts at the Genesis block. A hash is stored on each node, or block, as well as the hash of the previous block (in addition to whatever info you'd like to store on the block, like a transaction). That creates the link between them, and perhaps more important, makes tampering with a block more difficult. As tampering with the block changes the hash and can disconnect the chain. Also a key security measure for a blockchain is distribution--the more PCs have a copy of the chain, the more secure it becomes. Tampering with the chain requires both updating the entire chain (to prevent disconnect from the link to previous hash) and distributing it widely enough to overtake the majority. Otherwise, your tampered with blocks will simply be rejected by the other (presumably valid) chains. In order for a new block to be added (and accepted) by the chain, proof of work must be completed. This generally means finding a solution to an algorithm that requires a heavy amount of computing power. The difficulty in unlocking a block is what gives the currency its value. Solve a time-consuming algorithm, get your coin!
- 2. What is an array and how does it work?
     Arrays are a contiguous block of memory that link data together through adjacency. Say an index in the array is going to take X space in memory, then accessing the 5th index simply requires X _ 5. This is a key aspect in why the first index in an array is zero: X _ 0. However, since an array only works if it is contiguous, if an array becomes too large for the allocated slot in memory, it must be rewritten somewhere else in memory that has a larger amount of free (continuous) space.
- 3. What is a hash table and how does it work?
     A hash table is an array however, the string keys used in place of an index are ran through a hash function to turn them into an index. When a duplicate index is used, the items are linked via a linked list to prevent erasing data. The hash function used is critical since a poor function will result in poor distribution and longer linked lists to sift through. Naturally if the hash function is slow, runtime performance will suffer potentially dramatically as hash tables are incredibly common. A djb2 is a common hash function used because it's fast and creates a wide distribution. It's able to do this through two key numbers: 5318 and 33. The first has four key factors that make it good for distributing indices: it's odd, prime, deficient, and bitmasked. 33 has similar properties and while other numbers would work well, 33 is a "magic constant" that tends to perform best.

You will receive points at the PM's discretion based on the following criteria:

- 20: Would love to have this person on my team!
- 14: Wouldn't mind working with this person.
- 10: Knowledge is lacking OR poor communication skills
- 6: Knowledge is lacking AND poor communication skills
- 2: You get 2 points for showing up

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (ideally using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

_You may not use any advanced built-in Python functions to solve these problems._

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin. Keep in mind that with many people competing over the same coins, this may take a long time. By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.

## Minimum Viable Product

You can earn 35 points from the main coding portion of the sprint challenge. Be sure to budget your time wisely. The Blockchain challenge is fun, but it is only 1/3 of the points availible for the coding portion of this challenge.

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain) - 12 pts

- ex1 - 12 pts

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables) - 24 pts

- ex1 - 12 pts
- ex2 - 12 pts

Both Hash Table problems will be graded as follows:

- 1: Code attempted
- 2: Code resembles the correct solution
- 3: Tests pass
- 4: Tests pass, using the existing hash table implementation, no flake8 complaints
- 5: Tests pass, using the existing hash table implementation, no flake8 complaints, linear runtime complexity

### Grading

Students can receive up to 55 points in total for this Sprint Challenge (not including 4 extra credit points).

- **Challenge**: 35
- **Interview**: 20

---

The score distributions are as follows:

- **3**: >= 48 points
- **2**: >= 35 points
- **1**: < 34 points
