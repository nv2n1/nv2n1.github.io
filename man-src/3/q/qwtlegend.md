---
title: "qwtlegend(3)"
name: "qwtlegend"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlegend/"
description: "QwtLegend –"
---

<p>QwtLegend &#8211; </p>
<p> The legend widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_legend.h&gt; </p>
<p> Inherits <code>QwtAbstractLegend</code>.</p>
<h3>Public Slots</h3>
<p>virtual void <code>updateLegend</code> (const QVariant &amp;, const QList&lt; <code>QwtLegendData</code> &gt; &amp;)<br />
 <i>Update the entries for an item. </i></p>
<h3>Signals</h3>
<p>void <code>clicked</code> (const QVariant &amp;<code>itemInfo</code>, int index) </p>
<p> void <code>checked</code> (const QVariant &amp;<code>itemInfo</code>, bool on, int index) </p>
<h3>Public Member Functions</h3>
<p><code>QwtLegend</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtLegend</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setMaxColumns</code> (uint numColums)<br />
 <i>Set the maximum number of entries in a row. </i><br />
 uint <code>maxColumns</code> () const </p>
<p> void <code>setDefaultItemMode</code> (<code>QwtLegendData::Mode</code>)<br />
 <i>Set the default mode for legend labels. </i><br />
 <code>QwtLegendData::Mode</code> <code>defaultItemMode</code> () const </p>
<p> QWidget * <code>contentsWidget</code> () </p>
<p> const QWidget * <code>contentsWidget</code> () const </p>
<p> QWidget * <code>legendWidget</code> (const QVariant &amp;) const </p>
<p> QList&lt; QWidget * &gt; <code>legendWidgets</code> (const QVariant &amp;) const </p>
<p> QVariant <code>itemInfo</code> (const QWidget *) const </p>
<p> virtual bool <code>eventFilter</code> (QObject *, QEvent *) </p>
<p> virtual QSize <code>sizeHint</code> () const<br />
 <i>Return a size hint. </i><br />
 virtual int <code>heightForWidth</code> (int w) const </p>
<p> QScrollBar * <code>horizontalScrollBar</code> () const </p>
<p> QScrollBar * <code>verticalScrollBar</code> () const </p>
<p> virtual void <code>renderLegend</code> (QPainter *, const QRectF &amp;, bool fillBackground) const </p>
<p> virtual void <code>renderItem</code> (QPainter *, const QWidget *, const QRectF &amp;, bool fillBackground) const </p>
<p> virtual bool <code>isEmpty</code> () const </p>
<p> virtual int <code>scrollExtent</code> (Qt::Orientation) const </p>
<h3>Protected Slots</h3>
<p>void <code>itemClicked</code> () </p>
<p> void <code>itemChecked</code> (bool) </p>
<h3>Protected Member Functions</h3>
<p>virtual QWidget * <code>createWidget</code> (const <code>QwtLegendData</code> &amp;) const<br />
 <i>Create a widget to be inserted into the legend. </i><br />
 virtual void <code>updateWidget</code> (QWidget *widget, const <code>QwtLegendData</code> &amp;data)<br />
 <i>Update the widget. </i></p>
<h2>Detailed Description</h2>
<p>The legend widget. </p>
<p> The <code>QwtLegend</code> widget is a tabular arrangement of legend items. Legend items might be any type of widget, but in general they will be a <code>QwtLegendLabel</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtLegendLabel</code>, <code>QwtPlotItem</code>, <code>QwtPlot</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLegend::QwtLegend (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtLegend::checked (const QVariant &amp;itemInfo, boolon, intindex) [signal]</h3>
<p>A signal which is emitted when the user has clicked on a legend label, which is in <code>QwtLegendData::Checkable</code> mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info for the item of the selected legend label<br />
 <i>index</i> Index of the legend label in the list of widgets that are associated with the plot item<br />
 <i>on</i> True when the legend label is checked</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>clicks are disabled as default</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultItemMode()</code>, <code>defaultItemMode()</code>, <code>QwtPlot::itemToInfo()</code></dl>
<h3>void QwtLegend::clicked (const QVariant &amp;itemInfo, intindex) [signal]</h3>
<p>A signal which is emitted when the user has clicked on a legend label, which is in <code>QwtLegendData::Clickable</code> mode. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info for the item item of the selected legend item<br />
 <i>index</i> Index of the legend label in the list of widgets that are associated with the plot item</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>clicks are disabled as default</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultItemMode()</code>, <code>defaultItemMode()</code>, <code>QwtPlot::itemToInfo()</code></dl>
<h3>QWidget * QwtLegend::contentsWidget ()</h3>
<p>The contents widget is the only child of the viewport of the internal QScrollArea and the parent widget of all legend items. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Container widget of the legend items</dl>
<h3>const QWidget * QwtLegend::contentsWidget () const</h3>
<p>The contents widget is the only child of the viewport of the internal QScrollArea and the parent widget of all legend items. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Container widget of the legend items</dl>
<h3>QWidget * QwtLegend::createWidget (const <code>QwtLegendData</code> &amp;data) const [protected], [virtual]</h3>
<p>Create a widget to be inserted into the legend. The default implementation returns a <code>QwtLegendLabel</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Attributes of the legend entry</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Widget representing data on the legend</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd><code>updateWidget()</code> will called soon after <code>createWidget()</code> with the same attributes.</dl>
<h3><code>QwtLegendData::Mode</code> QwtLegend::defaultItemMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Default item mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultItemMode()</code></dl>
<h3>bool QwtLegend::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Handle QEvent::ChildRemoved andQEvent::LayoutRequest events for the <code>contentsWidget()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Forwarded to QwtAbstractLegend::eventFilter()</dl>
<h3>int QwtLegend::heightForWidth (intwidth) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The preferred height, for a width.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<h3>QScrollBar * QwtLegend::horizontalScrollBar () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Horizontal scrollbar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>verticalScrollBar()</code></dl>
<h3>bool QwtLegend::isEmpty () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when no item is inserted</dl>
<p> Implements <code>QwtAbstractLegend</code>.</p>
<h3>void QwtLegend::itemChecked (boolon) [protected], [slot]</h3>
<p>Called internally when the legend has been checked Emits a <code>checked()</code> signal.</p>
<h3>void QwtLegend::itemClicked () [protected], [slot]</h3>
<p>Called internally when the legend has been clicked on. Emits a <code>clicked()</code> signal.</p>
<h3>QVariant QwtLegend::itemInfo (const QWidget *widget) const</h3>
<p>Find the item that is associated to a widget </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>widget</i> Widget on the legend</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Associated item info</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendWidget()</code></dl>
<h3>QWidget * QwtLegend::legendWidget (const QVariant &amp;itemInfo) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>First widget in the list of widgets associated to an item</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info about an item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemInfo()</code>, <code>QwtPlot::itemToInfo()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Almost all types of items have only one widget</dl>
<h3>QList&lt; QWidget * &gt; QwtLegend::legendWidgets (const QVariant &amp;itemInfo) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>List of widgets associated to a item</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info about an item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendWidget()</code>, <code>itemInfo()</code>, <code>QwtPlot::itemToInfo()</code></dl>
<h3>uint QwtLegend::maxColumns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximum number of entries in a row</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaxColumns()</code>, <code>QwtDynGridLayout::maxColumns()</code></dl>
<h3>void QwtLegend::renderItem (QPainter *painter, const QWidget *widget, const QRectF &amp;rect, boolfillBackground) const [virtual]</h3>
<p>Render a legend entry into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>widget</i> Widget representing a legend entry<br />
 <i>rect</i> Bounding rectangle<br />
 <i>fillBackground</i> When true, fill rect with the widget background</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>When widget is not derived from <code>QwtLegendLabel</code> renderItem does nothing beside the background</dl>
<h3>void QwtLegend::renderLegend (QPainter *painter, const QRectF &amp;rect, boolfillBackground) const [virtual]</h3>
<p>Render the legend into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Bounding rectangle<br />
 <i>fillBackground</i> When true, fill rect with the widget background</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderLegend()</code> is used by <code>QwtPlotRenderer</code> &#8211; not by <code>QwtLegend</code> itself</dl>
<p> Implements <code>QwtAbstractLegend</code>.</p>
<h3>int QwtLegend::scrollExtent (Qt::Orientationorientation) const [virtual]</h3>
<p>Return the extent, that is needed for the scrollbars </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Orientation (</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The width of the vertical scrollbar for Qt::Horizontal and v.v.</dl>
<p> Reimplemented from <code>QwtAbstractLegend</code>.</p>
<h3>void QwtLegend::setDefaultItemMode (<code>QwtLegendData::Mode</code>mode)</h3>
<p>Set the default mode for legend labels. Legend labels will be constructed according to the attributes in a <code>QwtLegendData</code> object. When it doesn&#8217;t contain a value for the QwtLegendData::ModeRole the label will be initialized with the default mode of the legend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Default item mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>itemMode(), <code>QwtLegendData::value()</code>, <code>QwtPlotItem::legendData()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the mode doesn&#8217;t have any effect on existing labels.</dl>
<h3>void QwtLegend::setMaxColumns (uintnumColums)</h3>
<p>Set the maximum number of entries in a row. F.e when the maximum is set to 1 all items are aligned vertically. 0 means unlimited </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numColums</i> Maximum number of entries in a row</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code>, <code>QwtDynGridLayout::setMaxColumns()</code></dl>
<h3>void QwtLegend::updateLegend (const QVariant &amp;itemInfo, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) [virtual], [slot]</h3>
<p>Update the entries for an item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info for an item<br />
 <i>data</i> List of legend entry attributes for the item</dl>
<h3>void QwtLegend::updateWidget (QWidget *widget, const <code>QwtLegendData</code> &amp;data) [protected], [virtual]</h3>
<p>Update the widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>widget</i> Usually a <code>QwtLegendLabel</code><br />
 <i>data</i> Attributes to be displayed</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>createWidget()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>When widget is no <code>QwtLegendLabel</code> <code>updateWidget()</code> does nothing.</dl>
<h3>QScrollBar * QwtLegend::verticalScrollBar () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Vertical scrollbar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>horizontalScrollBar()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
