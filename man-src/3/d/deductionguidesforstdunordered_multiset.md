---
title: "deductionguidesforstdunordered_multiset(3)"
name: "deductionguidesforstdunordered_multiset"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdunordered_multiset/"
description: "deductionguidesforstd::unordered_multiset – deductionguidesforstd::unordered_multiset"
---

<p>deductionguidesforstd::unordered_multiset &#8211; deductionguidesforstd::unordered_multiset</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;unordered_set&gt;<br />
template&lt;class InputIt,<br />
class Hash = std::hash&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
class Pred = std::equal_to&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
class Alloc = std::allocator&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;&gt; <code>(1)</code> <i>(since C++17)</i><br />
unordered_multiset(InputIt, InputIt,<br />
typename /*see below*/::size_type = /*see below*/,<br />
Hash = Hash(), Pred = Pred(), Alloc = Alloc())<br />
-&gt; unordered_multiset&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, Hash, Pred, Alloc&gt;;<br />
template&lt;class T,<br />
class Hash = std::hash&lt;T&gt;,<br />
class Pred = std::equal_to&lt;T&gt;,<br />
class Alloc = std::allocator&lt;T&gt;&gt; <code>(2)</code> <i>(since C++17)</i><br />
unordered_multiset(std::initializer_list&lt;T&gt;,<br />
typename /*see below*/::size_type = /*see below*/,<br />
Hash = Hash(), Pred = Pred(), Alloc = Alloc())<br />
-&gt; unordered_multiset&lt;T, Hash, Pred, Alloc&gt;;<br />
template&lt;class InputIt, class Alloc&gt;<br />
unordered_multiset(InputIt, InputIt, typename /*see below*/::size_type, Alloc)<br />
-&gt; unordered_multiset&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, <code>(3)</code> <i>(since C++17)</i><br />
std::hash&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
std::equal_to&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
Alloc&gt;;<br />
template&lt;class InputIt, class Hash, class Alloc&gt;<br />
unordered_multiset(InputIt, InputIt, typename /*see below*/::size_type, Hash, Alloc) <code>(4)</code> <i>(since C++17)</i><br />
-&gt; unordered_multiset&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, Hash,<br />
std::equal_to&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;, Allocator&gt;;<br />
template&lt;class T, class Allocator&gt;<br />
unordered_multiset(std::initializer_list&lt;T&gt;, typename /*see below*/::size_type, Allocator) <code>(5)</code> <i>(since C++17)</i><br />
-&gt; unordered_multiset&lt;T, std::hash&lt;T&gt;, std::equal_to&lt;T&gt;, Alloc&gt;;<br />
template&lt;class T, class Hash, class Alloc&gt;<br />
unordered_multiset(std::initializer_list&lt;T&gt;, typename /*see below*/::size_type, Hash, Alloc) <code>(6)</code> <i>(since C++17)</i><br />
-&gt; unordered_multiset&lt;T, Hash, std::equal_to&lt;T&gt;, Alloc&gt;; </p>
<p>These deduction_guides are provided for unordered_multiset to allow deduction from an iterator range (overloads (1,3,4)) and std::initializer_list (overloads (2,5.6)). This overload only participates in overload resolution if InputIt satisfies LegacyInputIterator, Alloc satisfies Allocator, neither Hash nor Pred satisfy Allocator, Hash is not an integral type<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand.<br />
The size_type parameter type in these guides refers to the size_type member type of the type deduced by the deduction guide. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;unordered_set&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::unordered_multiset s = {1,2,3,4}; // guide #2 deduces std::unordered_multiset&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::unordered_multiset s2(s.begin(), s.end()); // guide #1 deduces std::unordered_multiset&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;}</p>
