---
title: "deductionguidesforstdforward_list(3)"
name: "deductionguidesforstdforward_list"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdforward_list/"
---

deductionguidesforstd::forward_list - deductionguidesforstd::forward_list
<h2>Synopsis</h2>Defined in header &lt;forward_list&gt; 
template&lt; class InputIt, 
class Alloc = std::allocator&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;&gt; <i>(since C++17)</i> 
forward_list(InputIt, InputIt, Alloc = Alloc()) 
-&gt; forward_list&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type, Alloc&gt;; 

 
This deduction_guide is provided for forward_list to allow deduction from an iterator range. This overload only participates in overload resolution if InputIt satisfies LegacyInputIterator and Alloc satisfies Allocator. 
Note: the extent to which the library determines that a type does not satisfy LegacyInputIterator is unspecified, except that as a minimum integral types do not qualify as input iterators. Likewise, the extent to which it determines that a type does not satisfy Allocator is unspecified, except that as a minimum the member type Alloc::value_type must exist and the expression std::declval&lt;Alloc&amp;&gt;().allocate(std::size_t{}) must be well-formed when treated as an unevaluated operand. 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;forward_list&gt; 
&nbsp;<wbr>&nbsp;#include &lt;vector&gt; 
&nbsp;<wbr>&nbsp;int main() { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;int&gt; v = {1, 2, 3, 4}; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// uses explicit deduction guide to deduce std::forward_list&lt;int&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward_list x(v.begin(), v.end()); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// deduces std::forward_list&lt;std::vector&lt;int&gt;::iterator&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// first phase of overload resolution for list-initialization selects the candidate 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// synthesized from the initializer-list constructor; second phase is not performed and 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// deduction guide has no effect 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward_list y{v.begin(), v.end()}; 
&nbsp;<wbr>&nbsp;}
