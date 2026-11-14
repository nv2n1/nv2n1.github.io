---
title: "deductionguidesforstdbasic_regex(3)"
name: "deductionguidesforstdbasic_regex"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdbasic_regex/"
---

deductionguidesforstd::basic_regex - deductionguidesforstd::basic_regex
<h2>Synopsis</h2>Defined in header &lt;regex&gt; 
template&lt;class ForwardIt&gt; 
basic_regex(ForwardIt, ForwardIt, <i>(since C++17)</i> 
std::regex_constants::syntax_option_type = std::regex_constants::ECMAScript) 
-&gt; basic_regex&lt;typename std::iterator_traits&lt;ForwardIt&gt;::value_type&gt;; 

 
This deduction_guide is provided for std::basic_regex to allow deduction from an iterator range. 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;regex&gt; 
&nbsp;<wbr>&nbsp;#include &lt;vector&gt; 
&nbsp;<wbr>&nbsp;int main() { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;char&gt; v = {'a', 'b', 'c'}; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::basic_regex re{v.begin(), v.end()}; // uses explicit deduction guide 
&nbsp;<wbr>&nbsp;}
