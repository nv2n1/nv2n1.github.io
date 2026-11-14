---
title: "stdfpclassify(3)"
name: "stdfpclassify"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfpclassify/"
description: "std::fpclassify – std::fpclassify"
---

<p>std::fpclassify &#8211; std::fpclassify</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
int fpclassify( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
int fpclassify( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
int fpclassify( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
int fpclassify( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Categorizes floating point value arg into the following categories: zero, subnormal, normal, infinite, NAN, or implementation-defined category.<br />
4) A set of overloads or a function template accepting the from argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>one of FP_INFINITE, FP_NAN, FP_NORMAL, FP_SUBNORMAL, FP_ZERO or implementation-defined type, specifying the category of arg. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;
const char *show_classification(double x)
{
    switch (std::fpclassify(x)) {
    case FP_INFINITE:
        return &quot;Inf&quot;;
    case FP_NAN:
        return &quot;NaN&quot;;
    case FP_NORMAL:
        return &quot;normal&quot;;
    case FP_SUBNORMAL:
        return &quot;subnormal&quot;;
    case FP_ZERO:
        return &quot;zero&quot;;
    default:
        return &quot;unknown&quot;;
    }
}

int main()

{
    std::cout &lt;&lt; &quot;1.0/0.0 is &quot; &lt;&lt; show_classification(1 / 0.0) &lt;&lt; '
'
              &lt;&lt; &quot;0.0/0.0 is &quot; &lt;&lt; show_classification(0.0 / 0.0) &lt;&lt; '
'
              &lt;&lt; &quot;DBL_MIN/2 is &quot; &lt;&lt; show_classification(DBL_MIN / 2) &lt;&lt; '
'
              &lt;&lt; &quot;-0.0 is &quot; &lt;&lt; show_classification(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;1.0 is &quot; &lt;&lt; show_classification(1.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;1.0/0.0 is Inf<br />
&nbsp;<wbr>&nbsp;0.0/0.0 is NaN<br />
&nbsp;<wbr>&nbsp;DBL_MIN/2 is subnormal<br />
&nbsp;<wbr>&nbsp;-0.0 is zero<br />
&nbsp;<wbr>&nbsp;1.0 is normal</p>
<h2>See also</h2>
<p>isfinite checks if the given number has finite value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isinf checks if the given number is infinite<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnormal checks if the given number is normal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides an interface to query properties of all fundamental numeric types.<br />
numeric_limits <i>(class template)</i> </p>
