---
title: "qwtplotbarchart(3)"
name: "qwtplotbarchart"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotbarchart/"
description: "QwtPlotBarChart –"
---

<p>QwtPlotBarChart &#8211; </p>
<p> <code>QwtPlotBarChart</code> displays a series of a values as bars.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_barchart.h&gt; </p>
<p> Inherits <code>QwtPlotAbstractBarChart</code>, and <code>QwtSeriesStore&lt; QPointF &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>LegendMode</code> { <code>LegendChartTitle</code>, <code>LegendBarTitles</code> }<br />
 <i>Legend modes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotBarChart</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotBarChart</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotBarChart</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setSamples</code> (const QVector&lt; QPointF &gt; &amp;) </p>
<p> void <code>setSamples</code> (const QVector&lt; double &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; QPointF &gt; *series) </p>
<p> void <code>setSymbol</code> (<code>QwtColumnSymbol</code> *)<br />
 <i>Assign a symbol. </i><br />
 const <code>QwtColumnSymbol</code> * <code>symbol</code> () const </p>
<p> void <code>setLegendMode</code> (<code>LegendMode</code>) </p>
<p> <code>LegendMode</code> <code>legendMode</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual <code>QwtColumnSymbol</code> * <code>specialSymbol</code> (int sampleIndex, const QPointF &amp;) const </p>
<p> virtual <code>QwtText</code> <code>barTitle</code> (int sampleIndex) const<br />
 <i>Return the title of a bar. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawSample</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, const <code>QwtInterval</code> &amp;boundingInterval, int index, const QPointF &amp;<code>sample</code>) const </p>
<p> virtual void <code>drawBar</code> (QPainter *, int sampleIndex, const QPointF &amp;point, const <code>QwtColumnRect</code> &amp;) const </p>
<p> QList&lt; <code>QwtLegendData</code> &gt; <code>legendData</code> () const<br />
 <i>Return all information, that is needed to represent the item on the legend. </i><br />
 <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotBarChart</code> displays a series of a values as bars. </p>
<p> Each bar might be customized individually by implementing a <code>specialSymbol()</code>. Otherwise it is rendered using a default symbol. </p>
<p> Depending on its <code>orientation()</code> the bars are displayed horizontally or vertically. The bars cover the interval between the <code>baseline()</code> and the value. </p>
<p> By activating the LegendBarTitles mode each sample will have its own entry on the legend. </p>
<p> The most common use case of a bar chart is to display a list of y coordinates, where the x coordinate is simply the index in the list. But for other situations ( f.e. when values are related to dates ) it is also possible to set x coordinates explicitly. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotMultiBarChart</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotCurve::Sticks</code>, <code>QwtPlotSeriesItem::orientation()</code>, <code>QwtPlotAbstractBarChart::baseline()</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotBarChart::LegendMode</code></h3>
<p>Legend modes. The default setting is <code>QwtPlotBarChart::LegendChartTitle</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendMode()</code>, <code>legendMode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LegendChartTitle </i></p>
<dd>One entry on the legend showing the default symbol and the <code>title()</code> of the chart</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::title()</code></dl>
<dl COMPACT>
<dt><i>LegendBarTitles </i></p>
<dd>One entry for each value showing the individual symbol of the corresponding bar and the bar title.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>specialSymbol()</code>, <code>barTitle()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotBarChart::QwtPlotBarChart (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotBarChart::QwtPlotBarChart (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtText</code> QwtPlotBarChart::barTitle (intsampleIndex) const [virtual]</h3>
<p>Return the title of a bar. In LegendBarTitles mode the title is displayed on the legend entry corresponding to a bar. </p>
<p> The default implementation is a dummy, that is intended to be overloaded. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sampleIndex</i> Index of the bar</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An empty text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LegendBarTitles</code></dl>
<h3>QRectF QwtPlotBarChart::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of all samples. For an empty series the rectangle is invalid.</dl>
<p> Reimplemented from <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotBarChart::drawBar (QPainter *painter, intsampleIndex, const QPointF &amp;sample, const <code>QwtColumnRect</code> &amp;rect) const [protected], [virtual]</h3>
<p>Draw a bar </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>sampleIndex</i> Index of the sample represented by the bar<br />
 <i>sample</i> Value of the sample<br />
 <i>rect</i> Bounding rectangle of the bar</dl>
<h3>void QwtPlotBarChart::drawSample (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, const <code>QwtInterval</code> &amp;boundingInterval, intindex, const QPointF &amp;sample) const [protected], [virtual]</h3>
<p>Draw a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rect of the canvas<br />
 <i>boundingInterval</i> Bounding interval of sample values<br />
 <i>index</i> Index of the sample<br />
 <i>sample</i> Value of the sample</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code></dl>
<h3>void QwtPlotBarChart::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw an interval of the bar chart </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rect of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted. If to &lt; 0 the curve will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>drawSymbols()</dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>QList&lt; <code>QwtLegendData</code> &gt; QwtPlotBarChart::legendData () const [protected], [virtual]</h3>
<p>Return all information, that is needed to represent the item on the legend. In case of LegendBarTitles an entry for each bar is returned, otherwise the chart is represented like any other plot item from its <code>title()</code> and the <code>legendIcon()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Information, that is needed to represent the item on the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code>, <code>setLegendMode()</code>, <code>barTitle()</code>, <code>QwtLegend</code>, <code>QwtPlotLegendItem</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotBarChart::legendIcon (intindex, const QSizeF &amp;size) const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon representing a bar or the chart on the legend</dl>
<p> When the <code>legendMode()</code> is LegendBarTitles the icon shows the bar corresponding to index &#8211; otherwise the bar displays the default symbol. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendMode()</code>, <code>drawBar()</code>, <code>QwtPlotItem::setLegendIconSize()</code>, <code>QwtPlotItem::legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3><code>QwtPlotBarChart::LegendMode</code> QwtPlotBarChart::legendMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Legend mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendMode()</code></dl>
<h3>int QwtPlotBarChart::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotBarChart</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotBarChart::setLegendMode (<code>LegendMode</code>mode)</h3>
<p>Set the mode that decides what to display on the legend </p>
<p> In case of LegendBarTitles <code>barTitle()</code> needs to be overloaded to return individual titles for each bar. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> New mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendMode()</code>, <code>legendData()</code>, <code>barTitle()</code>, <code>QwtPlotItem::ItemAttribute</code></dl>
<h3>void QwtPlotBarChart::setSamples (const QVector&lt; QPointF &gt; &amp;samples)</h3>
<p>Initialize data with an array of points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>QVector is implicitly shared </p>
<p> QPolygonF is derived from QVector&lt;QPointF&gt;</dl>
<h3>void QwtPlotBarChart::setSamples (const QVector&lt; double &gt; &amp;samples)</h3>
<p>Initialize data with an array of doubles </p>
<p> The indices in the array are taken as x coordinate, while the doubles are interpreted as y values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of y coordinates</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>QVector is implicitly shared</dl>
<h3>void QwtPlotBarChart::setSamples (<code>QwtSeriesData</code>&lt; QPointF &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotBarChart::setSymbol (<code>QwtColumnSymbol</code> *symbol)</h3>
<p>Assign a symbol. The bar chart will take the ownership of the symbol, hence the previously set symbol will be delete by setting a new one. If symbol is NULL no symbol will be drawn. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> Symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code></dl>
<h3><code>QwtColumnSymbol</code> * QwtPlotBarChart::specialSymbol (intsampleIndex, const QPointF &amp;sample) const [virtual]</h3>
<p>Needs to be overloaded to return a non default symbol for a specific sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sampleIndex</i> Index of the sample represented by the bar<br />
 <i>sample</i> Value of the sample</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL, indicating to use the default symbol</dl>
<h3>const <code>QwtColumnSymbol</code> * QwtPlotBarChart::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol or NULL, when no symbol has been assigned</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
