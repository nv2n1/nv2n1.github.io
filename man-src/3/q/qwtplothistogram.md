---
title: "qwtplothistogram(3)"
name: "qwtplothistogram"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplothistogram/"
description: "QwtPlotHistogram –"
---

<p>QwtPlotHistogram &#8211; </p>
<p> <code>QwtPlotHistogram</code> represents a series of samples, where an interval is associated with a value ( $y = f([x1,x2])$ ).</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_histogram.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>, and <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>HistogramStyle</code> { <code>Outline</code>, <code>Columns</code>, <code>Lines</code>, <code>UserStyle</code> = 100 } </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotHistogram</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotHistogram</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotHistogram</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;) </p>
<p> const QBrush &amp; <code>brush</code> () const </p>
<p> void <code>setSamples</code> (const QVector&lt; <code>QwtIntervalSample</code> &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; <code>QwtIntervalSample</code> &gt; *) </p>
<p> void <code>setBaseline</code> (double reference)<br />
 <i>Set the value of the baseline. </i><br />
 double <code>baseline</code> () const </p>
<p> void <code>setStyle</code> (<code>HistogramStyle</code> <code>style</code>) </p>
<p> <code>HistogramStyle</code> <code>style</code> () const </p>
<p> void <code>setSymbol</code> (const <code>QwtColumnSymbol</code> *)<br />
 <i>Assign a symbol. </i><br />
 const <code>QwtColumnSymbol</code> * <code>symbol</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>QwtColumnRect</code> <code>columnRect</code> (const <code>QwtIntervalSample</code> &amp;, const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;) const </p>
<p> virtual void <code>drawColumn</code> (QPainter *, const <code>QwtColumnRect</code> &amp;, const <code>QwtIntervalSample</code> &amp;) const </p>
<p> void <code>drawColumns</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, int from, int to) const </p>
<p> void <code>drawOutline</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, int from, int to) const </p>
<p> void <code>drawLines</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, int from, int to) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotHistogram</code> represents a series of samples, where an interval is associated with a value ( $y = f([x1,x2])$ ). </p>
<p> The representation depends on the <code>style()</code> and an optional <code>symbol()</code> that is displayed for each interval. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The term &#8216;histogram&#8217; is used in a different way in the areas of digital image processing and statistics. Wikipedia introduces the terms &#8216;image histogram&#8217; and &#8216;color histogram&#8217; to avoid confusions. While &#8216;image histograms&#8217; can be displayed by a <code>QwtPlotCurve</code> there is no applicable plot item for a &#8216;color histogram&#8217; yet.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotBarChart</code>, <code>QwtPlotMultiBarChart</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotHistogram::HistogramStyle</code></h3>
<p>Histogram styles. The default style is <code>QwtPlotHistogram::Columns</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code>, <code>setSymbol()</code>, <code>symbol()</code>, <code>setBaseline()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Outline </i></p>
<dd>Draw an outline around the area, that is build by all intervals using the <code>pen()</code> and fill it with the <code>brush()</code>. The outline style requires, that the intervals are in increasing order and not overlapping.</p>
<dt><i>Columns </i></p>
<dd>Draw a column for each interval. When a <code>symbol()</code> has been set the symbol is used otherwise the column is displayed as plain rectangle using <code>pen()</code> and <code>brush()</code>.</p>
<dt><i>Lines </i></p>
<dd>Draw a simple line using the <code>pen()</code> for each interval.</p>
<dt><i>UserStyle </i></p>
<dd>Styles &gt;= UserStyle are reserved for derived classes that overload <code>drawSeries()</code> with additional application specific ways to display a histogram.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotHistogram::QwtPlotHistogram (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the histogram.</dl>
<h3>QwtPlotHistogram::QwtPlotHistogram (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the histogram.</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtPlotHistogram::baseline () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value of the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBaseline()</code></dl>
<h3>QRectF QwtPlotHistogram::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of all samples. For an empty series the rectangle is invalid.</dl>
<p> Reimplemented from <code>QwtPlotSeriesItem</code>.</p>
<h3>const QBrush &amp; QwtPlotHistogram::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used in a <code>style()</code> depending way.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3><code>QwtColumnRect</code> QwtPlotHistogram::columnRect (const <code>QwtIntervalSample</code> &amp;sample, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap) const [protected], [virtual]</h3>
<p>Calculate the area that is covered by a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> Sample<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle, that is covered by a sample</dl>
<h3>void QwtPlotHistogram::drawColumn (QPainter *painter, const <code>QwtColumnRect</code> &amp;rect, const <code>QwtIntervalSample</code> &amp;sample) const [protected], [virtual]</h3>
<p>Draw a column for a sample in Columns <code>style()</code>. </p>
<p> When a <code>symbol()</code> has been set the symbol is used otherwise the column is displayed as plain rectangle using <code>pen()</code> and <code>brush()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Rectangle where to paint the column in paint device coordinates<br />
 <i>sample</i> Sample to be displayed</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>In applications, where different intervals need to be displayed in a different way ( f.e different colors or even using different symbols) it is recommended to overload <code>drawColumn()</code>.</dl>
<h3>void QwtPlotHistogram::drawColumns (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, intfrom, intto) const [protected]</h3>
<p>Draw a histogram in Columns <code>style()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted. If to &lt; 0 the histogram will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code>, <code>setSymbol()</code>, <code>drawColumn()</code></dl>
<h3>void QwtPlotHistogram::drawLines (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, intfrom, intto) const [protected]</h3>
<p>Draw a histogram in Lines <code>style()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted. If to &lt; 0 the histogram will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code>, <code>setPen()</code></dl>
<h3>void QwtPlotHistogram::drawOutline (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, intfrom, intto) const [protected]</h3>
<p>Draw a histogram in Outline <code>style()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>from</i> Index of the first sample to be painted<br />
 <i>to</i> Index of the last sample to be painted. If to &lt; 0 the histogram will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The outline style requires, that the intervals are in increasing order and not overlapping.</dl>
<h3>void QwtPlotHistogram::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw a subset of the histogram samples </p>
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
<dd><code>drawOutline()</code>, <code>drawLines()</code>, <code>drawColumns</code></dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotHistogram::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p>A plain rectangle without pen using the <code>brush()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( ignored as there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A graphic displaying the icon</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setLegendIconSize()</code>, <code>QwtPlotItem::legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const QPen &amp; QwtPlotHistogram::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen used in a <code>style()</code> depending way.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>int QwtPlotHistogram::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotHistogram</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotHistogram::setBaseline (doublevalue)</h3>
<p>Set the value of the baseline. Each column representing an <code>QwtIntervalSample</code> is defined by its interval and the interval between baseline and the value of the sample. </p>
<p> The default value of the baseline is 0.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value of the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>baseline()</code></dl>
<h3>void QwtPlotHistogram::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush, that is used in a <code>style()</code> depending way. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> New brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotHistogram::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
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
<h3>void QwtPlotHistogram::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen, that is used in a <code>style()</code> depending way. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> New pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotHistogram::setSamples (const QVector&lt; <code>QwtIntervalSample</code> &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<h3>void QwtPlotHistogram::setSamples (<code>QwtSeriesData</code>&lt; <code>QwtIntervalSample</code> &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotHistogram::setStyle (<code>HistogramStyle</code>style)</h3>
<p>Set the histogram&#8217;s drawing style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Histogram style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>HistogramStyle</code>, <code>style()</code></dl>
<h3>void QwtPlotHistogram::setSymbol (const <code>QwtColumnSymbol</code> *symbol)</h3>
<p>Assign a symbol. In Column style an optional symbol can be assigned, that is responsible for displaying the rectangle that is defined by the interval and the distance between <code>baseline()</code> and value. When no symbol has been defined the area is displayed as plain rectangle using <code>pen()</code> and <code>brush()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code>, <code>symbol()</code>, <code>drawColumn()</code>, <code>pen()</code>, <code>brush()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>In applications, where different intervals need to be displayed in a different way ( f.e different colors or even using different symbols) it is recommended to overload <code>drawColumn()</code>.</dl>
<h3><code>QwtPlotHistogram::HistogramStyle</code> QwtPlotHistogram::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Style of the histogram</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>HistogramStyle</code>, <code>setStyle()</code></dl>
<h3>const <code>QwtColumnSymbol</code> * QwtPlotHistogram::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol or NULL, when no symbol has been assigned</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
