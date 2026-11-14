---
title: "stdfloat_round_style(3)"
name: "stdfloat_round_style"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfloat_round_style/"
description: "std::float_round_style – std::float_round_style"
---

<p>std::float_round_style &#8211; std::float_round_style</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;limits&gt;

enum float_round_style {

    round_indeterminate = -1,

    round_toward_zero = 0,

    round_to_nearest = 1,

    round_toward_infinity = 2,

    round_toward_neg_infinity = 3

};</code></pre>
<p>Enumeration constants of type std::float_round_style indicate the rounding style used by floating-point arithmetics whenever a result of an expression is stored in an object of a floating-point type. The values are:<br />
Enumeration constants<br />
Name Definition<br />
std::round_indeterminate Rounding style cannot be determined<br />
std::round_toward_zero Rounding toward zero<br />
std::round_to_nearest Rounding toward nearest representable value<br />
std::round_toward_infinity Rounding toward positive infinity<br />
std::round_toward_neg_infinity Rounding toward negative infinity </p>
<h2>See also</h2>
<p>round_style identifies the rounding style used by the type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
FE_DOWNWARD<br />
FE_TONEAREST floating-point rounding direction<br />
FE_TOWARDZERO (macro constant)<br />
FE_UPWARD<br />
<i>(C++11)</i> </p>
