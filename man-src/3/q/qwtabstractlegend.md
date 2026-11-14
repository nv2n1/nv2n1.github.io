---
title: "qwtabstractlegend(3)"
name: "qwtabstractlegend"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtabstractlegend/"
description: "QwtAbstractLegend –"
---

<p>QwtAbstractLegend &#8211; </p>
<p> Abstract base class for legend widgets.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_abstract_legend.h&gt; </p>
<p> Inherits QFrame. </p>
<p> Inherited by <code>QwtLegend</code>.</p>
<h3>Public Slots</h3>
<p>virtual void <code>updateLegend</code> (const QVariant &amp;itemInfo, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data)=0<br />
 <i>Update the entries for a plot item. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtAbstractLegend</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtAbstractLegend</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>renderLegend</code> (QPainter *painter, const QRectF &amp;rect, bool fillBackground) const =0 </p>
<p> virtual bool <code>isEmpty</code> () const =0 </p>
<p> virtual int <code>scrollExtent</code> (Qt::Orientation) const </p>
<h2>Detailed Description</h2>
<p>Abstract base class for legend widgets. </p>
<p> Legends, that need to be under control of the <code>QwtPlot</code> layout system need to be derived from <code>QwtAbstractLegend</code>. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Other type of legends can be implemented by connecting to the <code>QwtPlot::legendDataChanged()</code> signal. But as these legends are unknown to the plot layout system the layout code ( on screen and for <code>QwtPlotRenderer</code> ) need to be organized in application code.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtLegend</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAbstractLegend::QwtAbstractLegend (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>virtual bool QwtAbstractLegend::isEmpty () const [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when no plot item is inserted</dl>
<p> Implemented in <code>QwtLegend</code>.</p>
<h3>virtual void QwtAbstractLegend::renderLegend (QPainter *painter, const QRectF &amp;rect, boolfillBackground) const [pure virtual]</h3>
<p>Render the legend into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Bounding rectangle<br />
 <i>fillBackground</i> When true, fill rect with the widget background</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderLegend()</code> is used by <code>QwtPlotRenderer</code></dl>
<p> Implemented in <code>QwtLegend</code>.</p>
<h3>int QwtAbstractLegend::scrollExtent (Qt::Orientationorientation) const [virtual]</h3>
<p>Return the extent, that is needed for elements to scroll the legend ( usually scrollbars ), </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Orientation</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Extent of the corresponding scroll element</dl>
<p> Reimplemented in <code>QwtLegend</code>.</p>
<h3>virtual void QwtAbstractLegend::updateLegend (const QVariant &amp;itemInfo, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) [pure virtual], [slot]</h3>
<p>Update the entries for a plot item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info about an item<br />
 <i>data</i> List of legend entry attributes for the item</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
