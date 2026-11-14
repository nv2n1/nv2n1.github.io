---
title: "stdnumeric_limitshas_denorm(3)"
name: "stdnumeric_limitshas_denorm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitshas_denorm/"
description: "std::numeric_limits<T>::has_denorm – std::numeric_limits<T>::has_denorm"
---

<p>std::numeric_limits&lt;T&gt;::has_denorm &#8211; std::numeric_limits&lt;T&gt;::has_denorm</p>
<h2>Synopsis</h2>
<pre><code>static const std::float_denorm_style has_denorm;
(until C++ 11)

    static constexpr std::float_denorm_style has_denorm;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::has_denorm identifies the floating-point types that support subnormal_values. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::has_denorm<br />
/* non-specialized */ std::denorm_absent<br />
bool std::denorm_absent<br />
char std::denorm_absent<br />
signed char std::denorm_absent<br />
unsigned char std::denorm_absent<br />
wchar_t std::denorm_absent<br />
char8_t std::denorm_absent<br />
char16_t std::denorm_absent<br />
char32_t std::denorm_absent<br />
short std::denorm_absent<br />
unsigned short std::denorm_absent<br />
int std::denorm_absent<br />
unsigned int std::denorm_absent<br />
long std::denorm_absent<br />
unsigned long std::denorm_absent<br />
long long std::denorm_absent<br />
unsigned long long std::denorm_absent<br />
float usually std::denorm_present<br />
double usually std::denorm_present<br />
long double usually std::denorm_present</p>
<h2>See also</h2>
<p>denorm_min returns the smallest positive subnormal value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates floating-point denormalization modes<br />
float_denorm_style <i>(enum)</i> </p>
