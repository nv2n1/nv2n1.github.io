---
title: "qwtlegenditemmanager(3)"
name: "qwtlegenditemmanager"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlegenditemmanager/"
description: "QwtLegendItemManager – Abstract API to bind plot items to the legend."
---

<p>QwtLegendItemManager &#8211; Abstract API to bind plot items to the legend. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_legend_itemmanager.h">qwt_legend_itemmanager.h</a>&gt; </p>
<p> Inherited by <code>QwtPlotItem</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtLegendItemManager</code> () </p>
<p> virtual <code>~QwtLegendItemManager</code> () </p>
<p> virtual void <code>updateLegend</code> (<code>QwtLegend</code> *legend) const =0 </p>
<p> virtual QWidget * <code>legendItem</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>Abstract API to bind plot items to the legend.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLegendItemManager::QwtLegendItemManager () [inline]</h3>
<p>Constructor. </p>
<h3>virtual QwtLegendItemManager::~QwtLegendItemManager () [inline, virtual]</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3>virtual QWidget* QwtLegendItemManager::legendItem () const [pure virtual]</h3>
<p>Allocate the widget that represents the item on the legend </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Allocated widget</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>updateLegend()</code> QwtLegend()</dl>
<p> Implemented in <code>QwtPlotItem</code>.</p>
<h3>virtual void QwtLegendItemManager::updateLegend (<code>QwtLegend</code> * legend) const [pure virtual]</h3>
<p>Update the widget that represents the item on the legend </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>legend</i> Legend</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>legendItem()</code></dl>
<p> Implemented in <code>QwtPlotCurve</code>, and <code>QwtPlotItem</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
