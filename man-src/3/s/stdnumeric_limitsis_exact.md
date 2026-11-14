---
title: "stdnumeric_limitsis_exact(3)"
name: "stdnumeric_limitsis_exact"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_exact/"
description: "std::numeric_limits<T>::is_exact – std::numeric_limits<T>::is_exact"
---

<p>std::numeric_limits&lt;T&gt;::is_exact &#8211; std::numeric_limits&lt;T&gt;::is_exact</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_exact;
(until C++ 11)

    static constexpr bool is_exact;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_exact is true for all arithmetic types T that use exact representation. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_exact<br />
/* non-specialized */ false<br />
bool true<br />
char true<br />
signed char true<br />
unsigned char true<br />
wchar_t true<br />
char8_t true<br />
char16_t true<br />
char32_t true<br />
short true<br />
unsigned short true<br />
int true<br />
unsigned int true<br />
long true<br />
unsigned long true<br />
long long true<br />
unsigned long long true<br />
float false<br />
double false<br />
long double false</p>
<h2>Notes</h2>
<p>While all fundamental types T for which std::numeric_limits&lt;T&gt;::is_exact==true are integer types, a library may define exact types that aren&#8217;t integers, e.g. a rational arithmetics type representing fractions. </p>
<h2>See also</h2>
<p>is_integer identifies integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_signed identifies signed types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_bounded identifies types that represent a finite set of values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
