---
title: "stdlerp(3)"
name: "stdlerp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlerp/"
description: "std::lerp – std::lerp"
---

<p>std::lerp &#8211; std::lerp</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
constexpr float lerp( float a, float b, float t ); <code>(1)</code> <i>(since C++20)</i><br />
constexpr double lerp( double a, double b, double t ); <code>(2)</code> <i>(since C++20)</i><br />
constexpr long double lerp( long double a, long double b, long double t ); <code>(3)</code> <i>(since C++20)</i><br />
constexpr Promoted lerp( Arithmetic1 a, Arithmetic2 b, Arithmetic3 t ); <code>(4)</code> <i>(since C++20)</i><br />
1-3) Computes a+t*(b−a), i.e. the linear interpolation between a and b for the parameter t (or extrapolation, when t is outside the range [0,1]).<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by 1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double. </p>
<h2>Parameters</h2>
<p>a, b, t &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>a+t*(b−a)<br />
When isfinite(a) &amp;&amp; isfinite(b), the following properties are guaranteed:<br />
* If t == 0, the result is equal to a.<br />
* If t == 1, the result is equal to b.<br />
* If t &gt;= 0 &amp;&amp; t &lt;= 1, the result is finite.<br />
* If isfinite(t) &amp;&amp; a == b, the result is equal to a.<br />
* If isfinite(t) || (!isnan(t) &amp;&amp; b-a != 0), the result is not NaN.<br />
Let CMP(x,y) be 1 if x &gt; y, -1 if x &lt; y, and 0 otherwise. For any t1 and t2, the product of CMP(lerp(a, b, t2), lerp(a, b, t1)), CMP(t2, t1), and CMP(b, a) is non-negative. (That is, lerp is monotonic.) </p>
<h2>Examples</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
