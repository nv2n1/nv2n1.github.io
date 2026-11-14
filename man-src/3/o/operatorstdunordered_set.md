---
title: "operatorstdunordered_set(3)"
name: "operatorstdunordered_set"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdunordered_set/"
---

operator==,!=(std::unordered_set) - operator==,!=(std::unordered_set)

<h2>Synopsis</h2>

<pre><code>template &lt;class Key, class Hash, class KeyEqual, class Allocator&gt;

bool operator==(const unordered_set&lt;Key, Hash, KeyEqual, Allocator&gt; &amp;lhs, (1)

                                                                              const unordered_set&lt;Key, Hash, KeyEqual, Allocator&gt; &amp;rhs);

template &lt;class Key, class Hash, class KeyEqual, class Allocator&gt;

bool operator!=(const unordered_set&lt;Key, Hash, KeyEqual, Allocator&gt; &amp;lhs, (2)

                                                                              const unordered_set&lt;Key, Hash, KeyEqual, Allocator&gt; &amp;rhs);</code></pre> 
Compares the contents of two unordered containers. 
The contents of two unordered containers lhs and rhs are equal if the following conditions hold: 
* lhs.size() == rhs.size() 
* each group of equivalent elements [lhs_eq1, lhs_eq2) obtained from lhs.equal_range(lhs_eq1) has a corresponding group of equivalent elements in the other container [rhs_eq1, rhs_eq2) obtained from rhs.equal_range(rhs_eq1), that has the following properties: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::distance(lhs_eq1, lhs_eq2) == std::distance(rhs_eq1, rhs_eq2). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::is_permutation(lhs_eq1, lhs_eq2, rhs_eq1) == true. 
The behavior is undefined if Key is not EqualityComparable. 
The behavior is also undefined if 
hash_function() and key_eq() do 
<i>(until C++20)</i> 
key_eq() does 
<i>(since C++20)</i> not have the same behavior on lhs and rhs or if operator== for Key is not a refinement of the partition into equivalent-key groups introduced by key_eq() (that is, if two elements that compare equal using operator== fall into different partitions) 

<h2>Parameters</h2>

lhs, rhs - unordered containers to compare

<h2>Return value</h2>

1) true if the contents of the containers are equal, false otherwise 
2) true if the contents of the containers are not equal, false otherwise 

<h2>Complexity</h2>

Proportional to N calls to operator== on value_type, calls to the predicate returned by key_eq, and calls to the hasher returned by hash_function, in the average case, proportional to N2 in the worst case where N is the size of the container.
