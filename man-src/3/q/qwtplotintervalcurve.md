---
title: "qwtplotintervalcurve(3)"
name: "qwtplotintervalcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotintervalcurve/"
description: "QwtPlotIntervalCurve –"
---

<p>QwtPlotIntervalCurve &#8211; </p>
<p> <code>QwtPlotIntervalCurve</code> represents a series of samples, where each value is associated with an interval ( $[y1,y2] = f(x)$ ).</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_intervalcurve.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>, and <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>CurveStyle</code> { <code>NoCurve</code>, <code>Tube</code>, <code>UserCurve</code> = 100 }<br />
 <i>Curve styles. The default setting is </i><code>QwtPlotIntervalCurve::Tube</code>.<br />
 enum <code>PaintAttribute</code> { <code>ClipPolygons</code> = 0x01, <code>ClipSymbol</code> = 0x02 } </p>
<p> typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotIntervalCurve</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotIntervalCurve</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotIntervalCurve</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setSamples</code> (const QVector&lt; <code>QwtIntervalSample</code> &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; <code>QwtIntervalSample</code> &gt; *) </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;)<br />
 <i>Assign a pen. </i><br />
 const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;) </p>
<p> const QBrush &amp; <code>brush</code> () const </p>
<p> void <code>setStyle</code> (<code>CurveStyle</code> <code>style</code>) </p>
<p> <code>CurveStyle</code> <code>style</code> () const </p>
<p> void <code>setSymbol</code> (const <code>QwtIntervalSymbol</code> *) </p>
<p> const <code>QwtIntervalSymbol</code> * <code>symbol</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>init</code> ()<br />
 <i>Initialize internal members. </i><br />
 virtual void <code>drawTube</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>drawSymbols</code> (QPainter *, const <code>QwtIntervalSymbol</code> &amp;, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotIntervalCurve</code> represents a series of samples, where each value is associated with an interval ( $[y1,y2] = f(x)$ ). </p>
<p> The representation depends on the <code>style()</code> and an optional <code>symbol()</code> that is displayed for each interval. <code>QwtPlotIntervalCurve</code> might be used to display error bars or the area between 2 curves.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotIntervalCurve::CurveStyle</code></h3>
<p>Curve styles. The default setting is <code>QwtPlotIntervalCurve::Tube</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoCurve </i></p>
<dd>Don&#8217;t draw a curve. Note: This doesn&#8217;t affect the symbols.</p>
<dt><i>Tube </i></p>
<dd>Build 2 curves from the upper and lower limits of the intervals and draw them with the <code>pen()</code>. The area between the curves is filled with the <code>brush()</code>.</p>
<dt><i>UserCurve </i></p>
<dd>Styles &gt;= <code>QwtPlotIntervalCurve::UserCurve</code> are reserved for derived classes that overload <code>drawSeries()</code> with additional application specific curve types.</dl>
<h3>enum <code>QwtPlotIntervalCurve::PaintAttribute</code></h3>
<p>Attributes to modify the drawing algorithm. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ClipPolygons </i></p>
<dd>Clip polygons before painting them. In situations, where points are far outside the visible area (f.e when zooming deep) this might be a substantial improvement for the painting performance.</p>
<dt><i>ClipSymbol </i></p>
<dd>Check if a symbol is on the plot canvas before painting it.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotIntervalCurve::QwtPlotIntervalCurve (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotIntervalCurve::QwtPlotIntervalCurve (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPlotIntervalCurve::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of all samples. For an empty series the rectangle is invalid.</dl>
<p> Reimplemented from <code>QwtPlotSeriesItem</code>.</p>
<h3>const QBrush &amp; QwtPlotIntervalCurve::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used to fill the area in Tube <code>style()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code>, <code>setStyle()</code>, <code>CurveStyle</code></dl>
<h3>void QwtPlotIntervalCurve::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw a subset of the samples </p>
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
<dd><code>drawTube()</code>, <code>drawSymbols()</code></dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotIntervalCurve::drawSymbols (QPainter *painter, const <code>QwtIntervalSymbol</code> &amp;symbol, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw symbols for a subset of the samples </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>symbol</i> Interval symbol<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code>, <code>drawSeries()</code>, <code>drawTube()</code></dl>
<h3>void QwtPlotIntervalCurve::drawTube (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw a tube </p>
<p> Builds 2 curves from the upper and lower limits of the intervals and draws them with the <code>pen()</code>. The area between the curves is filled with the <code>brush()</code>. </p>
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
<dd><code>drawSeries()</code>, <code>drawSymbols()</code></dl>
<h3><code>QwtGraphic</code> QwtPlotIntervalCurve::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon for the legend</dl>
<p> In case of Tube <code>style()</code> the icon is a plain rectangle filled with the <code>brush()</code>. If a symbol is assigned it is scaled to size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( ignored as there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setLegendIconSize()</code>, <code>QwtPlotItem::legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const QPen &amp; QwtPlotIntervalCurve::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen used to draw the lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>int QwtPlotIntervalCurve::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotIntervalCurve</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotIntervalCurve::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. </p>
<p> The brush is used to fill the area in Tube <code>style()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brush()</code>, <code>pen()</code>, <code>setStyle()</code>, <code>CurveStyle</code></dl>
<h3>void QwtPlotIntervalCurve::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dl>
<h3>void QwtPlotIntervalCurve::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotIntervalCurve::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> New pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotIntervalCurve::setSamples (const QVector&lt; <code>QwtIntervalSample</code> &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of samples</dl>
<h3>void QwtPlotIntervalCurve::setSamples (<code>QwtSeriesData</code>&lt; <code>QwtIntervalSample</code> &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotIntervalCurve::setStyle (<code>CurveStyle</code>style)</h3>
<p>Set the curve&#8217;s drawing style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Curve style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CurveStyle</code>, <code>style()</code></dl>
<h3>void QwtPlotIntervalCurve::setSymbol (const <code>QwtIntervalSymbol</code> *symbol)</h3>
<p>Assign a symbol. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> Symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code></dl>
<h3><code>QwtPlotIntervalCurve::CurveStyle</code> QwtPlotIntervalCurve::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Style of the curve</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h3>const <code>QwtIntervalSymbol</code> * QwtPlotIntervalCurve::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol or NULL, when no symbol has been assigned</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code></dl>
<h3>bool QwtPlotIntervalCurve::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PaintAttribute</code>, <code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
