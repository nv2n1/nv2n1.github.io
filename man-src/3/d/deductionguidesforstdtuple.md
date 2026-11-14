---
title: "deductionguidesforstdtuple(3)"
name: "deductionguidesforstdtuple"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdtuple/"
description: "deductionguidesforstd::tuple – deductionguidesforstd::tuple"
---

<p>deductionguidesforstd::tuple &#8211; deductionguidesforstd::tuple</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;tuple&gt;<br />
template&lt;class&#8230; UTypes&gt; <code>(1)</code> <i>(since C++17)</i><br />
tuple(UTypes&#8230;) -&gt; tuple&lt;UTypes&#8230;&gt;;<br />
template&lt;class T1, class T2&gt; <code>(2)</code> <i>(since C++17)</i><br />
tuple(std::pair&lt;T1, T2&gt;) -&gt; tuple&lt;T1, T2&gt;;<br />
template&lt;class Alloc, class&#8230; UTypes&gt; <code>(3)</code> <i>(since C++17)</i><br />
tuple(std::allocator_arg_t, Alloc, UTypes&#8230;) -&gt; tuple&lt;UTypes&#8230;&gt;;<br />
template&lt;class Alloc, class T1, class T2&gt; <code>(4)</code> <i>(since C++17)</i><br />
tuple(std::allocator_arg_t, Alloc, std::pair&lt;T1, T2&gt;) -&gt; tuple&lt;T1, T2&gt;;<br />
template&lt;class Alloc, class&#8230; UTypes&gt; <code>(5)</code> <i>(since C++17)</i><br />
tuple(std::allocator_arg_t, Alloc, tuple&lt;UTypes&#8230;&gt;) -&gt; tuple&lt;UTypes&#8230;&gt;; </p>
<p>These deduction_guides are provided for std::tuple to account for the edge cases missed by the implicit deduction guides, in particular, non-copyable arguments and array to pointer conversion. </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;tuple&gt;<br />
&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a[2], b[3], c[4];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::tuple t1{a, b, c}; // explicit deduction guide is used in this case<br />
&nbsp;<wbr>&nbsp;}</p>
