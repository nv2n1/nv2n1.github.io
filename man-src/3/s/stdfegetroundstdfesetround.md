---
title: "stdfegetroundstdfesetround(3)"
name: "stdfegetroundstdfesetround"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfegetroundstdfesetround/"
description: "std::fegetround,std::fesetround – std::fegetround,std::fesetround"
---

<p>std::fegetround,std::fesetround &#8211; std::fegetround,std::fesetround</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cfenv&gt;<br />
int fesetround( int round ) <code>(1)</code> <i>(since C++11)</i><br />
int fegetround() <code>(2)</code> <i>(since C++11)</i><br />
Manages the floating-point rounding direction.<br />
1) Attempts to establish the floating-point rounding direction equal to the argument round, which is expected to be one of the floating_point_rounding_macros.<br />
2) Returns the value of the floating_point_rounding_macro that corresponds to the current rounding direction. </p>
<h2>Parameters</h2>
<p>round &#8211; rounding direction, one of floating_point_rounding_macros</p>
<h2>Return value</h2>
<p>1) 0 on success, non-zero otherwise.<br />
2) the floating_point_rounding_macro describing the current rounding direction or a negative value if the direction cannot be determined </p>
<h2>Notes</h2>
<p>The current rounding mode, reflecting the effects of the most recent fesetround, can also be queried with FLT_ROUNDS<br />
See floating-point_rounding_macros for the effects of rounding. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;cfenv&gt;

#include &lt;iostream&gt;
int main()

{
#pragma STDC FENV_ACCESS ON
    std::fesetround(FE_DOWNWARD);
    std::cout &lt;&lt; &quot;rounding using FE_DOWNWARD: 
&quot;
              &lt;&lt; std::fixed
              &lt;&lt; &quot; 12.0 -&gt;  &quot; &lt;&lt; std::nearbyint(12.0) &lt;&lt; '
'
              &lt;&lt; &quot; 12.1 -&gt;  &quot; &lt;&lt; std::nearbyint(12.1) &lt;&lt; '
'
              &lt;&lt; &quot;-12.1 -&gt; &quot; &lt;&lt; std::nearbyint(-12.1) &lt;&lt; '
'
              &lt;&lt; &quot; 12.5 -&gt;  &quot; &lt;&lt; std::nearbyint(12.5) &lt;&lt; '
'
              &lt;&lt; &quot; 12.9 -&gt;  &quot; &lt;&lt; std::nearbyint(12.9) &lt;&lt; '
'
              &lt;&lt; &quot;-12.9 -&gt; &quot; &lt;&lt; std::nearbyint(-12.9) &lt;&lt; '
'
              &lt;&lt; &quot; 13.0 -&gt;  &quot; &lt;&lt; std::nearbyint(13.0) &lt;&lt; '
';
    std::fesetround(FE_TONEAREST);
    std::cout &lt;&lt; &quot;rounding using FE_TONEAREST: 
&quot;
              &lt;&lt; &quot; 12.0 -&gt;  &quot; &lt;&lt; std::nearbyint(12.0) &lt;&lt; '
'
              &lt;&lt; &quot; 12.1 -&gt;  &quot; &lt;&lt; std::nearbyint(12.1) &lt;&lt; '
'
              &lt;&lt; &quot;-12.1 -&gt; &quot; &lt;&lt; std::nearbyint(-12.1) &lt;&lt; '
'
              &lt;&lt; &quot; 12.5 -&gt;  &quot; &lt;&lt; std::nearbyint(12.5) &lt;&lt; '
'
              &lt;&lt; &quot; 12.9 -&gt;  &quot; &lt;&lt; std::nearbyint(12.9) &lt;&lt; '
'
              &lt;&lt; &quot;-12.9 -&gt; &quot; &lt;&lt; std::nearbyint(-12.9) &lt;&lt; '
'
              &lt;&lt; &quot; 13.0 -&gt;  &quot; &lt;&lt; std::nearbyint(13.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;rounding using FE_DOWNWARD:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.0 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.1 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;-12.1 -&gt; -13.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.5 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.9 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;-12.9 -&gt; -13.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;13.0 -&gt; 13.000000<br />
&nbsp;<wbr>&nbsp;rounding using FE_TONEAREST:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.0 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.1 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;-12.1 -&gt; -12.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.5 -&gt; 12.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;12.9 -&gt; 13.000000<br />
&nbsp;<wbr>&nbsp;-12.9 -&gt; -13.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;13.0 -&gt; 13.000000</p>
<h2>See also</h2>
<p>nearbyint<br />
nearbyintf<br />
nearbyintl nearest integer using current rounding mode<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
rint<br />
rintf<br />
rintl<br />
lrint<br />
lrintf<br />
lrintl<br />
llrint<br />
llrintf nearest integer using current rounding mode with<br />
llrintl exception if the result differs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
