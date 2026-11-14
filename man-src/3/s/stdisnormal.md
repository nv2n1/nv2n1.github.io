---
title: "stdisnormal(3)"
name: "stdisnormal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisnormal/"
description: "std::isnormal – std::isnormal"
---

<p>std::isnormal &#8211; std::isnormal</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool isnormal( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
bool isnormal( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
bool isnormal( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
bool isnormal( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the given floating point number arg is normal, i.e. is neither zero, subnormal, infinite, nor NaN.<br />
4) A set of overloads or a function template accepting the arg argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if arg is normal, false otherwise </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;isnormal(NaN) = &quot; &lt;&lt; std::isnormal(NAN) &lt;&lt; '
'
              &lt;&lt; &quot;isnormal(Inf) = &quot; &lt;&lt; std::isnormal(INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;isnormal(0.0) = &quot; &lt;&lt; std::isnormal(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;isnormal(DBL_MIN/2.0) = &quot; &lt;&lt; std::isnormal(DBL_MIN / 2.0) &lt;&lt; '
'
              &lt;&lt; &quot;isnormal(1.0) = &quot; &lt;&lt; std::isnormal(1.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;isnormal(NaN) = false<br />
&nbsp;<wbr>&nbsp;isnormal(Inf) = false<br />
&nbsp;<wbr>&nbsp;isnormal(0.0) = false<br />
&nbsp;<wbr>&nbsp;isnormal(DBL_MIN/2.0) = false<br />
&nbsp;<wbr>&nbsp;isnormal(1.0) = true</p>
<h2>See also</h2>
<p>fpclassify categorizes the given floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isfinite checks if the given number has finite value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isinf checks if the given number is infinite<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
