---
title: "qwtcurvefitter(3)"
name: "qwtcurvefitter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcurvefitter/"
description: "QwtCurveFitter –"
---

<p>QwtCurveFitter &#8211; </p>
<p> Abstract base class for a curve fitter.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_curve_fitter.h&gt; </p>
<p> Inherited by <code>QwtSplineCurveFitter</code>, and <code>QwtWeedingCurveFitter</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~QwtCurveFitter</code> ()<br />
 <i>Destructor. </i><br />
 virtual QPolygonF <code>fitCurve</code> (const QPolygonF &amp;polygon) const =0 </p>
<h3>Protected Member Functions</h3>
<p><code>QwtCurveFitter</code> ()<br />
 <i>Constructor. </i></p>
<h2>Detailed Description</h2>
<p>Abstract base class for a curve fitter.</p>
<h2>Member Function Documentation</h2>
<h3>virtual QPolygonF QwtCurveFitter::fitCurve (const QPolygonF &amp;polygon) const [pure virtual]</h3>
<p>Find a curve which has the best fit to a series of data points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>polygon</i> Series of data points</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Curve points</dl>
<p> Implemented in <code>QwtWeedingCurveFitter</code>, and <code>QwtSplineCurveFitter</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
