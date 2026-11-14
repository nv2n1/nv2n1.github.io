---
title: "stdnumeric_limits(3)"
name: "stdnumeric_limits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limits/"
description: "std::numeric_limits – std::numeric_limits"
---

<p>std::numeric_limits &#8211; std::numeric_limits</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;limits&gt;

template&lt; class T &gt; class numeric_limits;</code></pre>
<p>The numeric_limits class template provides a standardized way to query various properties of arithmetic types (e.g. the largest possible value for type int is std::numeric_limits&lt;int&gt;::max()).<br />
This information is provided via specializations of the numeric_limits template. The standard library makes available specializations for all arithmetic types: Defined in header&lt;limits&gt;</p>
<p>    template &lt;&gt;<br />
    class numeric_limits&lt;bool&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;char&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;signed char&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;unsigned char&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;wchar_t&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;char8_t&gt;; // C++20 feature</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;char16_t&gt;; // C++11 feature</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;char32_t&gt;; // C++11 feature</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;short&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;unsigned short&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;int&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;unsigned int&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;long&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;unsigned long&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;long long&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;unsigned long long&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;float&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;double&gt;;</p>
<p>template &lt;&gt;<br />
class numeric_limits&lt;long double&gt;;<br />
Additionally, a specialization exists for every cv-qualified version of each arithmetic type, identical to the unqualified specialization, e.g. std::numeric_limits&lt;const int&gt;, std::numeric_limits&lt;volatile int&gt;, and std::numeric_limits&lt;const volatile int&gt; are provided and are equivalent to std::numeric_limits&lt;int&gt;.<br />
The standard library types that are aliases of arithmetic types (such as std::size_t or std::streamsize) may also be examined with the std::numeric_limits type traits.<br />
Non-arithmetic standard types, such as std::complex&lt;T&gt; or std::nullptr_t, do not have specializations.<br />
Implementations may provide specializations of std::numeric_limits for implementation-specific types: e.g. GCC provides std::numeric_limits&lt;__int128&gt;. Non-standard libraries may add_specializations for library-provided types, e.g. OpenEXR provides std::numeric_limits&lt;half&gt; for a 16-bit floating-point type. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to retrieve numeric properties for</p>
<h2>Member constants</h2>
<p>is_specialized identifies types for which std::numeric_limits is specialized<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_signed identifies signed types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_integer identifies integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>has_infinity identifies floating-point types that can represent the special value &quot;positive infinity&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>has_quiet_NaN identifies floating-point types that can represent the special value &quot;quiet not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>has_signaling_NaN identifies floating-point types that can represent the special value &quot;signaling not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>has_denorm identifies the denormalization style used by the floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>has_denorm_loss identifies the floating-point types that detect loss of precision as denormalization loss rather than inexact result<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>round_style identifies the rounding style used by the type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_iec559 identifies the IEC 559/IEEE 754 floating-point types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_bounded identifies types that represent a finite set of values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>is_modulo identifies types that handle overflows with modulo arithmetic<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>digits number of radix digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>digits10 number of decimal digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>max_digits10 number of decimal digits necessary to differentiate all values of this type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> <i>(C++11)</i> </p>
<p>radix the radix or integer base used by the representation of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>min_exponent10 the smallest negative power of ten that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>max_exponent10 the largest integer power of 10 that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>traps identifies types which can cause arithmetic operations to trap<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>tinyness_before identifies floating-point types that detect tinyness before rounding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>min returns the smallest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>lowest returns the lowest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> <i>(C++11)</i> </p>
<p>max returns the largest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>epsilon returns the difference between 1.0 and the next representable value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>round_error returns the maximum rounding error of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>infinity returns the positive infinity value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>quiet_NaN returns a quiet NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>signaling_NaN returns a signaling NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>denorm_min returns the smallest positive subnormal value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Helper classes</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates floating-point rounding modes<br />
float_round_style <i>(enum)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates floating-point denormalization modes<br />
float_denorm_style <i>(enum)</i></p>
<h2>Relationship with C library macro constants</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Members<br />
Specialization min() lowest() max() epsilon() digits digits10 min_exponent min_exponent10 max_exponent max_exponent10 radix<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(C++11)</i><br />
numeric_limits&lt;bool&gt; 2<br />
numeric_limits&lt;char&gt; CHAR_MIN CHAR_MIN CHAR_MAX 2<br />
numeric_limits&lt;signed char&gt; SCHAR_MIN SCHAR_MIN SCHAR_MAX 2<br />
numeric_limits&lt;unsigned char&gt; 0 0 UCHAR_MAX 2<br />
numeric_limits&lt;wchar_t&gt; WCHAR_MIN WCHAR_MIN WCHAR_MAX 2<br />
numeric_limits&lt;char8_t&gt; 0 0 UCHAR_MAX 2<br />
numeric_limits&lt;char16_t&gt; 0 0 UINT_LEAST16_MAX 2<br />
numeric_limits&lt;char32_t&gt; 0 0 UINT_LEAST32_MAX 2<br />
numeric_limits&lt;short&gt; SHRT_MIN SHRT_MIN SHRT_MAX 2<br />
numeric_limits&lt;signed short&gt;<br />
numeric_limits&lt;unsigned short&gt; 0 0 USHRT_MAX 2<br />
numeric_limits&lt;int&gt; INT_MIN INT_MIN INT_MAX 2<br />
numeric_limits&lt;signed int&gt;<br />
numeric_limits&lt;unsigned int&gt; 0 0 UINT_MAX 2<br />
numeric_limits&lt;long&gt; LONG_MIN LONG_MIN LONG_MAX 2<br />
numeric_limits&lt;signed long&gt;<br />
numeric_limits&lt;unsigned long&gt; 0 0 ULONG_MAX 2<br />
numeric_limits&lt;long long&gt; LLONG_MIN LLONG_MIN LLONG_MAX 2<br />
numeric_limits&lt;signed long long&gt;<br />
numeric_limits&lt;unsigned long long&gt; 0 0 ULLONG_MAX 2<br />
numeric_limits&lt;float&gt; FLT_MIN -FLT_MAX FLT_MAX FLT_EPSILON FLT_MANT_DIG FLT_DIG FLT_MIN_EXP FLT_MIN_10_EXP FLT_MAX_EXP FLT_MAX_10_EXP FLT_RADIX<br />
numeric_limits&lt;double&gt; DBL_MIN -DBL_MAX DBL_MAX DBL_EPSILON DBL_MANT_DIG DBL_DIG DBL_MIN_EXP DBL_MIN_10_EXP DBL_MAX_EXP DBL_MAX_10_EXP FLT_RADIX<br />
numeric_limits&lt;long double&gt; LDBL_MIN -LDBL_MAX LDBL_MAX LDBL_EPSILON LDBL_MANT_DIG LDBL_DIG LDBL_MIN_EXP LDBL_MIN_10_EXP LDBL_MAX_EXP LDBL_MAX_10_EXP FLT_RADIX</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;limits&gt;

#include &lt;iostream&gt;
int main()

{
    std::cout &lt;&lt; &quot;type	lowest()	min()		max()

&quot;;
    std::cout &lt;&lt; &quot;uchar	&quot;
              &lt;&lt; +std::numeric_limits&lt;unsigned char&gt;::lowest() &lt;&lt; '	' &lt;&lt; '	'
              &lt;&lt; +std::numeric_limits&lt;unsigned char&gt;::min() &lt;&lt; '	' &lt;&lt; '	'
              &lt;&lt; +std::numeric_limits&lt;unsigned char&gt;::max() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int	&quot;
              &lt;&lt; std::numeric_limits&lt;int&gt;::lowest() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;int&gt;::min() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;int&gt;::max() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float	&quot;
              &lt;&lt; std::numeric_limits&lt;float&gt;::lowest() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;float&gt;::max() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;double	&quot;
              &lt;&lt; std::numeric_limits&lt;double&gt;::lowest() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;double&gt;::min() &lt;&lt; '	'
              &lt;&lt; std::numeric_limits&lt;double&gt;::max() &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;type<tt> </tt>lowest()<tt> </tt>min()<tt> </tt><tt> </tt>max()</p>
<p>&nbsp;<wbr>&nbsp;uchar<tt> </tt>0<tt> </tt><tt> </tt>0<tt> </tt><tt> </tt>255</p>
<p>&nbsp;<wbr>&nbsp;int<tt> </tt>-2147483648<tt> </tt>-2147483648<tt> </tt>2147483647</p>
<p>&nbsp;<wbr>&nbsp;float<tt> </tt>-3.40282e+38<tt> </tt>1.17549e-38<tt> </tt>3.40282e+38</p>
<p>&nbsp;<wbr>&nbsp;double<tt> </tt>-1.79769e+308<tt> </tt>2.22507e-308<tt> </tt>1.79769e+308</p>
<h2>See also</h2>
<p>* Fixed_width_integer_types<br />
* Arithmetic_types<br />
* C++_type_system_overview<br />
* Type_support_(basic_types,_RTTI,_type_traits) </p>
