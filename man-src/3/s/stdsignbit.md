---
title: "stdsignbit(3)"
name: "stdsignbit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsignbit/"
description: "std::signbit – std::signbit"
---

<p>std::signbit &#8211; std::signbit</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool signbit( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
bool signbit( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
bool signbit( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
bool signbit( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the given floating point number arg is negative.<br />
4) A set of overloads or a function template accepting the arg argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if arg is negative, false otherwise </p>
<h2>Notes</h2>
<p>This function detects the sign bit of zeroes, infinities, and NaNs. Along with std::copysign, std::signbit is one of the only two portable ways to examine the sign of a NaN. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;signbit(+0.0) = &quot; &lt;&lt; std::signbit(+0.0) &lt;&lt; '
'
              &lt;&lt; &quot;signbit(-0.0) = &quot; &lt;&lt; std::signbit(-0.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;signbit(+0.0) = false<br />
&nbsp;<wbr>&nbsp;signbit(-0.0) = true</p>
<h2>See also</h2>
<p>abs(float)<br />
fabs<br />
fabsf<br />
fabsl absolute value of a floating point value (|x|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
copysign<br />
copysignf<br />
copysignl copies the sign of a floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
