---
title: "qwttext(3)"
name: "qwttext"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwttext/"
description: "QwtText –"
---

<p>QwtText &#8211; </p>
<p> A class representing a text.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_text.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>TextFormat</code> { <code>AutoText</code> = 0, <code>PlainText</code>, <code>RichText</code>, <code>MathMLText</code>, <code>TeXText</code>, <code>OtherFormat</code> = 100 }<br />
 <i>Text format. </i><br />
 enum <code>PaintAttribute</code> { <code>PaintUsingTextFont</code> = 0x01, <code>PaintUsingTextColor</code> = 0x02, <code>PaintBackground</code> = 0x04 }<br />
 <i>Paint Attributes. </i><br />
 enum <code>LayoutAttribute</code> { <code>MinimumLayout</code> = 0x01 }<br />
 <i>Layout Attributes The layout attributes affects some aspects of the layout of the text. </i><br />
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i><br />
 typedef QFlags&lt; <code>LayoutAttribute</code> &gt; <code>LayoutAttributes</code><br />
 <i>Layout attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtText</code> (const QString &amp;=QString::null, <code>TextFormat</code> textFormat=<code>AutoText</code>) </p>
<p> <code>QwtText</code> (const <code>QwtText</code> &amp;)<br />
 <i>Copy constructor. </i><br />
 <code>~QwtText</code> ()<br />
 <i>Destructor. </i><br />
 <code>QwtText</code> &amp; <code>operator=</code> (const <code>QwtText</code> &amp;)<br />
 <i>Assignment operator. </i><br />
 bool <code>operator==</code> (const <code>QwtText</code> &amp;) const<br />
 <i>Relational operator. </i><br />
 bool <code>operator!=</code> (const <code>QwtText</code> &amp;) const<br />
 <i>Relational operator. </i><br />
 void <code>setText</code> (const QString &amp;, <code>QwtText::TextFormat</code> textFormat=<code>AutoText</code>) </p>
<p> QString <code>text</code> () const </p>
<p> bool <code>isNull</code> () const </p>
<p> bool <code>isEmpty</code> () const </p>
<p> void <code>setFont</code> (const QFont &amp;) </p>
<p> QFont <code>font</code> () const<br />
 <i>Return the font. </i><br />
 QFont <code>usedFont</code> (const QFont &amp;) const </p>
<p> void <code>setRenderFlags</code> (int flags)<br />
 <i>Change the render flags. </i><br />
 int <code>renderFlags</code> () const </p>
<p> void <code>setColor</code> (const QColor &amp;) </p>
<p> QColor <code>color</code> () const<br />
 <i>Return the pen color, used for painting the text. </i><br />
 QColor <code>usedColor</code> (const QColor &amp;) const </p>
<p> void <code>setBorderRadius</code> (double) </p>
<p> double <code>borderRadius</code> () const </p>
<p> void <code>setBorderPen</code> (const QPen &amp;) </p>
<p> QPen <code>borderPen</code> () const </p>
<p> void <code>setBackgroundBrush</code> (const QBrush &amp;) </p>
<p> QBrush <code>backgroundBrush</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setLayoutAttribute</code> (<code>LayoutAttribute</code>, bool on=true) </p>
<p> bool <code>testLayoutAttribute</code> (<code>LayoutAttribute</code>) const </p>
<p> double <code>heightForWidth</code> (double width, const QFont &amp;=QFont()) const </p>
<p> QSizeF <code>textSize</code> (const QFont &amp;=QFont()) const </p>
<p> void <code>draw</code> (QPainter *painter, const QRectF &amp;rect) const </p>
<h3>Static Public Member Functions</h3>
<p>static const <code>QwtTextEngine</code> * <code>textEngine</code> (const QString &amp;<code>text</code>, <code>QwtText::TextFormat</code>=<code>AutoText</code>) </p>
<p> static const <code>QwtTextEngine</code> * <code>textEngine</code> (<code>QwtText::TextFormat</code>)<br />
 <i>Find the text engine for a text format. </i><br />
 static void <code>setTextEngine</code> (<code>QwtText::TextFormat</code>, <code>QwtTextEngine</code> *) </p>
<h2>Detailed Description</h2>
<p>A class representing a text. </p>
<p> A <code>QwtText</code> is a text including a set of attributes how to render it. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Format </p>
<p>&nbsp;<wbr>A text might include control sequences&nbsp;<wbr>(f.e tags)&nbsp;<wbr>describing how to render it. Each format&nbsp;<wbr>(f.e MathML, TeX, Qt Rich Text)&nbsp;<wbr>has its own set of control sequences, that can be handles by a special&nbsp;<wbr><code>QwtTextEngine</code>&nbsp;<wbr>for this format.</p>
<dt>&bull;</p>
<dd>Background </p>
<p>&nbsp;<wbr>A text might have a background, defined by a QPen and QBrush to improve its visibility. The corners of the background might be rounded.</p>
<dt>&bull;</p>
<dd>Font </p>
<p>&nbsp;<wbr>A text might have an individual font.</p>
<dt>&bull;</p>
<dd>Color </p>
<p>&nbsp;<wbr>A text might have an individual color.</p>
<dt>&bull;</p>
<dd>Render Flags </p>
<p>&nbsp;<wbr>Flags from Qt::AlignmentFlag and Qt::TextFlag used like in QPainter::drawText().</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTextEngine</code>, <code>QwtTextLabel</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtText::LayoutAttribute</code></h3>
<p>Layout Attributes The layout attributes affects some aspects of the layout of the text. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>MinimumLayout </i></p>
<dd>Layout the text without its margins. This mode is useful if a text needs to be aligned accurately, like the tick labels of a scale. If <code>QwtTextEngine::textMargins</code> is not implemented for the format of the text, MinimumLayout has no effect.</dl>
<h3>enum <code>QwtText::PaintAttribute</code></h3>
<p>Paint Attributes. Font and color and background are optional attributes of a <code>QwtText</code>. The paint attributes hold the information, if they are set. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>PaintUsingTextFont </i></p>
<dd>The text has an individual font.</p>
<dt><i>PaintUsingTextColor </i></p>
<dd>The text has an individual color.</p>
<dt><i>PaintBackground </i></p>
<dd>The text has an individual background.</dl>
<h3>enum <code>QwtText::TextFormat</code></h3>
<p>Text format. The text format defines the <code>QwtTextEngine</code>, that is used to render the text. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTextEngine</code>, <code>setTextEngine()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AutoText </i></p>
<dd>The text format is determined using <code>QwtTextEngine::mightRender()</code> for all available text engines in increasing order &gt; PlainText. If none of the text engines can render the text is rendered like <code>QwtText::PlainText</code>.</p>
<dt><i>PlainText </i></p>
<dd>Draw the text as it is, using a <code>QwtPlainTextEngine</code>.</p>
<dt><i>RichText </i></p>
<dd>Use the Scribe framework (Qt Rich Text) to render the text.</p>
<dt><i>MathMLText </i></p>
<dd></dl>
<pre> Use a MathML (<a rel="nofollow" href="http://en.wikipedia.org/wiki/MathML)">http://en.wikipedia.org/wiki/MathML)</a> render engine
 to display the text. The Qwt MathML extension offers such an engine
 based on the MathML renderer of the Qt solutions package. 
 To enable MathML support the following code needs to be added to the
 application:</pre>
<p>&nbsp;<wbr> </p>
<pre>QwtText::setTextEngine(QwtText::MathMLText, new QwtMathMLTextEngine()); </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>TeXText </i></p>
<dd>Use a TeX (<a rel="nofollow" href="http://en.wikipedia.org/wiki/TeX)">http://en.wikipedia.org/wiki/TeX)</a> render engine to display the text ( not implemented yet ).</p>
<dt><i>OtherFormat </i></p>
<dd>The number of text formats can be extended using setTextEngine. Formats &gt;= <code>QwtText::OtherFormat</code> are not used by Qwt.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtText::QwtText (const QString &amp;text = QString::null, <code>QwtText::TextFormat</code>textFormat = <code>AutoText</code>)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text content<br />
 <i>textFormat</i> Text format</dl>
<h2>Member Function Documentation</h2>
<h3>QBrush QwtText::backgroundBrush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Background brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBackgroundBrush()</code>, <code>borderPen()</code></dl>
<h3>QPen QwtText::borderPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Background pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderPen()</code>, <code>backgroundBrush()</code></dl>
<h3>double QwtText::borderRadius () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Radius for the corners of the border frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code>, <code>borderPen()</code>, <code>backgroundBrush()</code></dl>
<h3>void QwtText::draw (QPainter *painter, const QRectF &amp;rect) const</h3>
<p>Draw a text into a rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Rectangle</dl>
<h3>double QwtText::heightForWidth (doublewidth, const QFont &amp;defaultFont = QFont()) const</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font, used for the calculation if the text has no font<br />
 <i>width</i> Width</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dl>
<h3>bool QwtText::isEmpty () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>text()</code>.<code>isEmpty()</code></dl>
<h3>bool QwtText::isNull () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>text()</code>.<code>isNull()</code></dl>
<h3>int QwtText::renderFlags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Render flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderFlags()</code></dl>
<h3>void QwtText::setBackgroundBrush (const QBrush &amp;brush)</h3>
<p>Set the background brush </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Background brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>backgroundBrush()</code>, <code>setBorderPen()</code></dl>
<h3>void QwtText::setBorderPen (const QPen &amp;pen)</h3>
<p>Set the background pen </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Background pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderPen()</code>, <code>setBackgroundBrush()</code></dl>
<h3>void QwtText::setBorderRadius (doubleradius)</h3>
<p>Set the radius for the corners of the border frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>radius</i> Radius of a rounded corner</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderRadius()</code>, <code>setBorderPen()</code>, <code>setBackgroundBrush()</code></dl>
<h3>void QwtText::setColor (const QColor &amp;color)</h3>
<p>Set the pen color used for drawing the text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Color</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Setting the color might have no effect, when the text contains control sequences for setting colors.</dl>
<h3>void QwtText::setFont (const QFont &amp;font)</h3>
<p>Set the font. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Setting the font might have no effect, when the text contains control sequences for setting fonts.</dl>
<h3>void QwtText::setLayoutAttribute (<code>LayoutAttribute</code>attribute, boolon = true)</h3>
<p>Change a layout attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Layout attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testLayoutAttribute()</code></dl>
<h3>void QwtText::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Change a paint attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Used by <code>setFont()</code>, <code>setColor()</code>, <code>setBorderPen()</code> and <code>setBackgroundBrush()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dl>
<h3>void QwtText::setRenderFlags (intrenderFlags)</h3>
<p>Change the render flags. The default setting is Qt::AlignCenter </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>renderFlags</i> Bitwise OR of the flags used like in QPainter::drawText()</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderFlags()</code>, <code>QwtTextEngine::draw()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some renderFlags might have no effect, depending on the text format.</dl>
<h3>void QwtText::setText (const QString &amp;text, <code>QwtText::TextFormat</code>textFormat = <code>AutoText</code>)</h3>
<p>Assign a new text content </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text content<br />
 <i>textFormat</i> Text format</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>text()</code></dl>
<h3>void QwtText::setTextEngine (<code>QwtText::TextFormat</code>format, <code>QwtTextEngine</code> *engine) [static]</h3>
<p>Assign/Replace a text engine for a text format </p>
<p> With setTextEngine it is possible to extend Qwt with other types of text formats. </p>
<p> For <code>QwtText::PlainText</code> it is not allowed to assign a engine == NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> Text format<br />
 <i>engine</i> Text engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtMathMLTextEngine</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>Using <code>QwtText::AutoText</code> does nothing.</dl>
<h3>bool QwtText::testLayoutAttribute (<code>LayoutAttribute</code>attribute) const</h3>
<p>Test a layout attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Layout attribute</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLayoutAttribute()</code></dl>
<h3>bool QwtText::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p>Test a paint attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code></dl>
<h3>QString QwtText::text () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Text as QString.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setText()</code></dl>
<h3>const <code>QwtTextEngine</code> * QwtText::textEngine (const QString &amp;text, <code>QwtText::TextFormat</code>format = <code>AutoText</code>) [static]</h3>
<p>Find the text engine for a text format </p>
<p> In case of <code>QwtText::AutoText</code> the first text engine (beside <code>QwtPlainTextEngine</code>) is returned, where <code>QwtTextEngine::mightRender</code> returns true. If there is none <code>QwtPlainTextEngine</code> is returned. </p>
<p> If no text engine is registered for the format <code>QwtPlainTextEngine</code> is returnd. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text, needed in case of AutoText<br />
 <i>format</i> Text format</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Corresponding text engine</dl>
<h3>const <code>QwtTextEngine</code> * QwtText::textEngine (<code>QwtText::TextFormat</code>format) [static]</h3>
<p>Find the text engine for a text format. textEngine can be used to find out if a text format is supported. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> Text format</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The text engine, or NULL if no engine is available.</dl>
<h3>QSizeF QwtText::textSize (const QFont &amp;defaultFont = QFont()) const</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font, used for the calculation if the text has no font</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dl>
<p> Returns the size, that is needed to render text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font of the text</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Caluclated size</dl>
<h3>QColor QwtText::usedColor (const QColor &amp;defaultColor) const</h3>
<p>Return the color of the text, if it has one. Otherwise return defaultColor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultColor</i> Default color</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Color used for drawing the text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColor()</code>, <code>color()</code>, <code>PaintAttributes</code></dl>
<h3>QFont QwtText::usedFont (const QFont &amp;defaultFont) const</h3>
<p>Return the font of the text, if it has one. Otherwise return defaultFont. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Default font</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Font used for drawing the text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFont()</code>, <code>font()</code>, <code>PaintAttributes</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
