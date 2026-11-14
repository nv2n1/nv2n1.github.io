---
title: "deductionguidesforstdunordered_map(3)"
name: "deductionguidesforstdunordered_map"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdunordered_map/"
description: "deductionguidesforstd::unordered_map – deductionguidesforstd::unordered_map"
---

<p>deductionguidesforstd::unordered_map &#8211; deductionguidesforstd::unordered_map</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;unordered_map&gt;<br />
template&lt;class InputIt,<br />
class Hash = std::hash&lt;iter_key_t&lt;InputIt&gt;&gt;,<br />
class Pred = std::equal_to&lt;iter_key_t&lt;InputIt&gt;&gt;,<br />
class Alloc = std::allocator&lt;iter_to_alloc_t&lt;InputIt&gt;&gt;&gt; <code>(1)</code> <i>(since C++17)</i><br />
unordered_map(InputIt, InputIt,<br />
typename /*see below*/::size_type = /*see below*/,<br />
Hash = Hash(), Pred = Pred(), Alloc = Alloc())<br />
-&gt; unordered_map&lt;iter_key_t&lt;InputIt&gt;, iter_val_t&lt;InputIt&gt;, Hash, Pred, Alloc&gt;;<br />
template&lt;class Key, class T, class Hash = std::hash&lt;Key&gt;,<br />
class Pred = std::equal_to&lt;Key&gt;,<br />
class Alloc = std::allocator&lt;std::pair&lt;const Key, T&gt;&gt;&gt;<br />
unordered_map(std::initializer_list&lt;std::pair&lt;Key, T&gt;&gt;, <code>(2)</code> <i>(since C++17)</i><br />
typename /*see below*/::size_type = /*see below*/,<br />
Hash = Hash(), Pred = Pred(), Alloc = Alloc())<br />
-&gt; unordered_map&lt;Key, T, Hash, Pred, Alloc&gt;;<br />
template&lt;class InputIt, class Alloc&gt;<br />
unordered_map(InputIt, InputIt, typename /*see below*/::size_type, Alloc)<br />
-&gt; unordered_map&lt;iter_key_t&lt;InputIt&gt;, iter_val_t&lt;InputIt&gt;, <code>(3)</code> <i>(since C++17)</i><br />
std::hash&lt;iter_key_t&lt;InputIt&gt;&gt;,<br />
std::equal_to&lt;iter_key_t&lt;InputIt&gt;&gt;, Alloc&gt;;<br />
template&lt;class InputIt, class Alloc&gt;<br />
unordered_map(InputIt, InputIt, Alloc)<br />
-&gt; unordered_map&lt;iter_key_t&lt;InputIt&gt;, iter_val_t&lt;InputIt&gt;, <code>(4)</code> <i>(since C++17)</i><br />
std::hash&lt;iter_key_t&lt;InputIt&gt;&gt;,<br />
std::equal_to&lt;iter_key_t&lt;InputIt&gt;&gt;, Alloc&gt;;<br />
template&lt;class InputIt, class Hash, class Alloc&gt;<br />
unordered_map(InputIt, InputIt, typename /*see below*/::size_type, Hash, Alloc) <code>(5)</code> <i>(since C++17)</i><br />
-&gt; unordered_map&lt;iter_key_t&lt;InputIt&gt;, iter_val_t&lt;InputIt&gt;, Hash,<br />
std::equal_to&lt;iter_key_t&lt;InputIt&gt;&gt;, Alloc&gt;;<br />
template&lt;class Key, class T, typename Alloc&gt;<br />
unordered_map(std::initializer_list&lt;std::pair&lt;Key, T&gt;&gt;, <code>(6)</code> <i>(since C++17)</i><br />
typename /*see below*/::size_type, Alloc)<br />
-&gt; unordered_map&lt;Key, T, std::hash&lt;Key&gt;, std::equal_to&lt;Key&gt;, Alloc&gt;;<br />
template&lt;class Key, class T, typename Alloc&gt;<br />
unordered_map(std::initializer_list&lt;std::pair&lt;Key, T&gt;&gt;, Alloc) <code>(7)</code> <i>(since C++17)</i><br />
-&gt; unordered_map&lt;Key, T, std::hash&lt;Key&gt;, std::equal_to&lt;Key&gt;, Alloc&gt;;<br />
template&lt;class Key, class T, class Hash, class Alloc&gt;<br />
unordered_map(std::initializer_list&lt;std::pair&lt;Key, T&gt;&gt;, <code>(8)</code> <i>(since C++17)</i><br />
typename /*see below*/::size_type, Hash, Alloc)<br />
-&gt; unordered_map&lt;Key, T, Hash, equal_to&lt;Key&gt;, Allocator&gt;; </p>
<p>where the type aliases iter_key_t, iter_val_t, iter_to_alloc_t are defined as if as follows </p>
<p>template&lt;class InputIt&gt;<br />
using iter_key_t = std::remove_const_t&lt; (exposition only)<br />
typename std::iterator_traits&lt;InputIt&gt;::value_type::first_type&gt;;<br />
template&lt;class InputIt&gt; (exposition only)<br />
using iter_val_t = typename std::iterator_traits&lt;InputIt&gt;::value_type::second_type;<br />
template&lt;class InputIt&gt;<br />
using iter_to_alloc_t = std::pair&lt;<br />
std::add_const_t&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type::first_type&gt;, (exposition only)<br />
typename std::iterator_traits&lt;InputIt&gt;::value_type::second_type<br />
&gt; </p>
<p>These deduction_guide are provided for unordered_map to allow deduction from an iterator range (overloads (1,3-5)) and std::initializer_list (overloads (2,6-8)). These overloads only participate in overload resolution if InputIt satisfies LegacyInputIterator, Alloc satisfies Allocator, neither Hash nor Pred satisfy Allocator, and Hash is not an integral type.<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand.<br />
The size_type parameter type in these guides in an refers to the size_type member type of the type deduced by the deduction guide. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;unordered_map&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;// std::unordered_map m1 = &#123;&#123;&quot;foo&quot;, 1}, {&quot;bar&quot;, 2}}; // Error: braced-init-list has no type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// cannot deduce pair&lt;Key, T&gt; from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// {&quot;foo&quot;, 1} or {&quot;bar&quot;, 2}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::unordered_map m1 = {std::pair{&quot;foo&quot;, 2}, {&quot;bar&quot;, 3}}; // guide #2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::unordered_map m2(m1.begin(), m1.end()); // guide #1<br />
&nbsp;<wbr>&nbsp;} </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_3025 C++17 initializer-list guides take std::pair&lt;const Key, T&gt; use std::pair&lt;Key, T&gt;</p>
