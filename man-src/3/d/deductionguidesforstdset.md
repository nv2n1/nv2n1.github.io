---
title: "deductionguidesforstdset(3)"
name: "deductionguidesforstdset"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdset/"
description: "deductionguidesforstd::set – deductionguidesforstd::set"
---

<p>deductionguidesforstd::set &#8211; deductionguidesforstd::set</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;set&gt;<br />
template&lt;class InputIt,<br />
class Comp = std::less&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
class Alloc = std::allocator&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;&gt; <code>(1)</code> <i>(since C++17)</i><br />
set(InputIt, InputIt, Comp = Comp(), Alloc = Alloc())<br />
-&gt; set&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, Comp, Alloc&gt;;<br />
template&lt;class Key, class Comp = std::less&lt;Key&gt;, class Alloc = std::allocator&lt;Key&gt;&gt;<br />
set(std::initializer_list&lt;Key&gt;, Comp = Comp(), Alloc = Alloc()) <code>(2)</code> <i>(since C++17)</i><br />
-&gt; set&lt;Key, Comp, Alloc&gt;;<br />
template&lt;class InputIt, class Alloc&gt;<br />
set(InputIt, InputIt, Alloc) <code>(3)</code> <i>(since C++17)</i><br />
-&gt; set&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type,<br />
std::less&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;, Alloc&gt;;<br />
template&lt;class Key, class Alloc&gt;<br />
set(std::initializer_list&lt;Key&gt;, Alloc) <code>(4)</code> <i>(since C++17)</i><br />
-&gt; set&lt;Key, std::less&lt;Key&gt;, Alloc&gt;; </p>
<p>These deduction_guides are provided for set to allow deduction from an iterator range (overloads (1,3)) and std::initializer_list (overloads (2,4)). These overloads only participate in overload resolution if InputIt satisfies LegacyInputIterator, Alloc satisfies Allocator, and Comp does not satisfy Allocator.<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;set&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::set s = {1,2,3,4}; // guide #2 deduces std::set&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::set s2(s.begin(), s.end()); // guide #1 deduces std::set&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;}</p>
