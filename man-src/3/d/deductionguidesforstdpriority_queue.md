---
title: "deductionguidesforstdpriority_queue(3)"
name: "deductionguidesforstdpriority_queue"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdpriority_queue/"
description: "deductionguidesforstd::priority_queue – deductionguidesforstd::priority_queue"
---

<p>deductionguidesforstd::priority_queue &#8211; deductionguidesforstd::priority_queue</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;queue&gt;<br />
template &lt;class Compare, class Container&gt;<br />
priority_queue(Compare, Container) <code>(1)</code> <i>(since C++17)</i><br />
-&gt; priority_queue&lt;typename Container::value_type, Container, Compare&gt;;<br />
template&lt;class InputIt,<br />
class Comp = std::less&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
class Container = std::vector&lt;typename iterator_traits&lt;InputIt&gt;::value_type&gt;&gt; <code>(2)</code> <i>(since C++17)</i><br />
priority_queue(InputIt, InputIt, Comp = Comp(), Container = Container())<br />
-&gt; priority_queue&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, Container, Comp&gt;;<br />
template&lt;class Comp, class Container, class Alloc&gt;<br />
priority_queue(Comp, Container, Alloc) <code>(2)</code> <i>(since C++17)</i><br />
-&gt; priority_queue&lt;typename Container::value_type, Container, Comp&gt;; </p>
<p>These deduction_guides are provided for std::priority_queue to allow deduction from underlying container type (overloads (1,3)) and from an iterator range (overload <code>(2)</code>) This overload only participates in overload resolution if InputIt satisfies LegacyInputIterator, Alloc satisfies Allocator, Comp does not satisfy Allocator, Container does not satisfy Allocator and, for overload <code>(3)</code>, if std::uses_allocator_v&lt;Container, Alloc&gt; is true<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;vector&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;queue&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;int&gt; v = {1,2,3,4};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::priority_queue pq1{v}; // deduces std::priority_queue&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::priority_queue pq2{v.begin(), v.end()}; // deduces std::priority_queue&lt;int&gt;<br />
&nbsp;<wbr>&nbsp;}</p>
