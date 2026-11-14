---
title: "qwtrichtextengine(3)"
name: "qwtrichtextengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtrichtextengine/"
description: "QwtRichTextEngine –"
---

<p>QwtRichTextEngine &#8211; </p>
<p> A text engine for Qt rich texts.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_text_engine.h&gt; </p>
<p> Inherits <code>QwtTextEngine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtRichTextEngine</code> ()<br />
 <i>Constructor. </i><br />
 virtual double <code>heightForWidth</code> (const QFont &amp;font, int flags, const QString &amp;text, double width) const </p>
<p> virtual QSizeF <code>textSize</code> (const QFont &amp;font, int flags, const QString &amp;text) const </p>
<p> virtual void <code>draw</code> (QPainter *painter, const QRectF &amp;rect, int flags, const QString &amp;text) const </p>
<p> virtual bool <code>mightRender</code> (const QString &amp;) const </p>
<p> virtual void <code>textMargins</code> (const QFont &amp;, const QString &amp;, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A text engine for Qt rich texts. </p>
<p> <code>QwtRichTextEngine</code> renders Qt rich texts using the classes of the Scribe framework of Qt.</p>
<h2>Member Function Documentation</h2>
<h3>void QwtRichTextEngine::draw (QPainter *painter, const QRectF &amp;rect, intflags, const QString &amp;text) const [virtual]</h3>
<p>Draw the text in a clipping rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Clipping rectangle<br />
 <i>flags</i> Bitwise OR of the flags like in for QPainter::drawText()<br />
 <i>text</i> Text to be rendered</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>double QwtRichTextEngine::heightForWidth (const QFont &amp;font, intflags, const QString &amp;text, doublewidth) const [virtual]</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>flags</i> Bitwise OR of the flags used like in QPainter::drawText()<br />
 <i>text</i> Text to be rendered<br />
 <i>width</i> Width</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>bool QwtRichTextEngine::mightRender (const QString &amp;text) const [virtual]</h3>
<p>Test if a string can be rendered by this text engine </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text to be tested</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Qt::mightBeRichText(text);</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>void QwtRichTextEngine::textMargins (const QFont &amp;, const QString &amp;, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const [virtual]</h3>
<p>Return margins around the texts </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>left</i> Return 0<br />
 <i>right</i> Return 0<br />
 <i>top</i> Return 0<br />
 <i>bottom</i> Return 0</dl>
<p> Implements <code>QwtTextEngine</code>.</p>
<h3>QSizeF QwtRichTextEngine::textSize (const QFont &amp;font, intflags, const QString &amp;text) const [virtual]</h3>
<p>Returns the size, that is needed to render text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>flags</i> Bitwise OR of the flags used like in QPainter::drawText()<br />
 <i>text</i> Text to be rendered</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Caluclated size</dl>
<p> Implements <code>QwtTextEngine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
