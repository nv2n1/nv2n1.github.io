---
title: "stdnumeric_limitshas_denorm_loss(3)"
name: "stdnumeric_limitshas_denorm_loss"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitshas_denorm_loss/"
description: "std::numeric_limits<T>::has_denorm_loss – std::numeric_limits<T>::has_denorm_loss"
---

<p>std::numeric_limits&lt;T&gt;::has_denorm_loss &#8211; std::numeric_limits&lt;T&gt;::has_denorm_loss</p>
<h2>Synopsis</h2>
<pre><code>static const bool has_denorm_loss;
(until C++ 11)

    static constexpr bool has_denorm_loss;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::has_denorm_loss is true for all floating-point types T that detect loss of precision when creating a subnormal number as denormalization loss rather than as inexact result (see below). </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::has_denorm_loss<br />
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
float implementation-defined<br />
double implementation-defined<br />
long double implementation-defined</p>
<h2>Notes</h2>
<p>Standard-compliant IEEE 754 floating-point implementations of subnormal numbers are required to detect the loss of accuracy associated with the creation of such number, if it occurs, and may do so in one of the two distinct ways:<br />
1) Denormalization loss: the delivered result differs from what would have been computed were exponent range unbounded.<br />
2) Inexact result: the delivered result differs from what would have been computed were both exponent range and precision unbounded.<br />
No implementation of denormalization loss mechanism exists (accuracy loss is detected after rounding, as inexact result), and this option was removed in the 2008 revision of IEEE Std 754.<br />
libstdc++, libc++, libCstd, and stlport4 define this constant as false for all floating-point types. Microsoft Visual Studio defines it as true for all floating-point types.<br />
As with any floating-point computations, accuracy loss may raise FE_INEXACT </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>tinyness_before identifies floating-point types that detect tinyness before rounding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_denorm identifies the denormalization style used by the floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
