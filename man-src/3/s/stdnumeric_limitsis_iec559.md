---
title: "stdnumeric_limitsis_iec559(3)"
name: "stdnumeric_limitsis_iec559"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_iec559/"
description: "std::numeric_limits<T>::is_iec559 – std::numeric_limits<T>::is_iec559"
---

<p>std::numeric_limits&lt;T&gt;::is_iec559 &#8211; std::numeric_limits&lt;T&gt;::is_iec559</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_iec559;
(until C++ 11)

    static constexpr bool is_iec559;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_iec559 is true for all floating-point types T which fulfill the requirements of IEC 559 (IEEE_754) standard. If std::numeric_limits&lt;T&gt;::is_iec559 is true, then std::numeric_limits&lt;T&gt;::has_infinity, std::numeric_limits&lt;T&gt;::has_quiet_NaN, and std::numeric_limits&lt;T&gt;::has_signaling_NaN are also true. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_iec559<br />
/* non-specialized */ false<br />
bool false<br />
char false<br />
signed char false<br />
unsigned char false<br />
wchar_t false<br />
char8_t false<br />
char16_t false<br />
char32_t false<br />
short false<br />
unsigned short false<br />
int false<br />
unsigned int false<br />
long false<br />
unsigned long false<br />
long long false<br />
unsigned long long false<br />
float usually true<br />
double usually true<br />
long double usually true</p>
<h2>See also</h2>
<p>has_infinity identifies floating-point types that can represent the special value &quot;positive infinity&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_quiet_NaN identifies floating-point types that can represent the special value &quot;quiet not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_signaling_NaN identifies floating-point types that can represent the special value &quot;signaling not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
