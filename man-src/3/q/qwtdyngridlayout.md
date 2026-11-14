---
title: "qwtdyngridlayout(3)"
name: "qwtdyngridlayout"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdyngridlayout/"
description: "QwtDynGridLayout –"
---

<p>QwtDynGridLayout &#8211; </p>
<p> The <code>QwtDynGridLayout</code> class lays out widgets in a grid, adjusting the number of columns and rows to the current size.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dyngrid_layout.h&gt; </p>
<p> Inherits QLayout.</p>
<h3>Public Member Functions</h3>
<p><code>QwtDynGridLayout</code> (QWidget *, int margin=0, int space=-1) </p>
<p> <code>QwtDynGridLayout</code> (int space=-1) </p>
<p> virtual <code>~QwtDynGridLayout</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>invalidate</code> ()<br />
 <i>Invalidate all internal caches. </i><br />
 void <code>setMaxColumns</code> (uint maxCols) </p>
<p> uint <code>maxColumns</code> () const<br />
 <i>Return the upper limit for the number of columns. </i><br />
 uint <code>numRows</code> () const </p>
<p> uint <code>numColumns</code> () const </p>
<p> virtual void <code>addItem</code> (QLayoutItem *)<br />
 <i>Add an item to the next free position. </i><br />
 virtual QLayoutItem * <code>itemAt</code> (int index) const </p>
<p> virtual QLayoutItem * <code>takeAt</code> (int index) </p>
<p> virtual int <code>count</code> () const </p>
<p> void <code>setExpandingDirections</code> (Qt::Orientations) </p>
<p> virtual Qt::Orientations <code>expandingDirections</code> () const<br />
 <i>Returns whether this layout can make use of more space than </i><code>sizeHint()</code>.<br />
 QList&lt; QRect &gt; <code>layoutItems</code> (const QRect &amp;, uint numCols) const </p>
<p> virtual int <code>maxItemWidth</code> () const </p>
<p> virtual void <code>setGeometry</code> (const QRect &amp;rect) </p>
<p> virtual bool <code>hasHeightForWidth</code> () const </p>
<p> virtual int <code>heightForWidth</code> (int) const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual bool <code>isEmpty</code> () const </p>
<p> uint <code>itemCount</code> () const </p>
<p> virtual uint <code>columnsForWidth</code> (int width) const<br />
 <i>Calculate the number of columns for a given width. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>layoutGrid</code> (uint numCols, QVector&lt; int &gt; &amp;rowHeight, QVector&lt; int &gt; &amp;colWidth) const </p>
<p> void <code>stretchGrid</code> (const QRect &amp;rect, uint numCols, QVector&lt; int &gt; &amp;rowHeight, QVector&lt; int &gt; &amp;colWidth) const </p>
<h2>Detailed Description</h2>
<p>The <code>QwtDynGridLayout</code> class lays out widgets in a grid, adjusting the number of columns and rows to the current size. </p>
<p> <code>QwtDynGridLayout</code> takes the space it gets, divides it up into rows and columns, and puts each of the widgets it manages into the correct cell(s). It lays out as many number of columns as possible (limited by <code>maxColumns()</code>).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDynGridLayout::QwtDynGridLayout (QWidget *parent, intmargin = 0, intspacing = -1) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget<br />
 <i>margin</i> Margin<br />
 <i>spacing</i> Spacing</dl>
<h3>QwtDynGridLayout::QwtDynGridLayout (intspacing = -1) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtDynGridLayout::addItem (QLayoutItem *item) [virtual]</h3>
<p>Add an item to the next free position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>item</i> Layout item</dl>
<h3>uint QwtDynGridLayout::columnsForWidth (intwidth) const [virtual]</h3>
<p>Calculate the number of columns for a given width. The calculation tries to use as many columns as possible ( limited by <code>maxColumns()</code> ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Available width for all columns</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of columns for a given width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code>, <code>setMaxColumns()</code></dl>
<h3>int QwtDynGridLayout::count () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of items in the layout</dl>
<h3>Qt::Orientations QwtDynGridLayout::expandingDirections () const [virtual]</h3>
<p>Returns whether this layout can make use of more space than <code>sizeHint()</code>. A value of Qt::Vertical or Qt::Horizontal means that it wants to grow in only one dimension, while Qt::Vertical | Qt::Horizontal means that it wants to grow in both dimensions. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Orientations, where the layout expands</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setExpandingDirections()</code></dl>
<h3>bool QwtDynGridLayout::hasHeightForWidth () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true: <code>QwtDynGridLayout</code> implements <code>heightForWidth()</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>heightForWidth()</code></dl>
<h3>int QwtDynGridLayout::heightForWidth (intwidth) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The preferred height for this layout, given a width.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hasHeightForWidth()</code></dl>
<h3>bool QwtDynGridLayout::isEmpty () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if this layout is empty.</dl>
<h3>QLayoutItem * QwtDynGridLayout::itemAt (intindex) const [virtual]</h3>
<p>Find the item at a specific index </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Item at a specific index</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>takeAt()</code></dl>
<h3>uint QwtDynGridLayout::itemCount () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>number of layout items</dl>
<h3>void QwtDynGridLayout::layoutGrid (uintnumColumns, QVector&lt; int &gt; &amp;rowHeight, QVector&lt; int &gt; &amp;colWidth) const [protected]</h3>
<p>Calculate the dimensions for the columns and rows for a grid of numColumns columns. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numColumns</i> Number of columns.<br />
 <i>rowHeight</i> Array where to fill in the calculated row heights.<br />
 <i>colWidth</i> Array where to fill in the calculated column widths.</dl>
<h3>QList&lt; QRect &gt; QwtDynGridLayout::layoutItems (const QRect &amp;rect, uintnumColumns) const</h3>
<p>Calculate the geometries of the layout items for a layout with numColumns columns and a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rect where to place the items<br />
 <i>numColumns</i> Number of columns</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>item geometries</dl>
<h3>uint QwtDynGridLayout::maxColumns () const</h3>
<p>Return the upper limit for the number of columns. 0 means unlimited, what is the default. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Upper limit for the number of columns</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaxColumns()</code></dl>
<h3>int QwtDynGridLayout::maxItemWidth () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum width of all layout items</dl>
<h3>uint QwtDynGridLayout::numColumns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of columns of the current layout.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>numRows()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The number of columns might change whenever the geometry changes</dl>
<h3>uint QwtDynGridLayout::numRows () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of rows of the current layout.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>numColumns()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The number of rows might change whenever the geometry changes</dl>
<h3>void QwtDynGridLayout::setExpandingDirections (Qt::Orientationsexpanding)</h3>
<p>Set whether this layout can make use of more space than <code>sizeHint()</code>. A value of Qt::Vertical or Qt::Horizontal means that it wants to grow in only one dimension, while Qt::Vertical | Qt::Horizontal means that it wants to grow in both dimensions. The default value is 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>expanding</i> Or&#8217;d orientations</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>expandingDirections()</code></dl>
<h3>void QwtDynGridLayout::setGeometry (const QRect &amp;rect) [virtual]</h3>
<p>Reorganizes columns and rows and resizes managed items within a rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Layout geometry</dl>
<h3>void QwtDynGridLayout::setMaxColumns (uintmaxColumns)</h3>
<p>Limit the number of columns. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxColumns</i> upper limit, 0 means unlimited</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code></dl>
<h3>QSize QwtDynGridLayout::sizeHint () const [virtual]</h3>
<p>Return the size hint. If <code>maxColumns()</code> &gt; 0 it is the size for a grid with <code>maxColumns()</code> columns, otherwise it is the size for a grid with only one row. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxColumns()</code>, <code>setMaxColumns()</code></dl>
<h3>void QwtDynGridLayout::stretchGrid (const QRect &amp;rect, uintnumColumns, QVector&lt; int &gt; &amp;rowHeight, QVector&lt; int &gt; &amp;colWidth) const [protected]</h3>
<p>Stretch columns in case of expanding() &amp; QSizePolicy::Horizontal and rows in case of expanding() &amp; QSizePolicy::Vertical to fill the entire rect. Rows and columns are stretched with the same factor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle<br />
 <i>numColumns</i> Number of columns<br />
 <i>rowHeight</i> Array to be filled with the calculated row heights<br />
 <i>colWidth</i> Array to be filled with the calculated column widths</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>setExpanding(), expanding()</dl>
<h3>QLayoutItem * QwtDynGridLayout::takeAt (intindex) [virtual]</h3>
<p>Find the item at a specific index and remove it from the layout </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Layout item, removed from the layout</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemAt()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
