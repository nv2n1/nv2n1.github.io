---
title: "stdnumeric_limitstraps(3)"
name: "stdnumeric_limitstraps"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitstraps/"
description: "std::numeric_limits<T>::traps – std::numeric_limits<T>::traps"
---

<p>std::numeric_limits&lt;T&gt;::traps &#8211; std::numeric_limits&lt;T&gt;::traps</p>
<h2>Synopsis</h2>
<pre><code>static const bool traps;
(until C++ 11)

    static constexpr bool traps;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::traps is true for all arithmetic types T that have at least one value that, if used as an argument to an arithmetic operation, will generate a trap. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::traps<br />
/* non-specialized */ false<br />
bool false<br />
char usually true<br />
signed char usually true<br />
unsigned char usually true<br />
wchar_t usually true<br />
char8_t usually true<br />
char16_t usually true<br />
char32_t usually true<br />
short usually true<br />
unsigned short usually true<br />
int usually true<br />
unsigned int usually true<br />
long usually true<br />
unsigned long usually true<br />
long long usually true<br />
unsigned long long usually true<br />
float usually false<br />
double usually false<br />
long double usually false</p>
<h2>Notes</h2>
<p>On most platforms integer division by zero always traps, and std::numeric_limits&lt;T&gt;::traps is true for all integer types that support the value 0. The exception is the type bool: even though division by false traps due to integral promotion from bool to int, it is the zero-valued int that traps. Zero is not a value of type bool.<br />
On most platforms, floating-point exceptions may be turned on and off at run time (e.g. feenableexcept() on Linux or _controlfp on Windows), in which case the value of std::numeric_limits&lt;T&gt;::traps for floating-point types reflects the state of floating-point trapping facility at the time of program startup, which is false on most modern systems. An exception would be a DEC Alpha program, where it is true if compiled without -ieee. </p>
<h2>See also</h2>
<p>Floating-point_environment<br />
tinyness_before identifies floating-point types that detect tinyness before rounding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_denorm_loss identifies the floating-point types that detect loss of precision as denormalization loss rather than inexact result<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
