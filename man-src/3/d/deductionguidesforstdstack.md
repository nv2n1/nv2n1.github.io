---
title: "deductionguidesforstdstack(3)"
name: "deductionguidesforstdstack"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdstack/"
description: "deductionguidesforstd::stack – deductionguidesforstd::stack"
---

<p>deductionguidesforstd::stack &#8211; deductionguidesforstd::stack</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;stack&gt;<br />
template&lt;class Container&gt;<br />
stack(Container) <code>(1)</code> <i>(since C++17)</i><br />
-&gt; stack&lt;typename Container::value_type, Container&gt;;<br />
template&lt;class Container, class Allocator&gt;<br />
stack(Container, Allocator) <code>(2)</code> <i>(since C++17)</i><br />
-&gt; stack&lt;typename Container::value_type, Container&gt;; </p>
<p>These deduction_guides are provided for stack to allow deduction from underlying container type. This overload only participates in overload resolution if Alloc satisfies Allocator, and Container does not satisfy Allocator and, for overload <code>(2)</code>, if std::uses_allocator_v&lt;Container, Allocator&gt; is true<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;vector&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;stack&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;int&gt; v = {1,2,3,4};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::stack s{v}; // guide #1 deduces std::stack&lt;int, vector&lt;int&gt;&gt;<br />
&nbsp;<wbr>&nbsp;}</p>
