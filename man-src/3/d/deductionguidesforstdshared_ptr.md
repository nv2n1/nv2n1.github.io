---
title: "deductionguidesforstdshared_ptr(3)"
name: "deductionguidesforstdshared_ptr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdshared_ptr/"
description: "deductionguidesforstd::shared_ptr – deductionguidesforstd::shared_ptr"
---

<p>deductionguidesforstd::shared_ptr &#8211; deductionguidesforstd::shared_ptr</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template &lt;class T&gt; <code>(1)</code> <i>(since C++17)</i><br />
shared_ptr(std::weak_ptr&lt;T&gt;) -&gt; shared_ptr&lt;T&gt;;<br />
template &lt;class T, class D&gt; <code>(2)</code> <i>(since C++17)</i><br />
shared_ptr(std::unique_ptr&lt;T, D&gt;) -&gt; shared_ptr&lt;T&gt;; </p>
<p>These deduction_guides are provided for std::shared_ptr to account for the edge cases missed by the implicit deduction guides.<br />
Note that there is no class template argument deduction from pointer types because it is impossible to distinguish pointers obtained from array and non-array forms of new. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;memory&gt; </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = std::make_shared&lt;int&gt;(42);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::weak_ptr w{p}; // explicit deduction guide is used in this case<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::shared_ptr p2{w}; // explicit deduction guide is used in this case<br />
&nbsp;<wbr>&nbsp;}</p>
