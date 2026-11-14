---
title: "stdis_eqstdis_neqstdis_ltstdis_gtstdis_lteqstdis_gteq(3)"
name: "stdis_eqstdis_neqstdis_ltstdis_gtstdis_lteqstdis_gteq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_eqstdis_neqstdis_ltstdis_gtstdis_lteqstdis_gteq/"
description: "std::is_eq,std::is_neq,std::is_lt,std::is_gt,std::is_lteq,std::is_gteq – std::is_eq,std::is_neq,std::is_lt,std::is_gt,std::is_lteq,std::is_gteq"
---

<p>std::is_eq,std::is_neq,std::is_lt,std::is_gt,std::is_lteq,std::is_gteq &#8211; std::is_eq,std::is_neq,std::is_lt,std::is_gt,std::is_lteq,std::is_gteq</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
constexpr bool is_eq(std::weak_equality cmp) noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr bool is_neq(std::weak_equality cmp) noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr bool is_lt(std::partial_ordering cmp) noexcept; <code>(3)</code> <i>(since C++20)</i><br />
constexpr bool is_lteq(std::partial_ordering cmp) noexcept; <code>(4)</code> <i>(since C++20)</i><br />
constexpr bool is_gt(std::partial_ordering cmp) noexcept; <code>(5)</code> <i>(since C++20)</i><br />
constexpr bool is_gteq(std::partial_ordering cmp) noexcept <code>(6)</code> <i>(since C++20)</i><br />
These functions take a result of 3-way comparison and convert it to the result of one of the six relational operators<br />
Specifically, these functions return<br />
1) cmp == 0<br />
2) cmp != 0<br />
3) cmp &lt; 0<br />
4) cmp &lt;= 0<br />
5) cmp &gt; 0<br />
6) cmp &gt;= 0 </p>
<h2>Parameters</h2>
<p>cmp &#8211; result of 3-way comparison</p>
<h2>Return value</h2>
<p>bool result of the corresponding relational operation </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>partial_ordering the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20) </p>
