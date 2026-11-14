---
title: "qwtintervalsymbol(3)"
name: "qwtintervalsymbol"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtintervalsymbol/"
description: "QwtIntervalSymbol –"
---

<p>QwtIntervalSymbol &#8211; </p>
<p> A drawing primitive for displaying an interval like an error bar.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_interval_symbol.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>NoSymbol</code> = -1, <code>Bar</code>, <code>Box</code>, <code>UserSymbol</code> = 1000 }<br />
 <i>Symbol style. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtIntervalSymbol</code> (<code>Style</code>=<code>NoSymbol</code>) </p>
<p> <code>QwtIntervalSymbol</code> (const <code>QwtIntervalSymbol</code> &amp;)<br />
 <i>Copy constructor. </i><br />
 virtual <code>~QwtIntervalSymbol</code> ()<br />
 <i>Destructor. </i><br />
 <code>QwtIntervalSymbol</code> &amp; <code>operator=</code> (const <code>QwtIntervalSymbol</code> &amp;)<br />
 <i>Assignment operator. </i><br />
 bool <code>operator==</code> (const <code>QwtIntervalSymbol</code> &amp;) const<br />
 <i>Compare two symbols. </i><br />
 bool <code>operator!=</code> (const <code>QwtIntervalSymbol</code> &amp;) const<br />
 <i>Compare two symbols. </i><br />
 void <code>setWidth</code> (int) </p>
<p> int <code>width</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;b)<br />
 <i>Assign a brush. </i><br />
 const QBrush &amp; <code>brush</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal <code>width</code>=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setStyle</code> (<code>Style</code>) </p>
<p> <code>Style</code> <code>style</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *, Qt::Orientation, const QPointF &amp;from, const QPointF &amp;to) const </p>
<h2>Detailed Description</h2>
<p>A drawing primitive for displaying an interval like an error bar. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotIntervalCurve</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtIntervalSymbol::Style</code></h3>
<p>Symbol style. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoSymbol </i></p>
<dd>No Style. The symbol cannot be drawn.</p>
<dt><i>Bar </i></p>
<dd>The symbol displays a line with caps at the beginning/end. The size of the caps depends on the symbol <code>width()</code>.</p>
<dt><i>Box </i></p>
<dd>The symbol displays a plain rectangle using <code>pen()</code> and <code>brush()</code>. The size of the rectangle depends on the translated interval and the <code>width()</code>,</p>
<dt><i>UserSymbol </i></p>
<dd>Styles &gt;= UserSymbol are reserved for derived classes of <code>QwtIntervalSymbol</code> that overload <code>draw()</code> with additional application specific symbol types.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtIntervalSymbol::QwtIntervalSymbol (<code>Style</code>style = <code>NoSymbol</code>)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style of the symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code>, <code>Style</code></dl>
<h2>Member Function Documentation</h2>
<h3>const QBrush &amp; QwtIntervalSymbol::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code></dl>
<h3>void QwtIntervalSymbol::draw (QPainter *painter, Qt::Orientationorientation, const QPointF &amp;from, const QPointF &amp;to) const [virtual]</h3>
<p>Draw a symbol depending on its style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>orientation</i> Orientation<br />
 <i>from</i> Start point of the interval in target device coordinates<br />
 <i>to</i> End point of the interval in target device coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h3>const QPen &amp; QwtIntervalSymbol::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>void QwtIntervalSymbol::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. The brush is used for the Box style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brush()</code></dl>
<h3>void QwtIntervalSymbol::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtIntervalSymbol::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>setBrush()</code></dl>
<h3>void QwtIntervalSymbol::setStyle (<code>Style</code>style)</h3>
<p>Specify the symbol style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code>, <code>Style</code></dl>
<h3>void QwtIntervalSymbol::setWidth (intwidth)</h3>
<p>Specify the width of the symbol It is used depending on the style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>width()</code>, <code>setStyle()</code></dl>
<h3><code>QwtIntervalSymbol::Style</code> QwtIntervalSymbol::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h3>int QwtIntervalSymbol::width () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the symbol.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWidth()</code>, <code>setStyle()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
