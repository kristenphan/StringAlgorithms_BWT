# SuffixArrays: Build Burrows-Wheeler Transform (BWT) - Slow Implementation

"__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/specializations/data-structures-algorithms. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)
<br/>
<br/>
__Assignment Description:__
<br/>
Problem Introduction:
Our goal is to further improve on the memory requirements of the suffix array.
Given a string Text, form all possible cyclic rotations of Text; a cyclic rotation is defined by chopping off
a suffix from the end of Text and appending this suffix to the beginning of Text. Next — similarly to suffix
arrays — order all the cyclic rotations of Text lexicographically to form a |Text| × |Text| matrix of symbols
that we call the Burrows–Wheeler matrix and denote by 𝑀(Text).
<br/>
<br/>
Note that the first column of 𝑀(Text) contains the symbols of Text ordered lexicographically. In turn,
the second column of 𝑀(Text) contains the second symbols of all cyclic rotations of Text, and so it too
represents a (different) rearrangement of symbols from Text. The same reasoning applies to show that any
column of 𝑀(Text) is some rearrangement of the symbols of Text. We are interested in the last column of
𝑀(Text), called the Burrows–Wheeler transform of Text, or BWT(Text).
<br/>
<br/>
Task: Construct the Burrows–Wheeler transform of a string.
<br/>
<br/>
Input Format: A string Text ending with a “$” symbol.
<br/>
<br/>
Constraints: 1 ≤ |Text| ≤ 1 000; except for the last symbol, Text contains symbols A, C, G, T only.
<br/>
<br/>
Output Format: BWT(Text).
<br/>
<br/>
Time Limits: Python - 0.5 seconds
<br/>
<br/>
Memory Limits: 512 MB

