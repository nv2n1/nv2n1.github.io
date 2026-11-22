---
title: "qwtspline(3)"
name: "qwtspline"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtspline/"
description: "QwtSpline –"
---

<p>QwtSpline &#8211; </p>
<p> A class for spline interpolation.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_spline.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>SplineType</code> { <code>Natural</code>, <code>Periodic</code> }<br/>
 <i>Spline type. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtSpline</code> ()<br/>
 <i>Constructor. </i><br/>
 <code>QwtSpline</code> (const <code>QwtSpline</code> &amp;) </p>
<p> <code>~QwtSpline</code> ()<br/>
 <i>Destructor. </i><br/>
 <code>QwtSpline</code> &amp; <code>operator=</code> (const <code>QwtSpline</code> &amp;) </p>
<p> void <code>setSplineType</code> (<code>SplineType</code>) </p>
<p> <code>SplineType</code> <code>splineType</code> () const </p>
<p> bool <code>setPoints</code> (const QPolygonF &amp;<code>points</code>)<br/>
 <i>Calculate the spline coefficients. </i><br/>
 QPolygonF <code>points</code> () const </p>
<p> void <code>reset</code> ()<br/>
 <i>Free allocated memory and set size to 0. </i><br/>
 bool <code>isValid</code> () const<br/>
 <i>True if valid. </i><br/>
 double <code>value</code> (double x) const </p>
<p> const QVector&lt; double &gt; &amp; <code>coefficientsA</code> () const </p>
<p> const QVector&lt; double &gt; &amp; <code>coefficientsB</code> () const </p>
<p> const QVector&lt; double &gt; &amp; <code>coefficientsC</code> () const </p>
<h3>Protected Member Functions</h3>
<p>bool <code>buildNaturalSpline</code> (const QPolygonF &amp;)<br/>
 <i>Determines the coefficients for a natural spline. </i><br/>
 bool <code>buildPeriodicSpline</code> (const QPolygonF &amp;)<br/>
 <i>Determines the coefficients for a periodic spline. </i></p>
<h2>Detailed Description</h2>
<p>A class for spline interpolation. </p>
<p> The <code>QwtSpline</code> class is used for cubical spline interpolation. Two types of splines, natural and periodic, are supported. </p>
<p> <code>Usage:</code></p>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>1.</dt>
<dd>First call <code>setPoints()</code> to determine the spline coefficients for a tabulated function y(x).</dd>
<dt>2.</dt>
<dd>After the coefficients have been set up, the interpolated function value for an argument x can be determined by calling <code>QwtSpline::value()</code>.</dd></dl>
</dl>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>#include &lt;qwt_spline.h&gt;
QPolygonF interpolate(const QPolygonF&amp; points, int numValues)
{
 QwtSpline spline;
 if ( !spline.setPoints(points) )
 return points;
 QPolygonF interpolatedPoints(numValues);
 const double delta =
 (points[numPoints - 1].x() - points[0].x()) / (points.size() - 1);
 for(i = 0; i &lt; points.size(); i++) / interpolate
 {
 const double x = points[0].x() + i * delta;
 interpolatedPoints[i].setX(x);
 interpolatedPoints[i].setY(spline.value(x));
 }
 return interpolatedPoints;
}</pre>
<p>&nbsp;<wbr></dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtSpline::SplineType</code></h3>
<p>Spline type. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Natural </i></dt>
<dd>A natural spline.</dd>
<dt><i>Periodic </i></dt>
<dd>A periodic spline.</dd></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSpline::QwtSpline (const <code>QwtSpline</code> &amp;other)</h3>
<p>Copy constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Spline used for initialization</dd></dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtSpline::buildNaturalSpline (const QPolygonF &amp;points) [protected]</h3>
<p>Determines the coefficients for a natural spline. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if successful</dd></dl>
<h3>bool QwtSpline::buildPeriodicSpline (const QPolygonF &amp;points) [protected]</h3>
<p>Determines the coefficients for a periodic spline. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if successful</dd></dl>
<h3>const QVector&lt; double &gt; &amp; QwtSpline::coefficientsA () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A coefficients</dd></dl>
<h3>const QVector&lt; double &gt; &amp; QwtSpline::coefficientsB () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>B coefficients</dd></dl>
<h3>const QVector&lt; double &gt; &amp; QwtSpline::coefficientsC () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>C coefficients</dd></dl>
<h3><code>QwtSpline</code> &amp; QwtSpline::operator= (const <code>QwtSpline</code> &amp;other)</h3>
<p>Assignment operator </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Spline used for initialization</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>*this</dd></dl>
<h3>QPolygonF QwtSpline::points () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Points, that have been by <code>setPoints()</code></dd></dl>
<h3>bool QwtSpline::setPoints (const QPolygonF &amp;points)</h3>
<p>Calculate the spline coefficients. Depending on the value of <i>periodic</i>, this function will determine the coefficients for a natural or a periodic spline and store them internally. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>points</i> Points</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if successful</dd></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The sequence of x (but not y) values has to be strictly monotone increasing, which means points[i].x() &lt; points[i+1].x(). If this is not the case, the function will return false</dd></dl>
<h3>void QwtSpline::setSplineType (<code>SplineType</code>splineType)</h3>
<p>Select the algorithm used for calculating the spline </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>splineType</i> Spline type</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>splineType()</code></dd></dl>
<h3><code>QwtSpline::SplineType</code> QwtSpline::splineType () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the spline type</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSplineType()</code></dd></dl>
<h3>double QwtSpline::value (doublex) const</h3>
<p>Calculate the interpolated function value corresponding to a given argument x. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Coordinate</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interpolated coordinate</dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
