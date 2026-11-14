---
title: "std__numeric_limits_base(3)"
name: "std__numeric_limits_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__numeric_limits_base/"
description: "std::__numeric_limits_base –"
---

<p>std::__numeric_limits_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::numeric_limits&lt; _Tp &gt;</code>.</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr int digits



static constexpr int digits10



static constexpr float_denorm_style has_denorm



static constexpr bool has_denorm_loss



static constexpr bool has_infinity



static constexpr bool has_quiet_NaN



static constexpr bool has_signaling_NaN



static constexpr bool is_bounded



static constexpr bool is_exact



static constexpr bool is_iec559



static constexpr bool is_integer



static constexpr bool is_modulo



static constexpr bool is_signed



static constexpr bool is_specialized



static constexpr int max_digits10



static constexpr int max_exponent



static constexpr int max_exponent10



static constexpr int min_exponent



static constexpr int min_exponent10



static constexpr int radix



static constexpr float_round_style round_style



static constexpr bool tinyness_before



static constexpr bool traps</code></pre>
<h2>Detailed Description</h2>
<p>Part of std::numeric_limits. </p>
<p> The static const members are usable as integral constant expressions. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This is a separate class for purposes of efficiency; you should only access these members as part of an instantiation of the std::numeric_limits class.</dl>
<p> Definition at line 191 of file limits.</p>
<h2>Member Data Documentation</h2>
<h3>constexpr int std::__numeric_limits_base::digits [static]</h3>
<p>The number of radix digits that be represented without change: for integer types, the number of non-sign bits in the mantissa; for floating types, the number of radix digits in the mantissa. </p>
<p> Definition at line 200 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::digits10 [static]</h3>
<p>The number of base 10 digits that can be represented without change. </p>
<p> Definition at line 203 of file limits.</p>
<h3>constexpr <code>float_denorm_style</code> std::__numeric_limits_base::has_denorm [static]</h3>
<p>See std::float_denorm_style for more information. </p>
<p> Definition at line 255 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::has_denorm_loss [static]</h3>
<p>True if loss of accuracy is detected as a denormalization loss, rather than as an inexact result. </p>
<p> Definition at line 259 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::has_infinity [static]</h3>
<p>True if the type has a representation for positive infinity. </p>
<p> Definition at line 244 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::has_quiet_NaN [static]</h3>
<p>True if the type has a representation for a quiet (non-signaling) Not a Number. </p>
<p> Definition at line 248 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::has_signaling_NaN [static]</h3>
<p>True if the type has a representation for a signaling Not a Number. </p>
<p> Definition at line 252 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_bounded [static]</h3>
<p>True if the set of values representable by the type is finite. All built-in types are bounded, this member would be false for arbitrary precision types. </p>
<p> Definition at line 268 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_exact [static]</h3>
<p>True if the type uses an exact representation. All integer types are exact, but not all exact types are integer. For example, rational and fixed-exponent representations are exact but not integer. </p>
<p> Definition at line 220 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_iec559 [static]</h3>
<p>True if-and-only-if the type adheres to the IEC 559 standard, also known as IEEE 754. (Only makes sense for floating point types.) </p>
<p> Definition at line 263 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_integer [static]</h3>
<p>True if the type is integer. </p>
<p> Definition at line 215 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_modulo [static]</h3>
<p>True if the type is <i>modulo</i>. A type is modulo if, for any operation involving +, -, or * on values of that type whose result would fall outside the range [min(),max()], the value returned differs from the true value by an integer multiple of max() &#8211; min() + 1. On most machines, this is false for floating types, true for unsigned integers, and true for signed integers. See PR22200 about signed integers. </p>
<p> Definition at line 277 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_signed [static]</h3>
<p>True if the type is signed. </p>
<p> Definition at line 212 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::is_specialized [static]</h3>
<p>This will be true for all fundamental types (which have specializations), and false for everything else. </p>
<p> Definition at line 195 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::max_digits10 [static]</h3>
<p>The number of base 10 digits required to ensure that values which differ are always differentiated. </p>
<p> Definition at line 208 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::max_exponent [static]</h3>
<p>The maximum positive integer such that radix raised to the power of (one less than that integer) is a representable finite floating point number. </p>
<p> Definition at line 237 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::max_exponent10 [static]</h3>
<p>The maximum positive integer such that 10 raised to that power is in the range of representable finite floating point numbers. </p>
<p> Definition at line 241 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::min_exponent [static]</h3>
<p>The minimum negative integer such that radix raised to the power of (one less than that integer) is a normalized floating point number. </p>
<p> Definition at line 228 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::min_exponent10 [static]</h3>
<p>The minimum negative integer such that 10 raised to that power is in the range of normalized floating point numbers. </p>
<p> Definition at line 232 of file limits.</p>
<h3>constexpr int std::__numeric_limits_base::radix [static]</h3>
<p>For integer types, specifies the base of the representation. For floating types, specifies the base of the exponent representation. </p>
<p> Definition at line 224 of file limits.</p>
<h3>constexpr <code>float_round_style</code> std::__numeric_limits_base::round_style [static]</h3>
<p>See std::float_round_style for more information. This is only meaningful for floating types; integer types will all be round_toward_zero. </p>
<p> Definition at line 288 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::tinyness_before [static]</h3>
<p>True if tininess is detected before rounding. (see IEC 559) </p>
<p> Definition at line 283 of file limits.</p>
<h3>constexpr bool std::__numeric_limits_base::traps [static]</h3>
<p>True if trapping is implemented for this type. </p>
<p> Definition at line 280 of file limits.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
