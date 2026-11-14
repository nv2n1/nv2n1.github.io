---
title: "qwtcolumnsymbol(3)"
name: "qwtcolumnsymbol"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcolumnsymbol/"
description: "QwtColumnSymbol –"
---

<p>QwtColumnSymbol &#8211; </p>
<p> A drawing primitive for columns.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_column_symbol.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>NoStyle</code> = -1, <code>Box</code>, <code>UserStyle</code> = 1000 } </p>
<p> enum <code>FrameStyle</code> { <code>NoFrame</code>, <code>Plain</code>, <code>Raised</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtColumnSymbol</code> (<code>Style</code>=<code>NoStyle</code>) </p>
<p> virtual <code>~QwtColumnSymbol</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setFrameStyle</code> (<code>FrameStyle</code> <code>style</code>) </p>
<p> <code>FrameStyle</code> <code>frameStyle</code> () const </p>
<p> void <code>setLineWidth</code> (int width) </p>
<p> int <code>lineWidth</code> () const </p>
<p> void <code>setPalette</code> (const QPalette &amp;) </p>
<p> const QPalette &amp; <code>palette</code> () const </p>
<p> void <code>setStyle</code> (<code>Style</code>) </p>
<p> <code>Style</code> <code>style</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *, const <code>QwtColumnRect</code> &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>drawBox</code> (QPainter *, const <code>QwtColumnRect</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p>A drawing primitive for columns.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtColumnSymbol::FrameStyle</code></h3>
<p>Frame Style used in Box <code>style()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Style</code>, <code>setFrameStyle()</code>, <code>frameStyle()</code>, <code>setStyle()</code>, <code>setPalette()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoFrame </i></p>
<dd>No frame.</p>
<dt><i>Plain </i></p>
<dd>A plain frame style.</p>
<dt><i>Raised </i></p>
<dd>A raised frame style.</dl>
<h3>enum <code>QwtColumnSymbol::Style</code></h3>
<p>Style </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoStyle </i></p>
<dd>No Style, the symbol draws nothing.</p>
<dt><i>Box </i></p>
<dd>The column is painted with a frame depending on the <code>frameStyle()</code> and <code>lineWidth()</code> using the <code>palette()</code>.</p>
<dt><i>UserStyle </i></p>
<dd>Styles &gt;= <code>QwtColumnSymbol::UserStyle</code> are reserved for derived classes of <code>QwtColumnSymbol</code> that overload <code>draw()</code> with additional application specific symbol types.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtColumnSymbol::QwtColumnSymbol (<code>Style</code>style = <code>NoStyle</code>)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style of the symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code>, <code>Style</code></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtColumnSymbol::draw (QPainter *painter, const <code>QwtColumnRect</code> &amp;rect) const [virtual]</h3>
<p>Draw the symbol depending on its style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Directed rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawBox()</code></dl>
<h3>void QwtColumnSymbol::drawBox (QPainter *painter, const <code>QwtColumnRect</code> &amp;rect) const [protected]</h3>
<p>Draw the symbol when it is in Box style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Directed rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>draw()</code></dl>
<h3><code>QwtColumnSymbol::FrameStyle</code> QwtColumnSymbol::frameStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current frame style, that is used for the Box style.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFrameStyle()</code>, <code>lineWidth()</code>, <code>setStyle()</code></dl>
<h3>int QwtColumnSymbol::lineWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Line width of the frame, that is used for the Box style.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>frameStyle()</code>, <code>setStyle()</code></dl>
<h3>const QPalette &amp; QwtColumnSymbol::palette () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current palette</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPalette()</code></dl>
<h3>void QwtColumnSymbol::setFrameStyle (<code>FrameStyle</code>frameStyle)</h3>
<p>Set the frame, that is used for the Box style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>frameStyle</i> Frame style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>frameStyle()</code>, <code>setLineWidth()</code>, <code>setStyle()</code></dl>
<h3>void QwtColumnSymbol::setLineWidth (intwidth)</h3>
<p>Set the line width of the frame, that is used for the Box style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lineWidth()</code>, <code>setFrameStyle()</code></dl>
<h3>void QwtColumnSymbol::setPalette (const QPalette &amp;palette)</h3>
<p>Assign a palette for the symbol </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>palette</i> Palette</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>palette()</code>, <code>setStyle()</code></dl>
<h3>void QwtColumnSymbol::setStyle (<code>Style</code>style)</h3>
<p>Specify the symbol style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code>, <code>setPalette()</code></dl>
<h3><code>QwtColumnSymbol::Style</code> QwtColumnSymbol::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
