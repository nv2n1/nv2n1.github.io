---
title: "qwtplotabstractbarchart(3)"
name: "qwtplotabstractbarchart"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotabstractbarchart/"
description: "QwtPlotAbstractBarChart –"
---

<p>QwtPlotAbstractBarChart &#8211; </p>
<p> Abstract base class for bar chart items.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_abstract_barchart.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>. </p>
<p> Inherited by <code>QwtPlotBarChart</code>, and <code>QwtPlotMultiBarChart</code>.</p>
<h3>Public Types</h3>
<p>enum <code>LayoutPolicy</code> { <code>AutoAdjustSamples</code>, <code>ScaleSamplesToAxes</code>, <code>ScaleSampleToCanvas</code>, <code>FixedSampleSize</code> }<br />
 <i>Mode how to calculate the bar width. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotAbstractBarChart</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotAbstractBarChart</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setLayoutPolicy</code> (<code>LayoutPolicy</code>) </p>
<p> <code>LayoutPolicy</code> <code>layoutPolicy</code> () const </p>
<p> void <code>setLayoutHint</code> (double) </p>
<p> double <code>layoutHint</code> () const </p>
<p> void <code>setSpacing</code> (int)<br />
 <i>Set the spacing. </i><br />
 int <code>spacing</code> () const </p>
<p> void <code>setMargin</code> (int)<br />
 <i>Set the margin. </i><br />
 int <code>margin</code> () const </p>
<p> void <code>setBaseline</code> (double)<br />
 <i>Set the baseline. </i><br />
 double <code>baseline</code> () const </p>
<p> virtual void <code>getCanvasMarginHint</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const<br />
 <i>Calculate a hint for the canvas margin. </i></p>
<h3>Protected Member Functions</h3>
<p>double <code>sampleWidth</code> (const <code>QwtScaleMap</code> &amp;map, double canvasSize, double <code>dataSize</code>, double value) const </p>
<h2>Detailed Description</h2>
<p>Abstract base class for bar chart items. </p>
<p> In opposite to almost all other plot items bar charts can&#8217;t be displayed inside of their bounding rectangle and need a special API how to calculate the width of the bars and how they affect the layout of the attached plot.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotAbstractBarChart::LayoutPolicy</code></h3>
<p>Mode how to calculate the bar width. <code>setLayoutPolicy()</code>, <code>setLayoutHint()</code>, barWidthHint() </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AutoAdjustSamples </i></p>
<dd>The sample width is calculated by dividing the bounding rectangle by the number of samples. The <code>layoutHint()</code> is used as a minimum width in paint device coordinates.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>boundingRectangle()</dl>
<dl COMPACT>
<dt><i>ScaleSamplesToAxes </i></p>
<dd><code>layoutHint()</code> defines an interval in axis coordinates</p>
<dt><i>ScaleSampleToCanvas </i></p>
<dd>The bar width is calculated by multiplying <code>layoutHint()</code> with the height or width of the canvas.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>boundingRectangle()</dl>
<dl COMPACT>
<dt><i>FixedSampleSize </i></p>
<dd><code>layoutHint()</code> defines a fixed width in paint device coordinates.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotAbstractBarChart::QwtPlotAbstractBarChart (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the chart</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtPlotAbstractBarChart::baseline () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value for the origin of the bar chart</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBaseline()</code>, <code>QwtPlotSeriesItem::orientation()</code></dl>
<h3>void QwtPlotAbstractBarChart::getCanvasMarginHint (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const [virtual]</h3>
<p>Calculate a hint for the canvas margin. Bar charts need to reserve some space for displaying the bars for the first and the last sample. The hint is calculated from the <code>layoutHint()</code> depending on the <code>layoutPolicy()</code>. </p>
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
<dd>Margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>layoutPolicy()</code>, <code>layoutHint()</code>, <code>QwtPlotItem::Margins</code> <code>QwtPlot::getCanvasMarginsHint()</code>, <code>QwtPlot::updateCanvasMargins()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>double QwtPlotAbstractBarChart::layoutHint () const</h3>
<p>The combination of <code>layoutPolicy()</code> and <code>layoutHint()</code> define how the width of the bars is calculated </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Layout policy of the chart item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutPolicy</code>, <code>setLayoutHint()</code>, <code>layoutPolicy()</code></dl>
<h3><code>QwtPlotAbstractBarChart::LayoutPolicy</code> QwtPlotAbstractBarChart::layoutPolicy () const</h3>
<p>The combination of <code>layoutPolicy()</code> and <code>layoutHint()</code> define how the width of the bars is calculated </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Layout policy of the chart item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLayoutPolicy()</code>, <code>layoutHint()</code></dl>
<h3>int QwtPlotAbstractBarChart::margin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Margin between the outmost bars and the contentsRect() of the canvas.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code>, <code>spacing()</code></dl>
<h3>double QwtPlotAbstractBarChart::sampleWidth (const <code>QwtScaleMap</code> &amp;map, doublecanvasSize, doubleboundingSize, doublevalue) const [protected]</h3>
<p>Calculate the width for a sample in paint device coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>map</i> Scale map for the corresponding scale<br />
 <i>canvasSize</i> Size of the canvas in paint device coordinates<br />
 <i>boundingSize</i> Bounding size of the chart in plot coordinates ( used in AutoAdjustSamples mode )<br />
 <i>value</i> Value of the sample</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>layoutPolicy()</code>, <code>layoutHint()</code></dl>
<h3>void QwtPlotAbstractBarChart::setBaseline (doublevalue)</h3>
<p>Set the baseline. The baseline is the origin for the chart. Each bar is painted from the baseline in the direction of the sample value. In case of a horizontal <code>orientation()</code> the baseline is interpreted as x &#8211; otherwise as y &#8211; value. </p>
<p> The default value for the baseline is 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value for the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>baseline()</code>, <code>QwtPlotSeriesItem::orientation()</code></dl>
<h3>void QwtPlotAbstractBarChart::setLayoutHint (doublehint)</h3>
<p>The combination of <code>layoutPolicy()</code> and <code>layoutHint()</code> define how the width of the bars is calculated </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hint</i> Layout hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutPolicy</code>, <code>layoutPolicy()</code>, <code>layoutHint()</code></dl>
<h3>void QwtPlotAbstractBarChart::setLayoutPolicy (<code>LayoutPolicy</code>policy)</h3>
<p>The combination of <code>layoutPolicy()</code> and <code>layoutHint()</code> define how the width of the bars is calculated </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>policy</i> Layout policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>layoutPolicy()</code>, <code>layoutHint()</code></dl>
<h3>void QwtPlotAbstractBarChart::setMargin (intmargin)</h3>
<p>Set the margin. The margin is the distance between the outmost bars and the contentsRect() of the canvas. The default setting is 5 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>, <code>margin()</code></dl>
<h3>void QwtPlotAbstractBarChart::setSpacing (intspacing)</h3>
<p>Set the spacing. The spacing is the distance between 2 samples ( bars for <code>QwtPlotBarChart</code> or a group of bars for <code>QwtPlotMultiBarChart</code> ) in paint device coordinates. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code></dl>
<h3>int QwtPlotAbstractBarChart::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing between 2 samples ( bars or groups of bars )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code>, <code>margin()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
