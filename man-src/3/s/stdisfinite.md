---
title: "stdisfinite(3)"
name: "stdisfinite"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisfinite/"
description: "std::isfinite – std::isfinite"
---

<p>std::isfinite &#8211; std::isfinite</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool isfinite( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
bool isfinite( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
bool isfinite( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
bool isfinite( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the given floating point number arg has finite value i.e. it is normal, subnormal or zero, but not infinite or NaN.<br />
4) A set of overloads or a function template accepting the arg argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if arg has finite value, false otherwise </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;isfinite(NaN) = &quot; &lt;&lt; std::isfinite(NAN) &lt;&lt; '
'
              &lt;&lt; &quot;isfinite(Inf) = &quot; &lt;&lt; std::isfinite(INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;isfinite(0.0) = &quot; &lt;&lt; std::isfinite(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;isfinite(exp(800)) = &quot; &lt;&lt; std::isfinite(std::exp(800)) &lt;&lt; '
'
              &lt;&lt; &quot;isfinite(DBL_MIN/2.0) = &quot; &lt;&lt; std::isfinite(DBL_MIN / 2.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;isfinite(NaN) = false<br />
&nbsp;<wbr>&nbsp;isfinite(Inf) = false<br />
&nbsp;<wbr>&nbsp;isfinite(0.0) = true<br />
&nbsp;<wbr>&nbsp;isfinite(exp(800)) = false<br />
&nbsp;<wbr>&nbsp;isfinite(DBL_MIN/2.0) = true</p>
<h2>See also</h2>
<p>fpclassify categorizes the given floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isinf checks if the given number is infinite<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnormal checks if the given number is normal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
