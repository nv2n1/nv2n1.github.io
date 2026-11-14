---
title: "qwtlog10scaleengine(3)"
name: "qwtlog10scaleengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlog10scaleengine/"
description: "QwtLog10ScaleEngine – A scale engine for logarithmic (base 10) scales."
---

<p>QwtLog10ScaleEngine &#8211; A scale engine for logarithmic (base 10) scales. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_scale_engine.h">qwt_scale_engine.h</a>&gt; </p>
<p> Inherits <code>QwtScaleEngine</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>autoScale</code> (int maxSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const </p>
<p> virtual <code>QwtScaleDiv</code> <code>divideScale</code> (double x1, double x2, int numMajorSteps, int numMinorSteps, double stepSize=0.0) const </p>
<p> virtual <code>QwtScaleTransformation</code> * <code>transformation</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>QwtDoubleInterval</code> <code>log10</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> <code>pow10</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p>A scale engine for logarithmic (base 10) scales. </p>
<p> The step size is measured in *decades* and the major step size will be adjusted to fit the pattern $</p>
<hr>
<p>re n is a natural number including zero.</p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>the step size as well as the margins are measured in *decades*.</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtLog10ScaleEngine::autoScale (int maxNumSteps, double &amp; x1, double &amp; x2, double &amp; stepSize) const [virtual]</h3>
<p>Align and divide an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxNumSteps</i> Max. number of steps<br />
 <i>x1</i> First limit of the interval (In/Out)<br />
 <i>x2</i> Second limit of the interval (In/Out)<br />
 <i>stepSize</i> Step size (Out)</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleEngine::setAttribute()</code></dl>
<p> Implements <code>QwtScaleEngine</code>.</p>
<h3><code>QwtScaleDiv</code> QwtLog10ScaleEngine::divideScale (double x1, double x2, int maxMajSteps, int maxMinSteps, double stepSize = 0.0) const [virtual]</h3>
<p>Calculate a scale division. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x1</i> First interval limit<br />
 <i>x2</i> Second interval limit<br />
 <i>maxMajSteps</i> Maximum for the number of major steps<br />
 <i>maxMinSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size. If stepSize == 0, the scaleEngine calculates one.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>QwtScaleEngine::stepSize(), QwtLog10ScaleEngine::subDivide()</dl>
<p> Implements <code>QwtScaleEngine</code>.</p>
<h3><code>QwtDoubleInterval</code> QwtLog10ScaleEngine::log10 (const <code>QwtDoubleInterval</code> &amp; interval) const [protected]</h3>
<p>Return the interval [log10(interval.minValue(), log10(interval.maxValue]</p>
<h3><code>QwtDoubleInterval</code> QwtLog10ScaleEngine::pow10 (const <code>QwtDoubleInterval</code> &amp; interval) const [protected]</h3>
<p>Return the interval [pow10(interval.minValue(), pow10(interval.maxValue]</p>
<h3><code>QwtScaleTransformation</code> * QwtLog10ScaleEngine::transformation () const [virtual]</h3>
<p>Return a transformation, for logarithmic (base 10) scales </p>
<p> Implements <code>QwtScaleEngine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
