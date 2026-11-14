---
title: "deductionguidesforstdbasic_string(3)"
name: "deductionguidesforstdbasic_string"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdbasic_string/"
description: "deductionguidesforstd::basic_string – deductionguidesforstd::basic_string"
---

<p>deductionguidesforstd::basic_string &#8211; deductionguidesforstd::basic_string</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;string&gt;<br />
template&lt;class InputIt, class Alloc = std::allocator&lt;<br />
typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;&gt;<br />
basic_string(InputIt, InputIt, Alloc = Alloc()) <code>(1)</code> <i>(since C++17)</i><br />
-&gt; basic_string&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type,<br />
std::char_traits&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;,<br />
Alloc&gt;;<br />
template&lt;class CharT,<br />
class Traits,<br />
class Alloc = std::allocator&lt;CharT&gt;&gt; <code>(2)</code> <i>(since C++17)</i><br />
explicit basic_string(std::basic_string_view&lt;CharT, Traits&gt;, const Alloc&amp; = Alloc())<br />
-&gt; basic_string&lt;CharT, Traits, Alloc&gt;;<br />
template&lt;class CharT,<br />
class Traits,<br />
class Alloc = std::allocator&lt;CharT&gt;&gt;&gt; <code>(3)</code> <i>(since C++17)</i><br />
basic_string(std::basic_string_view&lt;CharT, Traits&gt;, typename /*see below*/::size_type,<br />
typename /*see below*/::size_type, const Alloc&amp; = Alloc())<br />
-&gt; basic_string&lt;CharT, Traits, Alloc&gt;; </p>
<p>1) This deduction_guide is provided for std::basic_string to allow deduction from an iterator range. This overload only participates in overload resolution if InputIt satisfies LegacyInputIterator and Alloc satisfies Allocator.<br />
2-3) These deduction guides are provided for std::basic_string to allow deduction from a std::basic_string_view. The size_type parameter type in <code>(3)</code> refers to the size_type member type of the type deduced by the deduction guide. These overloads only participate in overload resolution if Alloc satisfies Allocator.<br />
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand. </p>
<h2>Notes</h2>
<p>Guides (2-3) are needed because the std::basic_string constructors for std::basic_string_views are made templates to avoid causing ambiguities in existing code, and those templates do not support class template argument deduction. </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_3075 C++17 deduction from basic_string_view was unsupported (exacerbated by LWG_issue_2946) deduction guides added </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;string&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;vector&gt;<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;char&gt; v = {&#8216;a&#8217;, &#8216;b&#8217;, &#8216;c&#8217;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::basic_string s(v.begin(), v.end()); // uses explicit deduction guide<br />
&nbsp;<wbr>&nbsp;}</p>
