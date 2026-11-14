---
title: "qwttextengine(3)"
name: "qwttextengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwttextengine/"
description: "QwtTextEngine –"
---

<p>QwtTextEngine &#8211; </p>
<p> Abstract base class for rendering text strings.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_text_engine.h&gt; </p>
<p> Inherited by <code>QwtMathMLTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtRichTextEngine</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~QwtTextEngine</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>heightForWidth</code> (const QFont &amp;font, int flags, const QString &amp;text, double width) const =0 </p>
<p> virtual QSizeF <code>textSize</code> (const QFont &amp;font, int flags, const QString &amp;text) const =0 </p>
<p> virtual bool <code>mightRender</code> (const QString &amp;text) const =0 </p>
<p> virtual void <code>textMargins</code> (const QFont &amp;font, const QString &amp;text, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const =0 </p>
<p> virtual void <code>draw</code> (QPainter *painter, const QRectF &amp;rect, int flags, const QString &amp;text) const =0 </p>
<h3>Protected Member Functions</h3>
<p><code>QwtTextEngine</code> ()<br />
 <i>Constructor. </i></p>
<h2>Detailed Description</h2>
<p>Abstract base class for rendering text strings. </p>
<p> A text engine is responsible for rendering texts for a specific text format. They are used by <code>QwtText</code> to render a text. </p>
<p> <code>QwtPlainTextEngine</code> and <code>QwtRichTextEngine</code> are part of the Qwt library. The implementation of <code>QwtMathMLTextEngine</code> uses code from the Qt solution package. Because of license implications it is built into a separate library. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtText::setTextEngine()</code></dl>
<h2>Member Function Documentation</h2>
<h3>virtual void QwtTextEngine::draw (QPainter *painter, const QRectF &amp;rect, intflags, const QString &amp;text) const [pure virtual]</h3>
<p>Draw the text in a clipping rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Clipping rectangle<br />
 <i>flags</i> Bitwise OR of the flags like in for QPainter::drawText()<br />
 <i>text</i> Text to be rendered</dl>
<p> Implemented in <code>QwtRichTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtMathMLTextEngine</code>.</p>
<h3>virtual double QwtTextEngine::heightForWidth (const QFont &amp;font, intflags, const QString &amp;text, doublewidth) const [pure virtual]</h3>
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
<p> Implemented in <code>QwtRichTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtMathMLTextEngine</code>.</p>
<h3>virtual bool QwtTextEngine::mightRender (const QString &amp;text) const [pure virtual]</h3>
<p>Test if a string can be rendered by this text engine </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text to be tested</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if it can be rendered</dl>
<p> Implemented in <code>QwtRichTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtMathMLTextEngine</code>.</p>
<h3>virtual void QwtTextEngine::textMargins (const QFont &amp;font, const QString &amp;text, double &amp;left, double &amp;right, double &amp;top, double &amp;bottom) const [pure virtual]</h3>
<p>Return margins around the texts </p>
<p> The textSize might include margins around the text, like QFontMetrics::descent(). In situations where texts need to be aligned in detail, knowing these margins might improve the layout calculations. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>text</i> Text to be rendered<br />
 <i>left</i> Return value for the left margin<br />
 <i>right</i> Return value for the right margin<br />
 <i>top</i> Return value for the top margin<br />
 <i>bottom</i> Return value for the bottom margin</dl>
<p> Implemented in <code>QwtRichTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtMathMLTextEngine</code>.</p>
<h3>virtual QSizeF QwtTextEngine::textSize (const QFont &amp;font, intflags, const QString &amp;text) const [pure virtual]</h3>
<p>Returns the size, that is needed to render text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the text<br />
 <i>flags</i> Bitwise OR of the flags like in for QPainter::drawText<br />
 <i>text</i> Text to be rendered</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated size</dl>
<p> Implemented in <code>QwtRichTextEngine</code>, <code>QwtPlainTextEngine</code>, and <code>QwtMathMLTextEngine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
