---
title: "qwtplotitem(3)"
name: "qwtplotitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotitem/"
description: "QwtPlotItem –"
---

<p>QwtPlotItem &#8211; </p>
<p> Base class for items on the plot canvas.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_item.h&gt; </p>
<p> Inherited by <code>QwtPlotGrid</code>, <code>QwtPlotLegendItem</code>, <code>QwtPlotMarker</code>, <code>QwtPlotRasterItem</code>, <code>QwtPlotScaleItem</code>, <code>QwtPlotSeriesItem</code>, <code>QwtPlotShapeItem</code>, <code>QwtPlotSvgItem</code>, <code>QwtPlotTextLabel</code>, and <code>QwtPlotZoneItem</code>.</p>
<h3>Public Types</h3>
<p>enum <code>RttiValues</code> { <code>Rtti_PlotItem</code> = 0, <code>Rtti_PlotGrid</code>, <code>Rtti_PlotScale</code>, <code>Rtti_PlotLegend</code>, <code>Rtti_PlotMarker</code>, <code>Rtti_PlotCurve</code>, <code>Rtti_PlotSpectroCurve</code>, <code>Rtti_PlotIntervalCurve</code>, <code>Rtti_PlotHistogram</code>, <code>Rtti_PlotSpectrogram</code>, <code>Rtti_PlotSVG</code>, <code>Rtti_PlotTradingCurve</code>, <code>Rtti_PlotBarChart</code>, <code>Rtti_PlotMultiBarChart</code>, <code>Rtti_PlotShape</code>, <code>Rtti_PlotTextLabel</code>, <code>Rtti_PlotZone</code>, <code>Rtti_PlotUserItem</code> = 1000 }<br />
 <i>Runtime type information. </i><br />
 enum <code>ItemAttribute</code> { <code>Legend</code> = 0x01, <code>AutoScale</code> = 0x02, <code>Margins</code> = 0x04 }<br />
 <i>Plot Item Attributes. </i><br />
 enum <code>ItemInterest</code> { <code>ScaleInterest</code> = 0x01, <code>LegendInterest</code> = 0x02 }<br />
 <i>Plot Item Interests. </i><br />
 enum <code>RenderHint</code> { <code>RenderAntialiased</code> = 0x1 }<br />
 <i>Render hints. </i><br />
 typedef QFlags&lt; <code>ItemAttribute</code> &gt; <code>ItemAttributes</code><br />
 <i>Plot Item Attributes. </i><br />
 typedef QFlags&lt; <code>ItemInterest</code> &gt; <code>ItemInterests</code><br />
 <i>Plot Item Interests. </i><br />
 typedef QFlags&lt; <code>RenderHint</code> &gt; <code>RenderHints</code><br />
 <i>Render hints. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotItem</code> (const <code>QwtText</code> &amp;<code>title</code>=<code>QwtText</code>()) </p>
<p> virtual <code>~QwtPlotItem</code> ()<br />
 <i>Destroy the </i><code>QwtPlotItem</code>.<br />
 void <code>attach</code> (<code>QwtPlot</code> *<code>plot</code>)<br />
 <i>Attach the item to a plot. </i><br />
 void <code>detach</code> ()<br />
 <i>This method detaches a </i><code>QwtPlotItem</code> from any <code>QwtPlot</code> it has been associated with.<br />
 <code>QwtPlot</code> * <code>plot</code> () const<br />
 <i>Return attached plot. </i><br />
 void <code>setTitle</code> (const QString &amp;<code>title</code>) </p>
<p> void <code>setTitle</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> const <code>QwtText</code> &amp; <code>title</code> () const </p>
<p> virtual int <code>rtti</code> () const </p>
<p> void <code>setItemAttribute</code> (<code>ItemAttribute</code>, bool on=true) </p>
<p> bool <code>testItemAttribute</code> (<code>ItemAttribute</code>) const </p>
<p> void <code>setItemInterest</code> (<code>ItemInterest</code>, bool on=true) </p>
<p> bool <code>testItemInterest</code> (<code>ItemInterest</code>) const </p>
<p> void <code>setRenderHint</code> (<code>RenderHint</code>, bool on=true) </p>
<p> bool <code>testRenderHint</code> (<code>RenderHint</code>) const </p>
<p> void <code>setRenderThreadCount</code> (uint numThreads) </p>
<p> uint <code>renderThreadCount</code> () const </p>
<p> void <code>setLegendIconSize</code> (const QSize &amp;) </p>
<p> QSize <code>legendIconSize</code> () const </p>
<p> double <code>z</code> () const </p>
<p> void <code>setZ</code> (double <code>z</code>)<br />
 <i>Set the z value. </i><br />
 void <code>show</code> ()<br />
 <i>Show the item. </i><br />
 void <code>hide</code> ()<br />
 <i>Hide the item. </i><br />
 virtual void <code>setVisible</code> (bool) </p>
<p> bool <code>isVisible</code> () const </p>
<p> void <code>setAxes</code> (int <code>xAxis</code>, int <code>yAxis</code>) </p>
<p> void <code>setXAxis</code> (int axis) </p>
<p> int <code>xAxis</code> () const<br />
 <i>Return xAxis. </i><br />
 void <code>setYAxis</code> (int axis) </p>
<p> int <code>yAxis</code> () const<br />
 <i>Return yAxis. </i><br />
 virtual void <code>itemChanged</code> () </p>
<p> virtual void <code>legendChanged</code> () </p>
<p> virtual void <code>draw</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const =0<br />
 <i>Draw the item. </i><br />
 virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual void <code>getCanvasMarginHint</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasSize, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const<br />
 <i>Calculate a hint for the canvas margin. </i><br />
 virtual void <code>updateScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;, const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Update the item to changes of the axes scale division. </i><br />
 virtual void <code>updateLegend</code> (const <code>QwtPlotItem</code> *, const QList&lt; <code>QwtLegendData</code> &gt; &amp;)<br />
 <i>Update the item to changes of the legend info. </i><br />
 QRectF <code>scaleRect</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;) const<br />
 <i>Calculate the bounding scale rectangle of 2 maps. </i><br />
 QRectF <code>paintRect</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;) const<br />
 <i>Calculate the bounding paint rectangle of 2 maps. </i><br />
 virtual QList&lt; <code>QwtLegendData</code> &gt; <code>legendData</code> () const<br />
 <i>Return all information, that is needed to represent the item on the legend. </i><br />
 virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p><code>QwtGraphic</code> <code>defaultIcon</code> (const QBrush &amp;, const QSizeF &amp;) const<br />
 <i>Return a default icon from a brush. </i></p>
<h2>Detailed Description</h2>
<p>Base class for items on the plot canvas. </p>
<p> A plot item is &#8216;something&#8217;, that can be painted on the plot canvas, or only affects the scales of the plot widget. They can be categorized as: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Representator </p>
<p>&nbsp;<wbr>A&nbsp;<wbr>&#8216;Representator&#8217;&nbsp;<wbr>is an item that represents some sort of data on the plot canvas. The different representator classes are organized according to the characteristics of the data:</p>
<dt> &bull;</p>
<dd><code>QwtPlotMarker</code> Represents a point or a horizontal/vertical coordinate</p>
<dt> &bull;</p>
<dd><code>QwtPlotCurve</code> Represents a series of points</p>
<dt> &bull;</p>
<dd><code>QwtPlotSpectrogram</code> ( <code>QwtPlotRasterItem</code> ) Represents raster data</p>
<dt> &bull;</p>
<dd>&#8230;</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Decorators </p>
<p>&nbsp;<wbr>A&nbsp;<wbr>&#8216;Decorator&#8217;&nbsp;<wbr>is an item, that displays additional information, that is not related to any data:</p>
<dt> &bull;</p>
<dd><code>QwtPlotGrid</code></p>
<dt> &bull;</p>
<dd><code>QwtPlotScaleItem</code></p>
<dt> &bull;</p>
<dd><code>QwtPlotSvgItem</code></p>
<dt> &bull;</p>
<dd>&#8230;</dl>
<p> Depending on the <code>QwtPlotItem::ItemAttribute</code> flags, an item is included into autoscaling or has an entry on the legend. </p>
<p> Before misusing the existing item classes it might be better to implement a new type of plot item ( don&#8217;t implement a watermark as spectrogram ). Deriving a new type of <code>QwtPlotItem</code> primarily means to implement the YourPlotItem::draw() method. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>The cpuplot example shows the implementation of additional <code>plot</code> items.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotItem::ItemAttribute</code></h3>
<p>Plot Item Attributes. Various aspects of a plot widget depend on the attributes of the attached plot items. If and how a single plot item participates in these updates depends on its attributes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemAttribute()</code>, <code>testItemAttribute()</code>, <code>ItemInterest</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Legend </i></p>
<dd>The item is represented on the legend.</p>
<dt><i>AutoScale </i></p>
<dd>The <code>boundingRect()</code> of the item is included in the autoscaling calculation as long as its width or height is &gt;= 0.0.</p>
<dt><i>Margins </i></p>
<dd>The item needs extra space to display something outside its bounding rectangle.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getCanvasMarginHint()</code></dl>
<h3>enum <code>QwtPlotItem::ItemInterest</code></h3>
<p>Plot Item Interests. Plot items might depend on the situation of the corresponding plot widget. By enabling an interest the plot item will be notified, when the corresponding attribute of the plot widgets has changed. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemAttribute()</code>, <code>testItemAttribute()</code>, <code>ItemInterest</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ScaleInterest </i></p>
<dd>The item is interested in updates of the scales</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateScaleDiv()</code></dl>
<dl COMPACT>
<dt><i>LegendInterest </i></p>
<dd>The item is interested in updates of the legend ( of other items ) This flag is intended for items, that want to implement a legend for displaying entries of other plot item.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If the plot item wants to be represented on a legend enable <code>QwtPlotItem::Legend</code> instead.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateLegend()</code></dl>
<h3>enum <code>QwtPlotItem::RenderHint</code></h3>
<p>Render hints. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>RenderAntialiased </i></p>
<dd>Enable antialiasing.</dl>
<h3>enum <code>QwtPlotItem::RttiValues</code></h3>
<p>Runtime type information. RttiValues is used to cast plot items, without having to enable runtime type information of the compiler. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Rtti_PlotItem </i></p>
<dd>Unspecific value, that can be used, when it doesn&#8217;t matter.</p>
<dt><i>Rtti_PlotGrid </i></p>
<dd>For <code>QwtPlotGrid</code>.</p>
<dt><i>Rtti_PlotScale </i></p>
<dd>For <code>QwtPlotScaleItem</code>.</p>
<dt><i>Rtti_PlotLegend </i></p>
<dd>For <code>QwtPlotLegendItem</code>.</p>
<dt><i>Rtti_PlotMarker </i></p>
<dd>For <code>QwtPlotMarker</code>.</p>
<dt><i>Rtti_PlotCurve </i></p>
<dd>For <code>QwtPlotCurve</code>.</p>
<dt><i>Rtti_PlotSpectroCurve </i></p>
<dd>For <code>QwtPlotSpectroCurve</code>.</p>
<dt><i>Rtti_PlotIntervalCurve </i></p>
<dd>For <code>QwtPlotIntervalCurve</code>.</p>
<dt><i>Rtti_PlotHistogram </i></p>
<dd>For <code>QwtPlotHistogram</code>.</p>
<dt><i>Rtti_PlotSpectrogram </i></p>
<dd>For <code>QwtPlotSpectrogram</code>.</p>
<dt><i>Rtti_PlotSVG </i></p>
<dd>For <code>QwtPlotSvgItem</code>.</p>
<dt><i>Rtti_PlotTradingCurve </i></p>
<dd>For <code>QwtPlotTradingCurve</code>.</p>
<dt><i>Rtti_PlotBarChart </i></p>
<dd>For <code>QwtPlotBarChart</code>.</p>
<dt><i>Rtti_PlotMultiBarChart </i></p>
<dd>For <code>QwtPlotMultiBarChart</code>.</p>
<dt><i>Rtti_PlotShape </i></p>
<dd>For <code>QwtPlotShapeItem</code>.</p>
<dt><i>Rtti_PlotTextLabel </i></p>
<dd>For <code>QwtPlotTextLabel</code>.</p>
<dt><i>Rtti_PlotZone </i></p>
<dd>For <code>QwtPlotZoneItem</code>.</p>
<dt><i>Rtti_PlotUserItem </i></p>
<dd>Values &gt;= Rtti_PlotUserItem are reserved for plot items not implemented in the Qwt library.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotItem::QwtPlotItem (const <code>QwtText</code> &amp;title = <code>QwtText</code>()) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the item</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotItem::attach (<code>QwtPlot</code> *plot)</h3>
<p>Attach the item to a plot. This method will attach a <code>QwtPlotItem</code> to the <code>QwtPlot</code> argument. It will first detach the <code>QwtPlotItem</code> from any plot from a previous call to attach (if necessary). If a NULL argument is passed, it will detach from any <code>QwtPlot</code> it was attached to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>detach()</code></dl>
<h3>QRectF QwtPlotItem::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>An invalid bounding rect: QRectF(1.0, 1.0, -2.0, -2.0)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>A width or height &lt; 0.0 is ignored by the autoscaler</dl>
<p> Reimplemented in <code>QwtPlotTradingCurve</code>, <code>QwtPlotMarker</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotRasterItem</code>, <code>QwtPlotShapeItem</code>, <code>QwtPlotBarChart</code>, <code>QwtPlotMultiBarChart</code>, <code>QwtPlotZoneItem</code>, <code>QwtPlotSeriesItem</code>, and <code>QwtPlotSvgItem</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotItem::defaultIcon (const QBrush &amp;brush, const QSizeF &amp;size) const [protected]</h3>
<p>Return a default icon from a brush. The default icon is a filled rectangle used in several derived classes as <code>legendIcon()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Fill brush<br />
 <i>size</i> Icon size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A filled rectangle</dl>
<h3>void QwtPlotItem::detach ()</h3>
<p>This method detaches a <code>QwtPlotItem</code> from any <code>QwtPlot</code> it has been associated with. <code>detach()</code> is equivalent to calling attach( NULL ) </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>attach()</code></dl>
<h3>virtual void QwtPlotItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [pure virtual]</h3>
<p>Draw the item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rect of the canvas in painter coordinates</dl>
<p> Implemented in <code>QwtPlotMarker</code>, <code>QwtPlotLegendItem</code>, <code>QwtPlotRasterItem</code>, <code>QwtPlotShapeItem</code>, <code>QwtPlotSpectrogram</code>, <code>QwtPlotScaleItem</code>, <code>QwtPlotGrid</code>, <code>QwtPlotTextLabel</code>, <code>QwtPlotZoneItem</code>, <code>QwtPlotSvgItem</code>, and <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotItem::getCanvasMarginHint (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const [virtual]</h3>
<p>Calculate a hint for the canvas margin. When the <code>QwtPlotItem::Margins</code> flag is enabled the plot item indicates, that it needs some margins at the borders of the canvas. This is f.e. used by bar charts to reserve space for displaying the bars. </p>
<p> The margins are in target device coordinates ( pixels on screen ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates<br />
 <i>left</i> Returns the left margin<br />
 <i>top</i> Returns the top margin<br />
 <i>right</i> Returns the right margin<br />
 <i>bottom</i> Returns the bottom margin</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The default implementation returns 0 for all margins</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::getCanvasMarginsHint()</code>, <code>QwtPlot::updateCanvasMargins()</code></dl>
<p> Reimplemented in <code>QwtPlotAbstractBarChart</code>.</p>
<h3>bool QwtPlotItem::isVisible () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if visible</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setVisible()</code>, <code>show()</code>, <code>hide()</code></dl>
<h3>void QwtPlotItem::itemChanged () [virtual]</h3>
<p>Update the legend and call <code>QwtPlot::autoRefresh()</code> for the parent plot. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtPlot::legendChanged(), <code>QwtPlot::autoRefresh()</code></dl>
<h3>void QwtPlotItem::legendChanged () [virtual]</h3>
<p>Update the legend of the parent plot. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::updateLegend()</code>, <code>itemChanged()</code></dl>
<h3>QList&lt; <code>QwtLegendData</code> &gt; QwtPlotItem::legendData () const [virtual]</h3>
<p>Return all information, that is needed to represent the item on the legend. Most items are represented by one entry on the legend showing an icon and a text, but f.e. <code>QwtPlotMultiBarChart</code> displays one entry for each bar. </p>
<p> <code>QwtLegendData</code> is basically a list of QVariants that makes it possible to overload and reimplement <code>legendData()</code> to return almost any type of information, that is understood by the receiver that acts as the legend. </p>
<p> The default implementation returns one entry with the <code>title()</code> of the item and the <code>legendIcon()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Data, that is needed to represent the item on the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code>, <code>legendIcon()</code>, <code>QwtLegend</code>, <code>QwtPlotLegendItem</code></dl>
<p> Reimplemented in <code>QwtPlotBarChart</code>, and <code>QwtPlotMultiBarChart</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotItem::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon representing the item on the legend</dl>
<p> The default implementation returns an invalid icon </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( usually there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendIconSize()</code>, <code>legendData()</code></dl>
<p> Reimplemented in <code>QwtPlotCurve</code>, <code>QwtPlotTradingCurve</code>, <code>QwtPlotMarker</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotBarChart</code>, <code>QwtPlotShapeItem</code>, and <code>QwtPlotMultiBarChart</code>.</p>
<h3>QSize QwtPlotItem::legendIconSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Legend icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendIconSize()</code>, <code>legendIcon()</code></dl>
<h3>QRectF QwtPlotItem::paintRect (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap) const</h3>
<p>Calculate the bounding paint rectangle of 2 maps. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding paint rectangle of the scale maps, not normalized</dl>
<h3>uint QwtPlotItem::renderThreadCount () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of threads to be used for rendering. If numThreads() is set to 0, the system specific ideal thread count is used.</dl>
<h3>int QwtPlotItem::rtti () const [virtual]</h3>
<p>Return rtti for the specific class represented. <code>QwtPlotItem</code> is simply a virtual interface class, and base classes will implement this method with specific rtti values so a user can differentiate them. </p>
<p> The rtti value is useful for environments, where the runtime type information is disabled and it is not possible to do a dynamic_cast&lt;&#8230;&gt;. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>rtti value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>RttiValues</code></dl>
<p> Reimplemented in <code>QwtPlotCurve</code>, <code>QwtPlotTradingCurve</code>, <code>QwtPlotShapeItem</code>, <code>QwtPlotSpectrogram</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotMarker</code>, <code>QwtPlotBarChart</code>, <code>QwtPlotMultiBarChart</code>, <code>QwtPlotLegendItem</code>, <code>QwtPlotScaleItem</code>, <code>QwtPlotTextLabel</code>, <code>QwtPlotSpectroCurve</code>, <code>QwtPlotSvgItem</code>, <code>QwtPlotGrid</code>, and <code>QwtPlotZoneItem</code>.</p>
<h3>QRectF QwtPlotItem::scaleRect (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap) const</h3>
<p>Calculate the bounding scale rectangle of 2 maps. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding scale rect of the scale maps, not normalized</dl>
<h3>void QwtPlotItem::setAxes (intxAxis, intyAxis)</h3>
<p>Set X and Y axis </p>
<p> The item will painted according to the coordinates of its Axes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> X Axis ( <code>QwtPlot::xBottom</code> or <code>QwtPlot::xTop</code> )<br />
 <i>yAxis</i> Y Axis ( <code>QwtPlot::yLeft</code> or <code>QwtPlot::yRight</code> )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setXAxis()</code>, <code>setYAxis()</code>, <code>xAxis()</code>, <code>yAxis()</code>, <code>QwtPlot::Axis</code></dl>
<h3>void QwtPlotItem::setItemAttribute (<code>ItemAttribute</code>attribute, boolon = true)</h3>
<p>Toggle an item attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute type<br />
 <i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testItemAttribute()</code>, <code>ItemInterest</code></dl>
<h3>void QwtPlotItem::setItemInterest (<code>ItemInterest</code>interest, boolon = true)</h3>
<p>Toggle an item interest </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interest</i> Interest type<br />
 <i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testItemInterest()</code>, <code>ItemAttribute</code></dl>
<h3>void QwtPlotItem::setLegendIconSize (const QSize &amp;size)</h3>
<p>Set the size of the legend icon </p>
<p> The default setting is 8&#215;8 pixels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendIconSize()</code>, <code>legendIcon()</code></dl>
<h3>void QwtPlotItem::setRenderHint (<code>RenderHint</code>hint, boolon = true)</h3>
<p>Toggle an render hint </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hint</i> Render hint<br />
 <i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testRenderHint()</code>, <code>RenderHint</code></dl>
<h3>void QwtPlotItem::setRenderThreadCount (uintnumThreads)</h3>
<p>On multi core systems rendering of certain plot item ( f.e <code>QwtPlotRasterItem</code> ) can be done in parallel in several threads. </p>
<p> The default setting is set to 1. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numThreads</i> Number of threads to be used for rendering. If numThreads is set to 0, the system specific ideal thread count is used.</dl>
<p> The default thread count is 1 ( = no additional threads )</p>
<h3>void QwtPlotItem::setTitle (const QString &amp;title)</h3>
<p>Set a new title </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code></dl>
<h3>void QwtPlotItem::setTitle (const <code>QwtText</code> &amp;title)</h3>
<p>Set a new title </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code></dl>
<h3>void QwtPlotItem::setVisible (boolon) [virtual]</h3>
<p>Show/Hide the item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Show if true, otherwise hide</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isVisible()</code>, <code>show()</code>, <code>hide()</code></dl>
<h3>void QwtPlotItem::setXAxis (intaxis)</h3>
<p>Set the X axis </p>
<p> The item will painted according to the coordinates its Axes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> X Axis ( <code>QwtPlot::xBottom</code> or <code>QwtPlot::xTop</code> )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxes()</code>, <code>setYAxis()</code>, <code>xAxis()</code>, <code>QwtPlot::Axis</code></dl>
<h3>void QwtPlotItem::setYAxis (intaxis)</h3>
<p>Set the Y axis </p>
<p> The item will painted according to the coordinates its Axes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Y Axis ( <code>QwtPlot::yLeft</code> or <code>QwtPlot::yRight</code> )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxes()</code>, <code>setXAxis()</code>, <code>yAxis()</code>, <code>QwtPlot::Axis</code></dl>
<h3>void QwtPlotItem::setZ (doublez)</h3>
<p>Set the z value. Plot items are painted in increasing z-order. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>z</i> Z-value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>z()</code>, <code>QwtPlotDict::itemList()</code></dl>
<h3>bool QwtPlotItem::testItemAttribute (<code>ItemAttribute</code>attribute) const</h3>
<p>Test an item attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute type</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemAttribute()</code>, <code>ItemInterest</code></dl>
<h3>bool QwtPlotItem::testItemInterest (<code>ItemInterest</code>interest) const</h3>
<p>Test an item interest </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interest</i> Interest type</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemInterest()</code>, <code>ItemAttribute</code></dl>
<h3>bool QwtPlotItem::testRenderHint (<code>RenderHint</code>hint) const</h3>
<p>Test a render hint </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hint</i> Render hint</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderHint()</code>, <code>RenderHint</code></dl>
<h3>const <code>QwtText</code> &amp; QwtPlotItem::title () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Title of the item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTitle()</code></dl>
<h3>void QwtPlotItem::updateLegend (const <code>QwtPlotItem</code> *item, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) [virtual]</h3>
<p>Update the item to changes of the legend info. Plot items that want to display a legend ( not those, that want to be displayed on a legend ! ) will have to implement <code>updateLegend()</code>. </p>
<p> <code>updateLegend()</code> is only called when the LegendInterest interest is enabled. The default implementation does nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>item</i> Plot item to be displayed on a legend<br />
 <i>data</i> Attributes how to display item on the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotLegendItem</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Plot items, that want to be displayed on a legend need to enable the <code>QwtPlotItem::Legend</code> flag and to implement <code>legendData()</code> and <code>legendIcon()</code></dl>
<p> Reimplemented in <code>QwtPlotLegendItem</code>.</p>
<h3>void QwtPlotItem::updateScaleDiv (const <code>QwtScaleDiv</code> &amp;xScaleDiv, const <code>QwtScaleDiv</code> &amp;yScaleDiv) [virtual]</h3>
<p>Update the item to changes of the axes scale division. Update the item, when the axes of plot have changed. The default implementation does nothing, but items that depend on the scale division (like <code>QwtPlotGrid()</code>) have to reimplement <code>updateScaleDiv()</code> </p>
<p> <code>updateScaleDiv()</code> is only called when the ScaleInterest interest is enabled. The default implementation does nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xScaleDiv</i> Scale division of the x-axis<br />
 <i>yScaleDiv</i> Scale division of the y-axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::updateAxes()</code>, <code>ScaleInterest</code></dl>
<p> Reimplemented in <code>QwtPlotScaleItem</code>, <code>QwtPlotGrid</code>, and <code>QwtPlotSeriesItem</code>.</p>
<h3>double QwtPlotItem::z () const</h3>
<p>Plot items are painted in increasing z-order. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>setZ()</code>, <code>QwtPlotDict::itemList()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
