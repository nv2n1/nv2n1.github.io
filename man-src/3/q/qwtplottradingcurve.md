---
title: "qwtplottradingcurve(3)"
name: "qwtplottradingcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplottradingcurve/"
description: "QwtPlotTradingCurve –"
---

<p>QwtPlotTradingCurve &#8211; </p>
<p> <code>QwtPlotTradingCurve</code> illustrates movements in the price of a financial instrument over time.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_tradingcurve.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>, and <code>QwtSeriesStore&lt; QwtOHLCSample &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>SymbolStyle</code> { <code>NoSymbol</code> = -1, <code>Bar</code>, <code>CandleStick</code>, <code>UserSymbol</code> = 100 }<br />
 <i>Symbol styles. </i><br />
 enum <code>Direction</code> { <code>Increasing</code>, <code>Decreasing</code> }<br />
 <i>Direction of a price movement. </i><br />
 enum <code>PaintAttribute</code> { <code>ClipSymbols</code> = 0x01 } </p>
<p> typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotTradingCurve</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotTradingCurve</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotTradingCurve</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setSamples</code> (const QVector&lt; <code>QwtOHLCSample</code> &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; <code>QwtOHLCSample</code> &gt; *) </p>
<p> void <code>setSymbolStyle</code> (<code>SymbolStyle</code> style) </p>
<p> <code>SymbolStyle</code> <code>symbolStyle</code> () const </p>
<p> void <code>setSymbolPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setSymbolPen</code> (const QPen &amp;)<br />
 <i>Set the symbol pen. </i><br />
 QPen <code>symbolPen</code> () const </p>
<p> void <code>setSymbolBrush</code> (<code>Direction</code>, const QBrush &amp;) </p>
<p> QBrush <code>symbolBrush</code> (<code>Direction</code>) const </p>
<p> void <code>setSymbolExtent</code> (double width)<br />
 <i>Set the extent of the symbol. </i><br />
 double <code>symbolExtent</code> () const </p>
<p> void <code>setMinSymbolWidth</code> (double) </p>
<p> double <code>minSymbolWidth</code> () const </p>
<p> void <code>setMaxSymbolWidth</code> (double) </p>
<p> double <code>maxSymbolWidth</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>init</code> ()<br />
 <i>Initialize internal members. </i><br />
 virtual void <code>drawSymbols</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>drawUserSymbol</code> (QPainter *, <code>SymbolStyle</code>, const <code>QwtOHLCSample</code> &amp;, Qt::Orientation, bool inverted, double width) const<br />
 <i>Draw a symbol for a symbol style &gt;= UserSymbol. </i><br />
 void <code>drawBar</code> (QPainter *painter, const <code>QwtOHLCSample</code> &amp;, Qt::Orientation, bool inverted, double width) const<br />
 <i>Draw a bar. </i><br />
 void <code>drawCandleStick</code> (QPainter *, const <code>QwtOHLCSample</code> &amp;, Qt::Orientation, double width) const<br />
 <i>Draw a candle stick. </i><br />
 virtual double <code>scaledSymbolWidth</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotTradingCurve</code> illustrates movements in the price of a financial instrument over time. </p>
<p> <code>QwtPlotTradingCurve</code> supports candlestick or bar ( OHLC ) charts that are used in the domain of technical analysis. </p>
<p> While the length ( height or width depending on <code>orientation()</code> ) of each symbol depends on the corresponding OHLC sample the size of the other dimension can be controlled using: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>setSymbolExtent()</code></p>
<dt>&bull;</p>
<dd>setSymbolMinWidth()</p>
<dt>&bull;</p>
<dd>setSymbolMaxWidth()</dl>
<p> The extent is a size in scale coordinates, so that the symbol width is increasing when the plot is zoomed in. Minimum/Maximum width is in widget coordinates independent from the zoom level. When setting the minimum and maximum to the same value, the width of the symbol is fixed.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotTradingCurve::Direction</code></h3>
<p>Direction of a price movement. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Increasing </i></p>
<dd>The closing price is higher than the opening price.</p>
<dt><i>Decreasing </i></p>
<dd>The closing price is lower than the opening price.</dl>
<h3>enum <code>QwtPlotTradingCurve::PaintAttribute</code></h3>
<p>Attributes to modify the drawing algorithm. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ClipSymbols </i></p>
<dd>Check if a symbol is on the plot canvas before painting it.</dl>
<h3>enum <code>QwtPlotTradingCurve::SymbolStyle</code></h3>
<p>Symbol styles. The default setting is QwtPlotSeriesItem::CandleStick. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbolStyle()</code>, <code>symbolStyle()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoSymbol </i></p>
<dd>Nothing is displayed.</p>
<dt><i>Bar </i></p>
<dd>A line on the chart shows the price range (the highest and lowest prices) over one unit of time, e.g. one day or one hour. Tick marks project from each side of the line indicating the opening and closing price.</p>
<dt><i>CandleStick </i></p>
<dd>The range between opening/closing price are displayed as a filled box. The fill brush depends on the direction of the price movement. The box is connected to the highest/lowest values by lines.</p>
<dt><i>UserSymbol </i></p>
<dd>SymbolTypes &gt;= UserSymbol are displayed by <code>drawUserSymbol()</code>, that needs to be overloaded and implemented in derived curve classes.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawUserSymbol()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotTradingCurve::QwtPlotTradingCurve (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotTradingCurve::QwtPlotTradingCurve (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPlotTradingCurve::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of all samples. For an empty series the rectangle is invalid.</dl>
<p> Reimplemented from <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotTradingCurve::drawBar (QPainter *painter, const <code>QwtOHLCSample</code> &amp;sample, Qt::Orientationorientation, boolinverted, doublewidth) const [protected]</h3>
<p>Draw a bar. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter, initialized with pen/brush<br />
 <i>sample</i> Sample, already translated into paint device coordinates<br />
 <i>orientation</i> Vertical or horizontal<br />
 <i>inverted</i> When inverted is false the open tick is painted to the left/top, otherwise it is painted right/bottom. The close tick is painted in the opposite direction of the open tick. painted in the opposite d opposite direction.<br />
 <i>width</i> Width or height of the candle, depending on the orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Bar</code></dl>
<h3>void QwtPlotTradingCurve::drawCandleStick (QPainter *painter, const <code>QwtOHLCSample</code> &amp;sample, Qt::Orientationorientation, doublewidth) const [protected]</h3>
<p>Draw a candle stick. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter, initialized with pen/brush<br />
 <i>sample</i> Samples already translated into paint device coordinates<br />
 <i>orientation</i> Vertical or horizontal<br />
 <i>width</i> Width or height of the candle, depending on the orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CandleStick</code></dl>
<h3>void QwtPlotTradingCurve::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw an interval of the curve </p>
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
<dd><code>drawSymbols()</code></dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotTradingCurve::drawSymbols (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw symbols </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawSeries()</code></dl>
<h3>void QwtPlotTradingCurve::drawUserSymbol (QPainter *painter, <code>SymbolStyle</code>symbolStyle, const <code>QwtOHLCSample</code> &amp;sample, Qt::Orientationorientation, boolinverted, doublesymbolWidth) const [protected], [virtual]</h3>
<p>Draw a symbol for a symbol style &gt;= UserSymbol. The implementation does nothing and is intended to be overloaded </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter, initialized with pen/brush<br />
 <i>symbolStyle</i> Symbol style<br />
 <i>sample</i> Samples already translated into paint device coordinates<br />
 <i>orientation</i> Vertical or horizontal<br />
 <i>inverted</i> True, when the opposite scale ( Qt::Vertical: x, Qt::Horizontal: y ) is increasing in the opposite direction as QPainter coordinates.<br />
 <i>symbolWidth</i> Width of the symbol in paint device coordinates</dl>
<h3><code>QwtGraphic</code> QwtPlotTradingCurve::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A rectangle filled with the color of the symbol pen</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( usually there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendIconSize()</code>, <code>legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>double QwtPlotTradingCurve::maxSymbolWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximum for the symbol width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaxSymbolWidth()</code>, <code>minSymbolWidth()</code>, <code>symbolExtent()</code></dl>
<h3>double QwtPlotTradingCurve::minSymbolWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minmum for the symbol width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinSymbolWidth()</code>, <code>maxSymbolWidth()</code>, <code>symbolExtent()</code></dl>
<h3>int QwtPlotTradingCurve::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotTradingCurve</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>double QwtPlotTradingCurve::scaledSymbolWidth (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [protected], [virtual]</h3>
<p>Calculate the symbol width in paint coordinates </p>
<p> The width is calculated by scaling the symbol extent into paint device coordinates bounded by the minimum/maximum symbol width. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Symbol width in paint coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbolExtent()</code>, <code>minSymbolWidth()</code>, <code>maxSymbolWidth()</code></dl>
<h3>void QwtPlotTradingCurve::setMaxSymbolWidth (doublewidth)</h3>
<p>Set a maximum for the symbol width </p>
<p> A value &lt;= 0.0 means an unlimited width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width in paint device coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxSymbolWidth()</code>, <code>setMinSymbolWidth()</code>, <code>setSymbolExtent()</code></dl>
<h3>void QwtPlotTradingCurve::setMinSymbolWidth (doublewidth)</h3>
<p>Set a minimum for the symbol width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width in paint device coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minSymbolWidth()</code>, <code>setMaxSymbolWidth()</code>, <code>setSymbolExtent()</code></dl>
<h3>void QwtPlotTradingCurve::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dl>
<h3>void QwtPlotTradingCurve::setSamples (const QVector&lt; <code>QwtOHLCSample</code> &gt; &amp;samples)</h3>
<p>Initialize data with an array of samples. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of samples</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtPlotSeriesItem::setData()</dl>
<h3>void QwtPlotTradingCurve::setSamples (<code>QwtSeriesData</code>&lt; <code>QwtOHLCSample</code> &gt; *data)</h3>
<p>Assign a series of samples </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotTradingCurve::setSymbolBrush (<code>Direction</code>direction, const QBrush &amp;brush)</h3>
<p>Set the symbol brush </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>direction</i> Direction type<br />
 <i>brush</i> Brush used to fill the body of all candlestick symbols with the direction</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbolBrush()</code>, <code>setSymbolPen()</code></dl>
<h3>void QwtPlotTradingCurve::setSymbolExtent (doubleextent)</h3>
<p>Set the extent of the symbol. The width of the symbol is given in scale coordinates. When painting a symbol the width is scaled into paint device coordinates by <code>scaledSymbolWidth()</code>. The scaled width is bounded by <code>minSymbolWidth()</code>, <code>maxSymbolWidth()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>extent</i> Symbol width in scale coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbolExtent()</code>, <code>scaledSymbolWidth()</code>, <code>setMinSymbolWidth()</code>, <code>setMaxSymbolWidth()</code></dl>
<h3>void QwtPlotTradingCurve::setSymbolPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign the symbol pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotTradingCurve::setSymbolPen (const QPen &amp;pen)</h3>
<p>Set the symbol pen. The symbol pen is used for rendering the lines of the bar or candlestick symbols </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbolPen()</code>, <code>setSymbolBrush()</code></dl>
<h3>void QwtPlotTradingCurve::setSymbolStyle (<code>SymbolStyle</code>style)</h3>
<p>Set the symbol style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Symbol style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbolStyle()</code>, <code>setSymbolExtent()</code>, <code>setSymbolPen()</code>, <code>setSymbolBrush()</code></dl>
<h3>QBrush QwtPlotTradingCurve::symbolBrush (<code>Direction</code>direction) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>direction</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used to fill the body of all candlestick symbols with the direction</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbolPen()</code>, <code>symbolBrush()</code></dl>
<h3>double QwtPlotTradingCurve::symbolExtent () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Extent of a symbol in scale coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbolExtent()</code>, <code>scaledSymbolWidth()</code>, <code>minSymbolWidth()</code>, <code>maxSymbolWidth()</code></dl>
<h3>QPen QwtPlotTradingCurve::symbolPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Symbol pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbolPen()</code>, <code>symbolBrush()</code></dl>
<h3><code>QwtPlotTradingCurve::SymbolStyle</code> QwtPlotTradingCurve::symbolStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Symbol style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbolStyle()</code>, <code>symbolExtent()</code>, <code>symbolPen()</code>, <code>symbolBrush()</code></dl>
<h3>bool QwtPlotTradingCurve::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PaintAttribute</code>, <code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
