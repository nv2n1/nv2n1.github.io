---
title: "qwtweedingcurvefitter(3)"
name: "qwtweedingcurvefitter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtweedingcurvefitter/"
description: "QwtWeedingCurveFitter –"
---

<p>QwtWeedingCurveFitter &#8211; </p>
<p> A curve fitter implementing Douglas and Peucker algorithm.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_curve_fitter.h&gt; </p>
<p> Inherits <code>QwtCurveFitter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtWeedingCurveFitter</code> (double <code>tolerance</code>=1.0) </p>
<p> virtual <code>~QwtWeedingCurveFitter</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setTolerance</code> (double) </p>
<p> double <code>tolerance</code> () const </p>
<p> void <code>setChunkSize</code> (uint) </p>
<p> uint <code>chunkSize</code> () const </p>
<p> virtual QPolygonF <code>fitCurve</code> (const QPolygonF &amp;) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A curve fitter implementing Douglas and Peucker algorithm. </p>
<p> The purpose of the Douglas and Peucker algorithm is that given a &#8216;curve&#8217; composed of line segments to find a curve not too dissimilar but that has fewer points. The algorithm defines &#8216;too dissimilar&#8217; based on the maximum distance (tolerance) between the original curve and the smoothed curve. </p>
<p> The runtime of the algorithm increases non linear ( worst case O( n*n ) ) and might be very slow for huge polygons. To avoid performance issues it might be useful to split the polygon ( <code>setChunkSize()</code> ) and to run the algorithm for these smaller parts. The disadvantage of having no interpolation at the borders is for most use cases irrelevant. </p>
<p> The smoothed curve consists of a subset of the points that defined the original curve. </p>
<p> In opposite to <code>QwtSplineCurveFitter</code> the Douglas and Peucker algorithm reduces the number of points. By adjusting the tolerance parameter according to the axis scales <code>QwtSplineCurveFitter</code> can be used to implement different level of details to speed up painting of curves of many points.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtWeedingCurveFitter::QwtWeedingCurveFitter (doubletolerance = 1.0)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tolerance</i> Tolerance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTolerance()</code>, <code>tolerance()</code></dl>
<h2>Member Function Documentation</h2>
<h3>uint QwtWeedingCurveFitter::chunkSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximum for the number of points passed to a run of the algorithm &#8211; or 0, when unlimited</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setChunkSize()</code></dl>
<h3>QPolygonF QwtWeedingCurveFitter::fitCurve (const QPolygonF &amp;points) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>points</i> Series of data points</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Curve points</dl>
<p> Implements <code>QwtCurveFitter</code>.</p>
<h3>void QwtWeedingCurveFitter::setChunkSize (uintnumPoints)</h3>
<p>Limit the number of points passed to a run of the algorithm </p>
<p> The runtime of the Douglas Peucker algorithm increases non linear with the number of points. For a chunk size &gt; 0 the polygon is split into pieces passed to the algorithm one by one. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numPoints</i> Maximum for the number of points passed to the algorithm</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>chunkSize()</code></dl>
<h3>void QwtWeedingCurveFitter::setTolerance (doubletolerance)</h3>
<p>Assign the tolerance </p>
<p> The tolerance is the maximum distance, that is acceptable between the original curve and the smoothed curve. </p>
<p> Increasing the tolerance will reduce the number of the resulting points. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tolerance</i> Tolerance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>tolerance()</code></dl>
<h3>double QwtWeedingCurveFitter::tolerance () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Tolerance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTolerance()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
