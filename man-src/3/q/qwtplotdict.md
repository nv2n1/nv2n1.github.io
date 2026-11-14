---
title: "qwtplotdict(3)"
name: "qwtplotdict"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotdict/"
description: "QwtPlotDict –"
---

<p>QwtPlotDict &#8211; </p>
<p> A dictionary for plot items.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_dict.h&gt; </p>
<p> Inherited by <code>QwtPlot</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotDict</code> () </p>
<p> virtual <code>~QwtPlotDict</code> () </p>
<p> void <code>setAutoDelete</code> (bool) </p>
<p> bool <code>autoDelete</code> () const </p>
<p> const QwtPlotItemList &amp; <code>itemList</code> () const<br />
 <i>A QwtPlotItemList of all attached plot items. </i><br />
 QwtPlotItemList <code>itemList</code> (int rtti) const </p>
<p> void <code>detachItems</code> (int rtti=<code>QwtPlotItem::Rtti_PlotItem</code>, bool <code>autoDelete</code>=true) </p>
<h3>Protected Member Functions</h3>
<p>void <code>insertItem</code> (<code>QwtPlotItem</code> *) </p>
<p> void <code>removeItem</code> (<code>QwtPlotItem</code> *) </p>
<h2>Detailed Description</h2>
<p>A dictionary for plot items. </p>
<p> <code>QwtPlotDict</code> organizes plot items in increasing z-order. If <code>autoDelete()</code> is enabled, all attached items will be deleted in the destructor of the dictionary. <code>QwtPlotDict</code> can be used to get access to all <code>QwtPlotItem</code> items &#8211; or all items of a specific type &#8211; that are currently on the plot. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::attach()</code>, <code>QwtPlotItem::detach()</code>, <code>QwtPlotItem::z()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotDict::QwtPlotDict () [explicit]</h3>
<p>Constructor </p>
<p> Auto deletion is enabled. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAutoDelete()</code>, <code>QwtPlotItem::attach()</code></dl>
<h3>QwtPlotDict::~QwtPlotDict () [virtual]</h3>
<p>Destructor </p>
<p> If <code>autoDelete()</code> is on, all attached items will be deleted </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAutoDelete()</code>, <code>autoDelete()</code>, <code>QwtPlotItem::attach()</code></dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtPlotDict::autoDelete () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if auto deletion is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAutoDelete()</code>, <code>insertItem()</code></dl>
<h3>void QwtPlotDict::detachItems (intrtti = <code>QwtPlotItem::Rtti_PlotItem</code>, boolautoDelete = true)</h3>
<p>Detach items from the dictionary </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rtti</i> In case of <code>QwtPlotItem::Rtti_PlotItem</code> detach all items otherwise only those items of the type rtti.<br />
 <i>autoDelete</i> If true, delete all detached items</dl>
<h3>void QwtPlotDict::insertItem (<code>QwtPlotItem</code> *item) [protected]</h3>
<p>Insert a plot item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>item</i> PlotItem</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>removeItem()</code></dl>
<h3>const QwtPlotItemList &amp; QwtPlotDict::itemList () const</h3>
<p>A QwtPlotItemList of all attached plot items. Use caution when iterating these lists, as removing/detaching an item will invalidate the iterator. Instead you can place pointers to objects to be removed in a removal list, and traverse that list later. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>List of all attached plot items.</dl>
<h3>QwtPlotItemList QwtPlotDict::itemList (intrtti) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>List of all attached plot items of a specific type.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rtti</i> See <code>QwtPlotItem::RttiValues</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::rtti()</code></dl>
<h3>void QwtPlotDict::removeItem (<code>QwtPlotItem</code> *item) [protected]</h3>
<p>Remove a plot item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>item</i> PlotItem</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>insertItem()</code></dl>
<h3>void QwtPlotDict::setAutoDelete (boolautoDelete)</h3>
<p>En/Disable Auto deletion </p>
<p> If Auto deletion is on all attached plot items will be deleted in the destructor of <code>QwtPlotDict</code>. The default value is on. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>autoDelete()</code>, <code>insertItem()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
