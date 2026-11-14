---
title: "stdhashstdbitset(3)"
name: "stdhashstdbitset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdbitset/"
---

std::hash(std::bitset) - std::hash(std::bitset)

<h2>Synopsis</h2>

template&lt;size_t N&gt; struct hash&lt;bitset&lt;N&gt;&gt;; <i>(since C++11)</i> 
The template specialization of std::hash for std::bitset&lt;N&gt; allows users to obtain hashes of objects of type std::bitset&lt;N&gt;. 

<h2>Example</h2>

The following code shows one possible output of a hash function used on several bitsets: 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;

#include &lt;functional&gt;
int main()

{
    std::bitset&lt;4&gt; b1(1);
    std::bitset&lt;4&gt; b2(2);
    std::bitset&lt;4&gt; b3(b2);
    std::hash&lt;std::bitset&lt;4&gt;&gt; hash_fn;
    size_t h1 = hash_fn(b1);
    size_t h2 = hash_fn(b2);
    size_t h3 = hash_fn(b3);
    std::cout &lt;&lt; h1 &lt;&lt; '\n';
    std::cout &lt;&lt; h2 &lt;&lt; '\n';
    std::cout &lt;&lt; h3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;67918732 
&nbsp;<wbr>&nbsp;118251589 
&nbsp;<wbr>&nbsp;118251589

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
