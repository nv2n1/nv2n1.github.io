---
title: "qwtlogscaleengine(3)"
name: "qwtlogscaleengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlogscaleengine/"
description: "QwtLogScaleEngine –"
---

<p>QwtLogScaleEngine &#8211; </p>
<p> A scale engine for logarithmic scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_engine.h&gt; </p>
<p> Inherits <code>QwtScaleEngine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtLogScaleEngine</code> (uint <code>base</code>=10) </p>
<p> virtual <code>~QwtLogScaleEngine</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>autoScale</code> (int maxSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const </p>
<p> virtual <code>QwtScaleDiv</code> <code>divideScale</code> (double x1, double x2, int numMajorSteps, int numMinorSteps, double stepSize=0.0) const<br />
 <i>Calculate a scale division for an interval. </i></p>
<h3>Protected Member Functions</h3>
<p><code>QwtInterval</code> <code>align</code> (const <code>QwtInterval</code> &amp;, double stepSize) const<br />
 <i>Align an interval to a step size. </i><br />
 void <code>buildTicks</code> (const <code>QwtInterval</code> &amp;, double stepSize, int maxMinSteps, QList&lt; double &gt; ticks[<code>QwtScaleDiv::NTickTypes</code>]) const<br />
 <i>Calculate ticks for an interval. </i><br />
 QList&lt; double &gt; <code>buildMajorTicks</code> (const <code>QwtInterval</code> &amp;interval, double stepSize) const<br />
 <i>Calculate major ticks for an interval. </i><br />
 void <code>buildMinorTicks</code> (const QList&lt; double &gt; &amp;majorTicks, int maxMinorSteps, double stepSize, QList&lt; double &gt; &amp;minorTicks, QList&lt; double &gt; &amp;mediumTicks) const<br />
 <i>Calculate minor/medium ticks for major ticks. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A scale engine for logarithmic scales. </p>
<p> The step size is measured in <i>decades</i> and the major step size will be adjusted to fit the pattern $</p>
<hr>
<p>re n is a natural number including zero.</p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>the step size as well as the margins are measured in <i>decades</i>.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLogScaleEngine::QwtLogScaleEngine (uintbase = 10)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>base</i> Base of the scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBase()</code></dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtInterval</code> QwtLogScaleEngine::align (const <code>QwtInterval</code> &amp;interval, doublestepSize) const [protected]</h3>
<p>Align an interval to a step size. The limits of an interval are aligned that both are integer multiples of the step size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval<br />
 <i>stepSize</i> Step size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Aligned interval</dl>
<h3>void QwtLogScaleEngine::autoScale (intmaxNumSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const [virtual]</h3>
<p>Align and divide an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxNumSteps</i> Max. number of steps<br />
 <i>x1</i> First limit of the interval (In/Out)<br />
 <i>x2</i> Second limit of the interval (In/Out)<br />
 <i>stepSize</i> Step size (Out)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleEngine::setAttribute()</code></dl>
<p> Implements <code>QwtScaleEngine</code>.</p>
<h3>QList&lt; double &gt; QwtLogScaleEngine::buildMajorTicks (const <code>QwtInterval</code> &amp;interval, doublestepSize) const [protected]</h3>
<p>Calculate major ticks for an interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval<br />
 <i>stepSize</i> Step size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated ticks</dl>
<h3>void QwtLogScaleEngine::buildMinorTicks (const QList&lt; double &gt; &amp;majorTicks, intmaxMinorSteps, doublestepSize, QList&lt; double &gt; &amp;minorTicks, QList&lt; double &gt; &amp;mediumTicks) const [protected]</h3>
<p>Calculate minor/medium ticks for major ticks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>majorTicks</i> Major ticks<br />
 <i>maxMinorSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size<br />
 <i>minorTicks</i> Array to be filled with the calculated minor ticks<br />
 <i>mediumTicks</i> Array to be filled with the calculated medium ticks</dl>
<h3>void QwtLogScaleEngine::buildTicks (const <code>QwtInterval</code> &amp;interval, doublestepSize, intmaxMinorSteps, QList&lt; double &gt;ticks[QwtScaleDiv::NTickTypes]) const [protected]</h3>
<p>Calculate ticks for an interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval<br />
 <i>maxMinorSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size<br />
 <i>ticks</i> Arrays to be filled with the calculated ticks</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>buildMajorTicks()</code>, <code>buildMinorTicks</code></dl>
<h3><code>QwtScaleDiv</code> QwtLogScaleEngine::divideScale (doublex1, doublex2, intmaxMajorSteps, intmaxMinorSteps, doublestepSize = 0.0) const [virtual]</h3>
<p>Calculate a scale division for an interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x1</i> First interval limit<br />
 <i>x2</i> Second interval limit<br />
 <i>maxMajorSteps</i> Maximum for the number of major steps<br />
 <i>maxMinorSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size. If stepSize == 0, the engine calculates one.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated scale division</dl>
<p> Implements <code>QwtScaleEngine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
