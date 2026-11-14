---
title: "stdnumeric_limitsround_error(3)"
name: "stdnumeric_limitsround_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsround_error/"
description: "std::numeric_limits<T>::round_error – std::numeric_limits<T>::round_error"
---

<p>std::numeric_limits&lt;T&gt;::round_error &#8211; std::numeric_limits&lt;T&gt;::round_error</p>
<h2>Synopsis</h2>
<pre><code>static T round_error() throw();             (until C++11)

static constexpr T round_error() noexcept;  (since C++11)</code></pre>
<p>Returns the largest possible rounding error in ULPs (units in the last place) as defined by ISO 10967, which can vary from 0.5 (rounding to the nearest digit) to 1.0 (rounding to zero or to infinity). It is only meaningful if std::numeric_limits&lt;T&gt;::is_integer == false. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::round_error()<br />
/* non-specialized */ T()<br />
bool false<br />
char 0<br />
signed char 0<br />
unsigned char 0<br />
wchar_t 0<br />
char8_t 0<br />
char16_t 0<br />
char32_t 0<br />
short 0<br />
unsigned short 0<br />
int 0<br />
unsigned int 0<br />
long 0<br />
unsigned long 0<br />
long long 0<br />
unsigned long long 0<br />
float 0.5F<br />
double 0.5<br />
long double 0.5L </p>
<h2>See also</h2>
<p>round_style identifies the rounding style used by the type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
