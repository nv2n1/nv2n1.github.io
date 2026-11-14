---
title: "stdexperimentalshuffle(3)"
name: "stdexperimentalshuffle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshuffle/"
---

std::experimental::shuffle - std::experimental::shuffle

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / algorithm&gt;

    template &lt;class RandomIt&gt;
    (library fundamentals TS v2)

        void shuffle(RandomIt first, RandomIt last);</code></pre> 
Reorders the elements in the given range [first, last) such that each possible permutation of those elements has equal probability of appearance, using the per-thread_random_number_engine as the random number generator. 

<h2>Parameters</h2>

first, last - the range of elements to shuffle randomly 
- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Linear in the distance between first and last.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

random_shuffle 
shuffle randomly re-orders elements in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(until C++17)</i> 
<i>(C++11)</i> 
