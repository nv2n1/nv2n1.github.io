---
title: "qwtplotmultibarchart(3)"
name: "qwtplotmultibarchart"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotmultibarchart/"
description: "QwtPlotMultiBarChart –"
---

<p>QwtPlotMultiBarChart &#8211; </p>
<p> <code>QwtPlotMultiBarChart</code> displays a series of a samples that consist each of a set of values.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_multi_barchart.h&gt; </p>
<p> Inherits <code>QwtPlotAbstractBarChart</code>, and <code>QwtSeriesStore&lt; QwtSetSample &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ChartStyle</code> { <code>Grouped</code>, <code>Stacked</code> }<br />
 <i>Chart styles. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotMultiBarChart</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotMultiBarChart</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotMultiBarChart</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setBarTitles</code> (const QList&lt; <code>QwtText</code> &gt; &amp;)<br />
 <i>Set the titles for the bars. </i><br />
 QList&lt; <code>QwtText</code> &gt; <code>barTitles</code> () const </p>
<p> void <code>setSamples</code> (const QVector&lt; <code>QwtSetSample</code> &gt; &amp;) </p>
<p> void <code>setSamples</code> (const QVector&lt; QVector&lt; double &gt; &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; <code>QwtSetSample</code> &gt; *) </p>
<p> void <code>setStyle</code> (<code>ChartStyle</code> <code>style</code>) </p>
<p> <code>ChartStyle</code> <code>style</code> () const </p>
<p> void <code>setSymbol</code> (int barIndex, <code>QwtColumnSymbol</code> *<code>symbol</code>)<br />
 <i>Add a symbol to the symbol map. </i><br />
 const <code>QwtColumnSymbol</code> * <code>symbol</code> (int barIndex) const </p>
<p> void <code>resetSymbolMap</code> () </p>
<p> virtual void <code>drawSeries</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual QList&lt; <code>QwtLegendData</code> &gt; <code>legendData</code> () const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p><code>QwtColumnSymbol</code> * <code>symbol</code> (int barIndex) </p>
<p> virtual <code>QwtColumnSymbol</code> * <code>specialSymbol</code> (int sampleIndex, int valueIndex) const<br />
 <i>Create a symbol for special values. </i><br />
 virtual void <code>drawSample</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, const <code>QwtInterval</code> &amp;boundingInterval, int index, const <code>QwtSetSample</code> &amp;<code>sample</code>) const </p>
<p> virtual void <code>drawBar</code> (QPainter *, int sampleIndex, int barIndex, const <code>QwtColumnRect</code> &amp;) const </p>
<p> void <code>drawStackedBars</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int index, double <code>sampleWidth</code>, const <code>QwtSetSample</code> &amp;<code>sample</code>) const </p>
<p> void <code>drawGroupedBars</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int index, double <code>sampleWidth</code>, const <code>QwtSetSample</code> &amp;<code>sample</code>) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotMultiBarChart</code> displays a series of a samples that consist each of a set of values. </p>
<p> Each value is displayed as a bar, the bars of each set can be organized side by side or accumulated. </p>
<p> Each bar of a set is rendered by a <code>QwtColumnSymbol</code>, that is set by <code>setSymbol()</code>. The bars of different sets use the same symbols. Exceptions are possible by overloading <code>specialSymbol()</code> or overloading <code>drawBar()</code>. </p>
<p> Depending on its <code>orientation()</code> the bars are displayed horizontally or vertically. The bars cover the interval between the <code>baseline()</code> and the value. </p>
<p> In opposite to most other plot items, <code>QwtPlotMultiBarChart</code> returns more than one entry for the legend &#8211; one for each symbol. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotBarChart</code>, <code>QwtPlotHistogram</code> <code>QwtPlotSeriesItem::orientation()</code>, <code>QwtPlotAbstractBarChart::baseline()</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotMultiBarChart::ChartStyle</code></h3>
<p>Chart styles. The default setting is <code>QwtPlotMultiBarChart::Grouped</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Grouped </i></p>
<dd>The bars of a set are displayed side by side.</p>
<dt><i>Stacked </i></p>
<dd>The bars are displayed on top of each other accumulating to a single bar. All values of a set need to have the same sign.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotMultiBarChart::QwtPlotMultiBarChart (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the chart</dl>
<h3>QwtPlotMultiBarChart::QwtPlotMultiBarChart (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the chart</dl>
<h2>Member Function Documentation</h2>
<h3>QList&lt; <code>QwtText</code> &gt; QwtPlotMultiBarChart::barTitles () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bar titles</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBarTitles()</code>, <code>legendData()</code></dl>
<h3>QRectF QwtPlotMultiBarChart::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of all samples. For an empty series the rectangle is invalid.</dl>
<p> Reimplemented from <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotMultiBarChart::drawBar (QPainter *painter, intsampleIndex, intvalueIndex, const <code>QwtColumnRect</code> &amp;rect) const [protected], [virtual]</h3>
<p>Draw a bar </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>sampleIndex</i> Index of the sample &#8211; might be -1 when the bar is painted for the legend<br />
 <i>valueIndex</i> Index of a value in a set<br />
 <i>rect</i> Directed target rectangle for the bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code></dl>
<h3>void QwtPlotMultiBarChart::drawGroupedBars (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intindex, doublesampleWidth, const <code>QwtSetSample</code> &amp;sample) const [protected]</h3>
<p>Draw a grouped sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>index</i> Index of the sample to be painted<br />
 <i>sampleWidth</i> Boundng width for all bars of the smaple<br />
 <i>sample</i> Sample</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code>, <code>sampleWidth()</code></dl>
<h3>void QwtPlotMultiBarChart::drawSample (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, const <code>QwtInterval</code> &amp;boundingInterval, intindex, const <code>QwtSetSample</code> &amp;sample) const [protected], [virtual]</h3>
<p>Draw a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>boundingInterval</i> Bounding interval of sample values<br />
 <i>index</i> Index of the sample to be painted<br />
 <i>sample</i> Sample value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code></dl>
<h3>void QwtPlotMultiBarChart::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw an interval of the bar chart </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted. If to &lt; 0 the curve will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>drawSymbols()</dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotMultiBarChart::drawStackedBars (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intindex, doublesampleWidth, const <code>QwtSetSample</code> &amp;sample) const [protected]</h3>
<p>Draw a stacked sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>index</i> Index of the sample to be painted<br />
 <i>sampleWidth</i> Width of the bars<br />
 <i>sample</i> Sample</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code>, <code>sampleWidth()</code></dl>
<h3>QList&lt; <code>QwtLegendData</code> &gt; QwtPlotMultiBarChart::legendData () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Information to be displayed on the legend</dl>
<p> The chart is represented by a list of entries &#8211; one for each bar title. Each element contains a bar title and an icon showing its corresponding bar. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>barTitles()</code>, <code>legendIcon()</code>, <code>legendIconSize()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotMultiBarChart::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon for representing a bar on the legend</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the bar<br />
 <i>size</i> Icon size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An icon showing a bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawBar()</code>, <code>legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotMultiBarChart::resetSymbolMap ()</h3>
<p>Remove all symbols from the symbol map</p>
<h3>int QwtPlotMultiBarChart::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotBarChart</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotMultiBarChart::setBarTitles (const QList&lt; <code>QwtText</code> &gt; &amp;titles)</h3>
<p>Set the titles for the bars. The titles are used for the legend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>titles</i> Bar titles</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>barTitles()</code>, <code>legendData()</code></dl>
<h3>void QwtPlotMultiBarChart::setSamples (const QVector&lt; <code>QwtSetSample</code> &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<h3>void QwtPlotMultiBarChart::setSamples (const QVector&lt; QVector&lt; double &gt; &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<h3>void QwtPlotMultiBarChart::setSamples (<code>QwtSeriesData</code>&lt; <code>QwtSetSample</code> &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotMultiBarChart::setStyle (<code>ChartStyle</code>style)</h3>
<p>Set the style of the chart </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Chart style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code></dl>
<h3>void QwtPlotMultiBarChart::setSymbol (intvalueIndex, <code>QwtColumnSymbol</code> *symbol)</h3>
<p>Add a symbol to the symbol map. Assign a default symbol for drawing the bar representing all values with the same index in a set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>valueIndex</i> Index of a value in a set<br />
 <i>symbol</i> Symbol used for drawing a bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code>, <code>resetSymbolMap()</code>, <code>specialSymbol()</code></dl>
<h3><code>QwtColumnSymbol</code> * QwtPlotMultiBarChart::specialSymbol (intsampleIndex, intvalueIndex) const [protected], [virtual]</h3>
<p>Create a symbol for special values. Usually the symbols for displaying a bar are set by setSymbols() and common for all sets. By overloading <code>specialSymbol()</code> it is possible to create a temporary <code>symbol()</code> for displaying a special value. </p>
<p> The symbol has to be created by new each time <code>specialSymbol()</code> is called. As soon as the symbol is painted this symbol gets deleted. </p>
<p> When no symbol ( NULL ) is returned, the value will be displayed with the standard symbol that is used for all symbols with the same valueIndex. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sampleIndex</i> Index of the sample<br />
 <i>valueIndex</i> Index of the value in the set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL, meaning that the value is not special</dl>
<h3><code>QwtPlotMultiBarChart::ChartStyle</code> QwtPlotMultiBarChart::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Style of the chart</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h3>const <code>QwtColumnSymbol</code> * QwtPlotMultiBarChart::symbol (intvalueIndex) const</h3>
<p>Find a symbol in the symbol map </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>valueIndex</i> Index of a value in a set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The symbol, that had been set by <code>setSymbol()</code> or NULL.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code>, <code>specialSymbol()</code>, <code>drawBar()</code></dl>
<h3><code>QwtColumnSymbol</code> * QwtPlotMultiBarChart::symbol (intvalueIndex) [protected]</h3>
<p>Find a symbol in the symbol map </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>valueIndex</i> Index of a value in a set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The symbol, that had been set by <code>setSymbol()</code> or NULL.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code>, <code>specialSymbol()</code>, <code>drawBar()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
