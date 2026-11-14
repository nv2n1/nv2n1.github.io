---
title: "qwtsyntheticpointdata(3)"
name: "qwtsyntheticpointdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsyntheticpointdata/"
description: "QwtSyntheticPointData –"
---

<p>QwtSyntheticPointData &#8211; </p>
<p> Synthetic point data.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_data.h&gt; </p>
<p> Inherits <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtSyntheticPointData</code> (size_t <code>size</code>, const <code>QwtInterval</code> &amp;=<code>QwtInterval</code>()) </p>
<p> void <code>setSize</code> (size_t <code>size</code>) </p>
<p> virtual size_t <code>size</code> () const </p>
<p> void <code>setInterval</code> (const <code>QwtInterval</code> &amp;) </p>
<p> <code>QwtInterval</code> <code>interval</code> () const </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Calculate the bounding rectangle. </i><br />
 virtual QPointF <code>sample</code> (size_t i) const </p>
<p> virtual double <code>y</code> (double <code>x</code>) const =0 </p>
<p> virtual double <code>x</code> (uint index) const </p>
<p> virtual void <code>setRectOfInterest</code> (const QRectF &amp;) </p>
<p> QRectF <code>rectOfInterest</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>Synthetic point data. </p>
<p> <code>QwtSyntheticPointData</code> provides a fixed number of points for an interval. The points are calculated in equidistant steps in x-direction. </p>
<p> If the interval is invalid, the points are calculated for the &#8216;rectangle of interest&#8217;, what normally is the displayed area on the plot canvas. In this mode you get different levels of detail, when zooming in/out. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd></dl>
<p> The following example shows how to implement a sinus curve. </p>
<pre>#include &lt;cmath&gt;
#include &lt;qwt_series_data.h&gt;
#include &lt;qwt_plot_curve.h&gt;
#include &lt;qwt_plot.h&gt;
#include &lt;qapplication.h&gt;
class SinusData: public QwtSyntheticPointData
{
public:
 SinusData():
 QwtSyntheticPointData( 100 )
 {
 }
 virtual double y( double x ) const
 {
 return qSin( x );
 }
};
int main(int argc, char **argv)
{
 QApplication a( argc, argv );
 QwtPlot plot;
 plot.setAxisScale( QwtPlot::xBottom, 0.0, 10.0 );
 plot.setAxisScale( QwtPlot::yLeft, -1.0, 1.0 );
 QwtPlotCurve *curve = new QwtPlotCurve( &quot;y = sin(x)&quot; );
 curve-&gt;setData( new SinusData() );
 curve-&gt;attach( &amp;plot );
 plot.show();
 return a.exec();
}</pre>
<p>&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSyntheticPointData::QwtSyntheticPointData (size_tsize, const <code>QwtInterval</code> &amp;interval = <code>QwtInterval</code>())</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Number of points<br />
 <i>interval</i> Bounding interval for the points</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code>, <code>setSize()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtSyntheticPointData::boundingRect () const [virtual]</h3>
<p>Calculate the bounding rectangle. This implementation iterates over all points, what could often be implemented much faster using the characteristics of the series. When there are many points it is recommended to overload and reimplement this method using the characteristics of the series ( if possible ). </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3><code>QwtInterval</code> QwtSyntheticPointData::interval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code>, <code>size()</code></dl>
<h3>QRectF QwtSyntheticPointData::rectOfInterest () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRectOfInterest()</code></dl>
<h3>QPointF QwtSyntheticPointData::sample (size_tindex) const [virtual]</h3>
<p>Calculate the point from an index </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>QPointF(x(index), y(x(index)));</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>For invalid indices ( index &lt; 0 || index &gt;= <code>size()</code> ) (0, 0) is returned.</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>void QwtSyntheticPointData::setInterval (const <code>QwtInterval</code> &amp;interval)</h3>
<p>Set the bounding interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code>, <code>setSize()</code></dl>
<h3>void QwtSyntheticPointData::setRectOfInterest (const QRectF &amp;rect) [virtual]</h3>
<p>Set a the &#8216;rectangle of interest&#8217; </p>
<p> <code>QwtPlotSeriesItem</code> defines the current area of the plot canvas as &#8216;rect of interest&#8217; ( <code>QwtPlotSeriesItem::updateScaleDiv()</code> ). </p>
<p> If <code>interval()</code>.isValid() == false the x values are calculated in the interval rect.left() -&gt; rect.right(). </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rectOfInterest()</code></dl>
<p> Reimplemented from <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>void QwtSyntheticPointData::setSize (size_tsize)</h3>
<p>Change the number of points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Number of points</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>size()</code>, <code>setInterval()</code></dl>
<h3>size_t QwtSyntheticPointData::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of points</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSize()</code>, <code>interval()</code></dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>double QwtSyntheticPointData::x (uintindex) const [virtual]</h3>
<p>Calculate a x-value from an index </p>
<p> x values are calculated by dividing an interval into equidistant steps. If !interval().isValid() the interval is calculated from the &#8216;rectangle of interest&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the requested point</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated x coordinate</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code>, <code>rectOfInterest()</code>, <code>y()</code></dl>
<h3>virtual double QwtSyntheticPointData::y (doublex) const [pure virtual]</h3>
<p>Calculate a y value for a x value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> x value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Corresponding y value</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
