---
title: "deductionguidesforstdvalarray(3)"
name: "deductionguidesforstdvalarray"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdvalarray/"
---

deductionguidesforstd::valarray - deductionguidesforstd::valarray
<h2>Synopsis</h2>Defined in header &lt;valarray&gt; 
template&lt;typename T, std::size_t cnt&gt; <i>(since C++17)</i> 
valarray(const T(&amp;)[cnt], std::size_t) -&gt; valarray&lt;T&gt;; 

 
This deduction_guide is provided for std::valarray to allow deduction from array and size (note that deduction from pointer and size is covered by the implicit guides) 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;valarray&gt; 
&nbsp;<wbr>&nbsp;int main() { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a[] = {1, 2, 3}; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::valarray va(a, 3); // uses explicit deduction guide 
&nbsp;<wbr>&nbsp;}
