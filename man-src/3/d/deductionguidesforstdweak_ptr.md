---
title: "deductionguidesforstdweak_ptr(3)"
name: "deductionguidesforstdweak_ptr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdweak_ptr/"
---

deductionguidesforstd::weak_ptr - deductionguidesforstd::weak_ptr
<h2>Synopsis</h2>Defined in header &lt;memory&gt; 
template&lt;class T&gt; <i>(since C++17)</i> 
weak_ptr(std::shared_ptr&lt;T&gt;) -&gt; weak_ptr&lt;T&gt;; 

 
One deduction_guide is provided for std::weak_ptr to account for the edge case missed by the implicit deduction guides. 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;memory&gt; 

 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = std::make_shared&lt;int&gt;(42); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::weak_ptr w{p}; // explicit deduction guide is used in this case 
&nbsp;<wbr>&nbsp;}
