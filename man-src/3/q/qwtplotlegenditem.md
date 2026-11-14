---
title: "qwtplotlegenditem(3)"
name: "qwtplotlegenditem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotlegenditem/"
description: "QwtPlotLegendItem –"
---

<p>QwtPlotLegendItem &#8211; </p>
<p> A class which draws a legend inside the plot canvas.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_legenditem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Types</h3>
<p>enum <code>BackgroundMode</code> { <code>LegendBackground</code>, <code>ItemBackground</code> }<br />
 <i>Background mode. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotLegendItem</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotLegendItem</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setAlignment</code> (Qt::Alignment)<br />
 <i>Set the alignmnet. </i><br />
 Qt::Alignment <code>alignment</code> () const </p>
<p> void <code>setMaxColumns</code> (uint)<br />
 <i>Limit the number of columns. </i><br />
 uint <code>maxColumns</code> () const </p>
<p> void <code>setMargin</code> (int)<br />
 <i>Set the margin around legend items. </i><br />
 int <code>margin</code> () const </p>
<p> void <code>setSpacing</code> (int)<br />
 <i>Set the spacing between the legend items. </i><br />
 int <code>spacing</code> () const </p>
<p> void <code>setItemMargin</code> (int) </p>
<p> int <code>itemMargin</code> () const </p>
<p> void <code>setItemSpacing</code> (int) </p>
<p> int <code>itemSpacing</code> () const </p>
<p> void <code>setFont</code> (const QFont &amp;) </p>
<p> QFont <code>font</code> () const </p>
<p> void <code>setBorderDistance</code> (int numPixels)<br />
 <i>Set the margin between the legend and the canvas border. </i><br />
 int <code>borderDistance</code> () const </p>
<p> void <code>setBorderRadius</code> (double) </p>
<p> double <code>borderRadius</code> () const </p>
<p> void <code>setBorderPen</code> (const QPen &amp;) </p>
<p> QPen <code>borderPen</code> () const </p>
<p> void <code>setBackgroundBrush</code> (const QBrush &amp;)<br />
 <i>Set the background brush. </i><br />
 QBrush <code>backgroundBrush</code> () const </p>
<p> void <code>setBackgroundMode</code> (<code>BackgroundMode</code>)<br />
 <i>Set the background mode. </i><br />
 <code>BackgroundMode</code> <code>backgroundMode</code> () const </p>
<p> void <code>setTextPen</code> (const QPen &amp;)<br />
 <i>Set the pen for drawing text labels. </i><br />
 QPen <code>textPen</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const </p>
<p> void <code>clearLegend</code> ()<br />
 <i>Remove all items from the legend. </i><br />
 virtual void <code>updateLegend</code> (const <code>QwtPlotItem</code> *, const QList&lt; <code>QwtLegendData</code> &gt; &amp;) </p>
<p> virtual QRect <code>geometry</code> (const QRectF &amp;canvasRect) const </p>
<p> virtual QSize <code>minimumSize</code> (const <code>QwtLegendData</code> &amp;) const </p>
<p> virtual int <code>heightForWidth</code> (const <code>QwtLegendData</code> &amp;, int w) const </p>
<p> QList&lt; const <code>QwtPlotItem</code> * &gt; <code>plotItems</code> () const </p>
<p> QList&lt; QRect &gt; <code>legendGeometries</code> (const <code>QwtPlotItem</code> *) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawLegendData</code> (QPainter *painter, const <code>QwtPlotItem</code> *, const <code>QwtLegendData</code> &amp;, const QRectF &amp;) const </p>
<p> virtual void <code>drawBackground</code> (QPainter *, const QRectF &amp;rect) const </p>
<h2>Detailed Description</h2>
<p>A class which draws a legend inside the plot canvas. </p>
<p> <code>QwtPlotLegendItem</code> can be used to draw a inside the plot canvas. It can be used together with a <code>QwtLegend</code> or instead of it to have more space for the plot canvas. </p>
<p> In opposite to <code>QwtLegend</code> the legend item is not interactive. To identify mouse clicks on a legend item an event filter needs to be installed catching mouse events ob the plot canvas. The geometries of the legend items are available using <code>legendGeometries()</code>. </p>
<p> The legend item is aligned to plot canvas according to its <code>alignment()</code> flags. It might have a background for the complete legend ( usually semi transparent ) or for each legend item. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>An external <code>QwtLegend</code> with a transparent background on top the plot canvas might be another option with a similar effect.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotLegendItem::BackgroundMode</code></h3>
<p>Background mode. Depending on the mode the complete legend or each item might have an background. </p>
<p> The default setting is LegendBackground. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBackgroundMode()</code>, <code>setBackgroundBrush()</code>, <code>drawBackground()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LegendBackground </i></p>
<dd>The legend has a background.</p>
<dt><i>ItemBackground </i></p>
<dd>Each item has a background.</dl>
<h2>Member Function Documentation</h2>
<h3>Qt::Alignment QwtPlotLegendItem::alignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Alignment flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignment()</code></dl>
<h3>QBrush QwtPlotLegendItem::backgroundBrush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush is used to fill the background</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBackgroundBrush()</code>, <code>backgroundMode()</code>, <code>drawBackground()</code></dl>
<h3><code>QwtPlotLegendItem::BackgroundMode</code> QwtPlotLegendItem::backgroundMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>backgroundMode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBackgroundMode()</code>, <code>backgroundBrush()</code>, <code>drawBackground()</code></dl>
<h3>int QwtPlotLegendItem::borderDistance () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Margin between the legend and the canvas border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>margin()</code></dl>
<h3>QPen QwtPlotLegendItem::borderPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen for drawing the border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderPen()</code>, <code>backgroundBrush()</code></dl>
<h3>double QwtPlotLegendItem::borderRadius () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Radius of the border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code>, <code>setBorderPen()</code></dl>
<h3>void QwtPlotLegendItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the legend </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x Scale Map<br />
 <i>yMap</i> y Scale Map<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotLegendItem::drawBackground (QPainter *painter, const QRectF &amp;rect) const [protected], [virtual]</h3>
<p>Draw a rounded rect </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Bounding rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code>, <code>setBorderPen()</code>, <code>setBackgroundBrush()</code>, <code>setBackgroundMode()</code></dl>
<h3>void QwtPlotLegendItem::drawLegendData (QPainter *painter, const <code>QwtPlotItem</code> *plotItem, const <code>QwtLegendData</code> &amp;data, const QRectF &amp;rect) const [protected], [virtual]</h3>
<p>Draw an entry on the legend </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt Painter<br />
 <i>plotItem</i> Plot item, represented by the entry<br />
 <i>data</i> Attributes of the legend entry<br />
 <i>rect</i> Bounding rectangle for the entry</dl>
<h3>QFont QwtPlotLegendItem::font () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Font used for drawing the text label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFont()</code></dl>
<h3>QRect QwtPlotLegendItem::geometry (const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Calculate the geometry of the legend on the canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvasRect</i> Geometry of the canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry of the legend</dl>
<h3>int QwtPlotLegendItem::heightForWidth (const <code>QwtLegendData</code> &amp;data, intwidth) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The preferred height, for a width.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Attributes of the legend entry<br />
 <i>width</i> Width</dl>
<h3>int QwtPlotLegendItem::itemMargin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Margin around each item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemMargin()</code>, <code>itemSpacing()</code>, <code>margin()</code>, <code>spacing()</code></dl>
<h3>int QwtPlotLegendItem::itemSpacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing inside of each item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemSpacing()</code>, <code>itemMargin()</code>, <code>margin()</code>, <code>spacing()</code></dl>
<h3>QList&lt; QRect &gt; QwtPlotLegendItem::legendGeometries (const <code>QwtPlotItem</code> *plotItem) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Geometries of the items of a plot item</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Usually a plot item has only one entry on the legend</dl>
<h3>int QwtPlotLegendItem::margin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Margin around the legend items</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code>, <code>spacing()</code>, <code>itemMargin()</code>, <code>itemSpacing()</code></dl>
<h3>uint QwtPlotLegendItem::maxColumns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximum number of columns</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code>, <code>QwtDynGridLayout::maxColumns()</code></dl>
<h3>QSize QwtPlotLegendItem::minimumSize (const <code>QwtLegendData</code> &amp;data) const [virtual]</h3>
<p>Minimum size hint needed to display an entry </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Attributes of the legend entry</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size</dl>
<h3>QList&lt; const <code>QwtPlotItem</code> * &gt; QwtPlotLegendItem::plotItems () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>All plot items with an entry on the legend</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>A plot item might have more than one entry on the legend</dl>
<h3>int QwtPlotLegendItem::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotLegend</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotLegendItem::setAlignment (Qt::Alignmentalignment)</h3>
<p>Set the alignmnet. Alignment means the position of the legend relative to the geometry of the plot canvas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alignment</i> Alignment flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alignment()</code>, <code>setMaxColumns()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>To align a legend with many items horizontally the number of columns need to be limited</dl>
<h3>void QwtPlotLegendItem::setBackgroundBrush (const QBrush &amp;brush)</h3>
<p>Set the background brush. The brush is used to fill the background </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>backgroundBrush()</code>, <code>setBackgroundMode()</code>, <code>drawBackground()</code></dl>
<h3>void QwtPlotLegendItem::setBackgroundMode (<code>BackgroundMode</code>mode)</h3>
<p>Set the background mode. Depending on the mode the complete legend or each item might have an background. </p>
<p> The default setting is LegendBackground. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>backgroundMode()</code>, <code>setBackgroundBrush()</code>, <code>drawBackground()</code></dl>
<h3>void QwtPlotLegendItem::setBorderDistance (intdistance)</h3>
<p>Set the margin between the legend and the canvas border. The default setting for the margin is 10 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>distance</i> Margin in pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code></dl>
<h3>void QwtPlotLegendItem::setBorderPen (const QPen &amp;pen)</h3>
<p>Set the pen for drawing the border </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Border pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderPen()</code>, <code>setBackgroundBrush()</code></dl>
<h3>void QwtPlotLegendItem::setBorderRadius (doubleradius)</h3>
<p>Set the radius for the border </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>radius</i> A value &lt;= 0 defines a rectangular border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderRadius()</code>, <code>setBorderPen()</code></dl>
<h3>void QwtPlotLegendItem::setFont (const QFont &amp;font)</h3>
<p>Change the font used for drawing the text label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Legend font</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>font()</code></dl>
<h3>void QwtPlotLegendItem::setItemMargin (intmargin)</h3>
<p>Set the margin around each item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemMargin()</code>, <code>setItemSpacing()</code>, <code>setMargin()</code>, <code>setSpacing()</code></dl>
<h3>void QwtPlotLegendItem::setItemSpacing (intspacing)</h3>
<p>Set the spacing inside of each item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemSpacing()</code>, <code>setItemMargin()</code>, <code>setMargin()</code>, <code>setSpacing()</code></dl>
<h3>void QwtPlotLegendItem::setMargin (intmargin)</h3>
<p>Set the margin around legend items. The default setting for the margin is 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin in pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>margin()</code>, <code>setSpacing()</code>, <code>setItemMargin()</code>, <code>setItemSpacing</code></dl>
<h3>void QwtPlotLegendItem::setMaxColumns (uintmaxColumns)</h3>
<p>Limit the number of columns. When aligning the legend horizontally ( Qt::AlignLeft, Qt::AlignRight ) the number of columns needs to be limited to avoid, that the width of the legend grows with an increasing number of entries. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxColumns</i> Maximum number of columns. 0 means unlimited.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code>, <code>QwtDynGridLayout::setMaxColumns()</code></dl>
<h3>void QwtPlotLegendItem::setSpacing (intspacing)</h3>
<p>Set the spacing between the legend items. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing in pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>, <code>setMargin()</code></dl>
<h3>void QwtPlotLegendItem::setTextPen (const QPen &amp;pen)</h3>
<p>Set the pen for drawing text labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Text pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>textPen()</code>, <code>setFont()</code></dl>
<h3>int QwtPlotLegendItem::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing between the legend items</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code>, <code>margin()</code>, <code>itemSpacing()</code>, <code>itemMargin()</code></dl>
<h3>QPen QwtPlotLegendItem::textPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen for drawing text labels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTextPen()</code>, <code>font()</code></dl>
<h3>void QwtPlotLegendItem::updateLegend (const <code>QwtPlotItem</code> *plotItem, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) [virtual]</h3>
<p>Update the legend items according to modifications of a plot item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plotItem</i> Plot item<br />
 <i>data</i> Attributes of the legend entries</dl>
<p> Reimplemented from <code>QwtPlotItem</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
