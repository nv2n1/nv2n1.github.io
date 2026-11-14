---
title: "qwtsplinecurvefitter(3)"
name: "qwtsplinecurvefitter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsplinecurvefitter/"
description: "QwtSplineCurveFitter –"
---

<p>QwtSplineCurveFitter &#8211; </p>
<p> A curve fitter using cubic splines.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_curve_fitter.h&gt; </p>
<p> Inherits <code>QwtCurveFitter</code>.</p>
<h3>Public Types</h3>
<p>enum <code>FitMode</code> { <code>Auto</code>, <code>Spline</code>, <code>ParametricSpline</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtSplineCurveFitter</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtSplineCurveFitter</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setFitMode</code> (<code>FitMode</code>) </p>
<p> <code>FitMode</code> <code>fitMode</code> () const </p>
<p> void <code>setSpline</code> (const <code>QwtSpline</code> &amp;) </p>
<p> const <code>QwtSpline</code> &amp; <code>spline</code> () const </p>
<p> <code>QwtSpline</code> &amp; <code>spline</code> () </p>
<p> void <code>setSplineSize</code> (int size) </p>
<p> int <code>splineSize</code> () const </p>
<p> virtual QPolygonF <code>fitCurve</code> (const QPolygonF &amp;) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A curve fitter using cubic splines.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtSplineCurveFitter::FitMode</code></h3>
<p>Spline type The default setting is Auto </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFitMode()</code>, <code>FitMode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Auto </i></p>
<dd>Use the default spline algorithm for polygons with increasing x values ( p[i-1] &lt; p[i] ), otherwise use a parametric spline algorithm.</p>
<dt><i>Spline </i></p>
<dd>Use a default spline algorithm.</p>
<dt><i>ParametricSpline </i></p>
<dd>Use a parametric spline algorithm.</dl>
<h2>Member Function Documentation</h2>
<h3>QPolygonF QwtSplineCurveFitter::fitCurve (const QPolygonF &amp;points) const [virtual]</h3>
<p>Find a curve which has the best fit to a series of data points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>points</i> Series of data points</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Curve points</dl>
<p> Implements <code>QwtCurveFitter</code>.</p>
<h3><code>QwtSplineCurveFitter::FitMode</code> QwtSplineCurveFitter::fitMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode representing a spline algorithm</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFitMode()</code></dl>
<h3>void QwtSplineCurveFitter::setFitMode (<code>FitMode</code>mode)</h3>
<p>Select the algorithm used for building the spline </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Mode representing a spline algorithm</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>fitMode()</code></dl>
<h3>void QwtSplineCurveFitter::setSpline (const <code>QwtSpline</code> &amp;spline)</h3>
<p>Assign a spline </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spline</i> Spline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spline()</code></dl>
<h3>void QwtSplineCurveFitter::setSplineSize (intsplineSize)</h3>
<p>Assign a spline size ( has to be at least 10 points ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>splineSize</i> Spline size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>splineSize()</code></dl>
<h3>const <code>QwtSpline</code> &amp; QwtSplineCurveFitter::spline () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpline()</code></dl>
<h3><code>QwtSpline</code> &amp; QwtSplineCurveFitter::spline ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpline()</code></dl>
<h3>int QwtSplineCurveFitter::splineSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spline size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSplineSize()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
