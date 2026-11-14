---
title: "stdnumeric_limitshas_quiet_nan(3)"
name: "stdnumeric_limitshas_quiet_nan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitshas_quiet_nan/"
description: "std::numeric_limits<T>::has_quiet_NaN – std::numeric_limits<T>::has_quiet_NaN"
---

<p>std::numeric_limits&lt;T&gt;::has_quiet_NaN &#8211; std::numeric_limits&lt;T&gt;::has_quiet_NaN</p>
<h2>Synopsis</h2>
<pre><code>static const bool has_quiet_NaN;
(until C++ 11)

    static constexpr bool has_quiet_NaN;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::has_quiet_NaN is true for all types T capable of representing the special value &quot;Quiet Not-A-Number&quot;. This constant is meaningful for all floating-point types and is guaranteed to be true if std::numeric_limits&lt;T&gt;::is_iec559 == true. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::has_quiet_NaN<br />
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
<p>quiet_NaN returns a quiet NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
has_infinity identifies floating-point types that can represent the special value &quot;positive infinity&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_signaling_NaN identifies floating-point types that can represent the special value &quot;signaling not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
