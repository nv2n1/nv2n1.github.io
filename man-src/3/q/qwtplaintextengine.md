---
title: "qwtplaintextengine(3)"
name: "qwtplaintextengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplaintextengine/"
description: "QwtPlainTextEngine –"
---

<p>QwtPlainTextEngine &#8211; </p>
<p> A text engine for plain texts.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_text_engine.h&gt; </p>
<p> Inherits <code>QwtTextEngine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlainTextEngine</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlainTextEngine</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>heightForWidth</code> (const QFont &amp;font, int flags, const QString &amp;text, double width) const </p>
<p> virtual QSizeF <code>textSize</code> (const QFont &amp;font, int flags, const QString &amp;text) const </p>
<p> virtual void <code>draw</code> (QPainter *painter, const QRectF &amp;rect, int flags, const QString &amp;text) const<br />
 <i>Draw the text in a clipping rectangle. </i><br />
 virtual bool <code>mightRender</code> (const QString &amp;) const </p>
<p> virtual void <code>textMargins</code> (const QFont &amp;, const QString &amp;, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A text engine for plain texts. </p>
<p> <code>QwtPlainTextEngine</code> renders texts using the basic Qt classes QPainter and QFontMetrics.</p>
<h2>Member Function Documentation</h2>
<h3>void QwtPlainTextEngine::draw (QPainter *painter, const QRectF &amp;rect, intflags, const QString &amp;text) const [virtual]</h3>
<p>Draw the text in a clipping rectangle. A wrapper for QPainter::drawText. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Clipping rectangle<br />
 <i>flags</i> Bitwise OR of the flags used like in QPainter::drawText<br />
 <i>text</i> Text to be rendered</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>double QwtPlainTextEngine::heightForWidth (const QFont &amp;font, intflags, const QString &amp;text, doublewidth) const [virtual]</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>flags</i> Bitwise OR of the flags used like in QPainter::drawText<br />
 <i>text</i> Text to be rendered<br />
 <i>width</i> Width</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>bool QwtPlainTextEngine::mightRender (const QString &amp;) const [virtual]</h3>
<p>Test if a string can be rendered by this text engine. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Always true. All texts can be rendered by <code>QwtPlainTextEngine</code></dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>void QwtPlainTextEngine::textMargins (const QFont &amp;font, const QString &amp;, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const [virtual]</h3>
<p>Return margins around the texts </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>left</i> Return 0<br />
 <i>right</i> Return 0<br />
 <i>top</i> Return value for the top margin<br />
 <i>bottom</i> Return value for the bottom margin</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>QSizeF QwtPlainTextEngine::textSize (const QFont &amp;font, intflags, const QString &amp;text) const [virtual]</h3>
<p>Returns the size, that is needed to render text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>flags</i> Bitwise OR of the flags used like in QPainter::drawText<br />
 <i>text</i> Text to be rendered</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Caluclated size</dl>
<p> Implements <code>QwtTextEngine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
