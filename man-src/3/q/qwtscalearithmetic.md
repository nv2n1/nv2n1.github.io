---
title: "qwtscalearithmetic(3)"
name: "qwtscalearithmetic"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscalearithmetic/"
description: "QwtScaleArithmetic –"
---

<p>QwtScaleArithmetic &#8211; </p>
<p> Arithmetic including a tolerance.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_engine.h&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static double <code>ceilEps</code> (double value, double intervalSize) </p>
<p> static double <code>floorEps</code> (double value, double intervalSize) </p>
<p> static double <code>divideEps</code> (double interval, double steps)<br />
 <i>Divide an interval into steps. </i><br />
 static double <code>divideInterval</code> (double interval, int numSteps, uint base) </p>
<h2>Detailed Description</h2>
<p>Arithmetic including a tolerance.</p>
<h2>Member Function Documentation</h2>
<h3>double QwtScaleArithmetic::ceilEps (doublevalue, doubleintervalSize) [static]</h3>
<p>Ceil a value, relative to an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be ceiled<br />
 <i>intervalSize</i> Interval size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rounded value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>floorEps()</code></dl>
<h3>double QwtScaleArithmetic::divideEps (doubleintervalSize, doublenumSteps) [static]</h3>
<p>Divide an interval into steps. $stepSize = (intervalSize &#8211; intervalSize * 10e^{-6}) / numSteps$ </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervalSize</i> Interval size<br />
 <i>numSteps</i> Number of steps</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Step size</dl>
<h3>double QwtScaleArithmetic::divideInterval (doubleintervalSize, intnumSteps, uintbase) [static]</h3>
<p>Calculate a step size for a given interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervalSize</i> Interval size<br />
 <i>numSteps</i> Number of steps<br />
 <i>base</i> Base for the division ( usually 10 )</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated step size</dl>
<h3>double QwtScaleArithmetic::floorEps (doublevalue, doubleintervalSize) [static]</h3>
<p>Floor a value, relative to an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be floored<br />
 <i>intervalSize</i> Interval size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rounded value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>floorEps()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
