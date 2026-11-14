---
title: "deductionguidesforstdpair(3)"
name: "deductionguidesforstdpair"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdpair/"
---

deductionguidesforstd::pair - deductionguidesforstd::pair
<h2>Synopsis</h2>Defined in header &lt;utility&gt; 
template&lt;class T1, class T2&gt; <i>(since C++17)</i> 
pair(T1, T2) -&gt; pair&lt;T1, T2&gt;; 

 
One deduction_guide is provided for std::pair to account for the edge cases missed by the implicit deduction guides. 
In particular, non-copyable arguments and array to pointer conversion 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;utility&gt; 

 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a[2], b[3]; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::pair p{a, b}; // explicit deduction guide is used in this case 
&nbsp;<wbr>&nbsp;}
