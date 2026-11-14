---
title: "stdisinf(3)"
name: "stdisinf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisinf/"
description: "std::isinf – std::isinf"
---

<p>std::isinf &#8211; std::isinf</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool isinf( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
bool isinf( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
bool isinf( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
bool isinf( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the given floating point number arg is a positive or negative infinity.<br />
4) A set of overloads or a function template accepting the arg argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if arg is infinite, false otherwise </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;isinf(NaN) = &quot; &lt;&lt; std::isinf(NAN) &lt;&lt; '
'
              &lt;&lt; &quot;isinf(Inf) = &quot; &lt;&lt; std::isinf(INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;isinf(0.0) = &quot; &lt;&lt; std::isinf(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;isinf(exp(800)) = &quot; &lt;&lt; std::isinf(std::exp(800)) &lt;&lt; '
'
              &lt;&lt; &quot;isinf(DBL_MIN/2.0) = &quot; &lt;&lt; std::isinf(DBL_MIN / 2.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;isinf(NaN) = false<br />
&nbsp;<wbr>&nbsp;isinf(Inf) = true<br />
&nbsp;<wbr>&nbsp;isinf(0.0) = false<br />
&nbsp;<wbr>&nbsp;isinf(exp(800)) = true<br />
&nbsp;<wbr>&nbsp;isinf(DBL_MIN/2.0) = false</p>
<h2>See also</h2>
<p>fpclassify categorizes the given floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isfinite checks if the given number has finite value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnormal checks if the given number is normal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
