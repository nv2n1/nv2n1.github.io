---
title: "deductionguidesforstdoptional(3)"
name: "deductionguidesforstdoptional"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdoptional/"
---

deductionguidesforstd::optional - deductionguidesforstd::optional
<h2>Synopsis</h2>Defined in header &lt;optional&gt; 
template&lt;class T&gt; <i>(since C++17)</i> 
optional(T) -&gt; optional&lt;T&gt;; 

 
One deduction_guide is provided for std::optional to account for the edge cases missed by the implicit deduction guides, in particular, non-copyable arguments and array to pointer conversion 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;optional&gt; 

 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a[2]; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::optional oa{a}; // explicit deduction guide is used in this case 
&nbsp;<wbr>&nbsp;}
