---
title: "qwtplotspectrocurve(3)"
name: "qwtplotspectrocurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotspectrocurve/"
description: "QwtPlotSpectroCurve –"
---

<p>QwtPlotSpectroCurve &#8211; </p>
<p> Curve that displays 3D points as dots, where the z coordinate is mapped to a color.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_spectrocurve.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>, and <code>QwtSeriesStore&lt; QwtPoint3D &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>PaintAttribute</code> { <code>ClipPoints</code> = 1 }<br />
 <i>Paint attributes. </i><br />
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotSpectroCurve</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotSpectroCurve</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotSpectroCurve</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setSamples</code> (const QVector&lt; <code>QwtPoint3D</code> &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; <code>QwtPoint3D</code> &gt; *) </p>
<p> void <code>setColorMap</code> (<code>QwtColorMap</code> *) </p>
<p> const <code>QwtColorMap</code> * <code>colorMap</code> () const </p>
<p> void <code>setColorRange</code> (const <code>QwtInterval</code> &amp;) </p>
<p> <code>QwtInterval</code> &amp; <code>colorRange</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> void <code>setPenWidth</code> (double width) </p>
<p> double <code>penWidth</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawDots</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<h2>Detailed Description</h2>
<p>Curve that displays 3D points as dots, where the z coordinate is mapped to a color.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotSpectroCurve::PaintAttribute</code></h3>
<p>Paint attributes. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ClipPoints </i></p>
<dd>Clip points outside the canvas rectangle.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotSpectroCurve::QwtPlotSpectroCurve (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotSpectroCurve::QwtPlotSpectroCurve (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3>const <code>QwtColorMap</code> * QwtPlotSpectroCurve::colorMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Color Map used for mapping the intensity values to colors</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorMap()</code>, <code>setColorRange()</code>, <code>QwtColorMap::color()</code></dl>
<h3><code>QwtInterval</code> &amp; QwtPlotSpectroCurve::colorRange () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value interval, that corresponds to the color map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorRange()</code>, <code>setColorMap()</code>, <code>QwtColorMap::color()</code></dl>
<h3>void QwtPlotSpectroCurve::drawDots (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw a subset of the points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted. If to &lt; 0 the series will be painted to its last sample.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code></dl>
<h3>void QwtPlotSpectroCurve::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw a subset of the points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted. If to &lt; 0 the series will be painted to its last sample.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawDots()</code></dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>double QwtPlotSpectroCurve::penWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen width used to draw a dot</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPenWidth()</code></dl>
<h3>int QwtPlotSpectroCurve::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotSpectroCurve</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotSpectroCurve::setColorMap (<code>QwtColorMap</code> *colorMap)</h3>
<p>Change the color map </p>
<p> Often it is useful to display the mapping between intensities and colors as an additional plot axis, showing a color bar. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>colorMap</i> Color Map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>colorMap()</code>, <code>setColorRange()</code>, <code>QwtColorMap::color()</code>, <code>QwtScaleWidget::setColorBarEnabled()</code>, <code>QwtScaleWidget::setColorMap()</code></dl>
<h3>void QwtPlotSpectroCurve::setColorRange (const <code>QwtInterval</code> &amp;interval)</h3>
<p>Set the value interval, that corresponds to the color map </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> interval.minValue() corresponds to 0.0, interval.maxValue() to 1.0 on the color map.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>colorRange()</code>, <code>setColorMap()</code>, <code>QwtColorMap::color()</code></dl>
<h3>void QwtPlotSpectroCurve::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off /sa PaintAttribute, <code>testPaintAttribute()</code></dl>
<h3>void QwtPlotSpectroCurve::setPenWidth (doublepenWidth)</h3>
<p>Assign a pen width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>penWidth</i> New pen width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>penWidth()</code></dl>
<h3>void QwtPlotSpectroCurve::setSamples (const QVector&lt; <code>QwtPoint3D</code> &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<h3>void QwtPlotSpectroCurve::setSamples (<code>QwtSeriesData</code>&lt; <code>QwtPoint3D</code> &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>bool QwtPlotSpectroCurve::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PaintAttribute</code>, <code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
