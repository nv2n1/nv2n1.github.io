---
title: "qwtlegenditem(3)"
name: "qwtlegenditem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlegenditem/"
description: "QwtLegendItem – A legend label."
---

<p>QwtLegendItem &#8211; A legend label. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_legend_item.h">qwt_legend_item.h</a>&gt; </p>
<p> Inherits <code>QwtTextLabel</code>. </p>
<h3>Public Types</h3>
<p>enum <code>IdentifierMode</code> { <code>NoIdentifier</code> = 0, <code>ShowLine</code> = 1, <code>ShowSymbol</code> = 2, <code>ShowText</code> = 4 } </p>
<h3>Public Slots</h3>
<p>void <code>setChecked</code> (bool on) </p>
<h3>Signals</h3>
<p>void <code>clicked</code> () </p>
<p> void <code>pressed</code> () </p>
<p> void <code>released</code> () </p>
<p> void <code>checked</code> (bool) </p>
<h3>Public Member Functions</h3>
<p><code>QwtLegendItem</code> (QWidget *parent=0) </p>
<p> <code>QwtLegendItem</code> (const <code>QwtSymbol</code> &amp;, const QPen &amp;, const <code>QwtText</code> &amp;, QWidget *parent=0) </p>
<p> virtual <code>~QwtLegendItem</code> () </p>
<p> virtual void <code>setText</code> (const <code>QwtText</code> &amp;) </p>
<p> void <code>setItemMode</code> (<code>QwtLegend::LegendItemMode</code>) </p>
<p> <code>QwtLegend::LegendItemMode</code> <code>itemMode</code> () const </p>
<p> void <code>setIdentifierMode</code> (int) </p>
<p> int <code>identifierMode</code> () const </p>
<p> void <code>setIdentifierWidth</code> (int width) </p>
<p> int <code>identifierWidth</code> () const </p>
<p> void <code>setSpacing</code> (int spacing) </p>
<p> int <code>spacing</code> () const </p>
<p> void <code>setSymbol</code> (const <code>QwtSymbol</code> &amp;) </p>
<p> const <code>QwtSymbol</code> &amp; <code>symbol</code> () const </p>
<p> void <code>setCurvePen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>curvePen</code> () const </p>
<p> virtual void <code>drawIdentifier</code> (QPainter *, const QRect &amp;) const </p>
<p> virtual void <code>drawItem</code> (QPainter *p, const QRect &amp;) const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> bool <code>isChecked</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>setDown</code> (bool) </p>
<p> bool <code>isDown</code> () const </p>
<p> virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>mousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>mouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>keyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>keyReleaseEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>drawText</code> (QPainter *, const QRect &amp;) </p>
<h2>Detailed Description</h2>
<p>A legend label. </p>
<p> <code>QwtLegendItem</code> represents a curve on a legend. It displays an curve identifier with an explaining text. The identifier might be a combination of curve symbol and line. In readonly mode it behaves like a label, otherwise like an unstylish push button. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtLegend</code>, <code>QwtPlotCurve</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtLegendItem::IdentifierMode</code></h3>
<p>Identifier mode. </p>
<p> Default is ShowLine | ShowText </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>identifierMode()</code>, <code>setIdentifierMode()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLegendItem::QwtLegendItem (QWidget * parent = 0) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h3>QwtLegendItem::QwtLegendItem (const <code>QwtSymbol</code> &amp; symbol, const QPen &amp; curvePen, const <code>QwtText</code> &amp; text, QWidget * parent = 0) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> Curve symbol<br />
 <i>curvePen</i> Curve pen<br />
 <i>text</i> Label text<br />
 <i>parent</i> Parent widget</dl>
<h3>QwtLegendItem::~QwtLegendItem () [virtual]</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3>void QwtLegendItem::checked (bool) [signal]</h3>
<p>Signal, when the legend item has been toggled. </p>
<h3>void QwtLegendItem::clicked () [signal]</h3>
<p>Signal, when the legend item has been clicked. </p>
<h3>const QPen &amp; QwtLegendItem::curvePen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The curve pen.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setCurvePen()</code></dl>
<h3>void QwtLegendItem::drawIdentifier (QPainter * painter, const QRect &amp; rect) const [virtual]</h3>
<p>Paint the identifier to a given rect. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Rect where to paint</dl>
<h3>void QwtLegendItem::drawItem (QPainter * painter, const QRect &amp; rect) const [virtual]</h3>
<p>Draw the legend item to a given rect. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Rect where to paint the button</dl>
<h3>void QwtLegendItem::drawText (QPainter * painter, const QRect &amp; textRect) [protected, virtual]</h3>
<p>Redraw the text. </p>
<p> Reimplemented from <code>QwtTextLabel</code>.</p>
<h3>int QwtLegendItem::identifierMode () const</h3>
<p>Or&#8217;d values of IdentifierMode. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setIdentifierMode()</code>, <code>IdentifierMode</code></dl>
<h3>int QwtLegendItem::identifierWidth () const</h3>
<p>Return the width of the identifier </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setIdentifierWidth()</code></dl>
<h3>bool QwtLegendItem::isChecked () const</h3>
<p>Return true, if the item is checked. </p>
<h3>bool QwtLegendItem::isDown () const [protected]</h3>
<p>Return true, if the item is down. </p>
<h3><code>QwtLegend::LegendItemMode</code> QwtLegendItem::itemMode () const</h3>
<p>Return the item mode </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setItemMode()</code></dl>
<h3>void QwtLegendItem::keyPressEvent (QKeyEvent * e) [protected, virtual]</h3>
<p>Handle key press events. </p>
<h3>void QwtLegendItem::keyReleaseEvent (QKeyEvent * e) [protected, virtual]</h3>
<p>Handle key release events. </p>
<h3>void QwtLegendItem::mousePressEvent (QMouseEvent * e) [protected, virtual]</h3>
<p>Handle mouse press events. </p>
<h3>void QwtLegendItem::mouseReleaseEvent (QMouseEvent * e) [protected, virtual]</h3>
<p>Handle mouse release events. </p>
<h3>void QwtLegendItem::paintEvent (QPaintEvent * e) [protected, virtual]</h3>
<p>Paint event. </p>
<p> Reimplemented from <code>QwtTextLabel</code>.</p>
<h3>void QwtLegendItem::pressed () [signal]</h3>
<p>Signal, when the legend item has been pressed. </p>
<h3>void QwtLegendItem::released () [signal]</h3>
<p>Signal, when the legend item has been relased. </p>
<h3>void QwtLegendItem::setChecked (bool on) [slot]</h3>
<p>Check/Uncheck a the item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> check/uncheck</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setItemMode()</code></dl>
<h3>void QwtLegendItem::setCurvePen (const QPen &amp; pen)</h3>
<p>Set curve pen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Curve pen</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>curvePen()</code></dl>
<h3>void QwtLegendItem::setDown (bool down) [protected]</h3>
<p>Set the item being down. </p>
<h3>void QwtLegendItem::setIdentifierMode (int mode)</h3>
<p>Set identifier mode. Default is ShowLine | ShowText. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Or&#8217;d values of IdentifierMode</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>identifierMode()</code></dl>
<h3>void QwtLegendItem::setIdentifierWidth (int width)</h3>
<p>Set the width for the identifier Default is 8 pixels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> New width</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>identifierMode()</code>, <code>identifierWidth()</code></dl>
<h3>void QwtLegendItem::setItemMode (<code>QwtLegend::LegendItemMode</code> mode)</h3>
<p>Set the item mode The default is QwtLegend::ReadOnlyItem </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Item mode</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>itemMode()</code></dl>
<h3>void QwtLegendItem::setSpacing (int spacing)</h3>
<p>Change the spacing </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>, <code>identifierWidth()</code>, <code>QwtTextLabel::margin()</code></dl>
<h3>void QwtLegendItem::setSymbol (const <code>QwtSymbol</code> &amp; symbol)</h3>
<p>Set curve symbol. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> Symbol</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code></dl>
<h3>void QwtLegendItem::setText (const <code>QwtText</code> &amp; text) [virtual]</h3>
<p>Set the text to the legend item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text label</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtTextLabel::text()</code></dl>
<p> Reimplemented from <code>QwtTextLabel</code>.</p>
<h3>QSize QwtLegendItem::sizeHint () const [virtual]</h3>
<p>Return a size hint. </p>
<p> Reimplemented from <code>QwtTextLabel</code>.</p>
<h3>int QwtLegendItem::spacing () const</h3>
<p>Return the spacing </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code>, <code>identifierWidth()</code>, <code>QwtTextLabel::margin()</code></dl>
<h3>const <code>QwtSymbol</code> &amp; QwtLegendItem::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The curve symbol.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
