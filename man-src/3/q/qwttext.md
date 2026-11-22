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
<p>enum <code>TextFormat</code> { <code>AutoText</code> = 0, <code>PlainText</code>, <code>RichText</code>, <code>MathMLText</code>, <code>TeXText</code>, <code>OtherFormat</code> = 100 }<br/>
 <i>Text format. </i><br/>
 enum <code>PaintAttribute</code> { <code>PaintUsingTextFont</code> = 0x01, <code>PaintUsingTextColor</code> = 0x02, <code>PaintBackground</code> = 0x04 }<br/>
 <i>Paint Attributes. </i><br/>
 enum <code>LayoutAttribute</code> { <code>MinimumLayout</code> = 0x01 }<br/>
 <i>Layout Attributes The layout attributes affects some aspects of the layout of the text. </i><br/>
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br/>
 <i>Paint attributes. </i><br/>
 typedef QFlags&lt; <code>LayoutAttribute</code> &gt; <code>LayoutAttributes</code><br/>
 <i>Layout attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtText</code> (const QString &amp;=QString::null, <code>TextFormat</code> textFormat=<code>AutoText</code>) </p>
<p> <code>QwtText</code> (const <code>QwtText</code> &amp;)<br/>
 <i>Copy constructor. </i><br/>
 <code>~QwtText</code> ()<br/>
 <i>Destructor. </i><br/>
 <code>QwtText</code> &amp; <code>operator=</code> (const <code>QwtText</code> &amp;)<br/>
 <i>Assignment operator. </i><br/>
 bool <code>operator==</code> (const <code>QwtText</code> &amp;) const<br/>
 <i>Relational operator. </i><br/>
 bool <code>operator!=</code> (const <code>QwtText</code> &amp;) const<br/>
 <i>Relational operator. </i><br/>
 void <code>setText</code> (const QString &amp;, <code>QwtText::TextFormat</code> textFormat=<code>AutoText</code>) </p>
<p> QString <code>text</code> () const </p>
<p> bool <code>isNull</code> () const </p>
<p> bool <code>isEmpty</code> () const </p>
<p> void <code>setFont</code> (const QFont &amp;) </p>
<p> QFont <code>font</code> () const<br/>
 <i>Return the font. </i><br/>
 QFont <code>usedFont</code> (const QFont &amp;) const </p>
<p> void <code>setRenderFlags</code> (int flags)<br/>
 <i>Change the render flags. </i><br/>
 int <code>renderFlags</code> () const </p>
<p> void <code>setColor</code> (const QColor &amp;) </p>
<p> QColor <code>color</code> () const<br/>
 <i>Return the pen color, used for painting the text. </i><br/>
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
<p> static const <code>QwtTextEngine</code> * <code>textEngine</code> (<code>QwtText::TextFormat</code>)<br/>
 <i>Find the text engine for a text format. </i><br/>
 static void <code>setTextEngine</code> (<code>QwtText::TextFormat</code>, <code>QwtTextEngine</code> *) </p>
<h2>Detailed Description</h2>
<p>A class representing a text. </p>
<p> A <code>QwtText</code> is a text including a set of attributes how to render it. </p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>Format </dd>
<p>&nbsp;<wbr>A text might include control sequences&nbsp;<wbr>(f.e tags)&nbsp;<wbr>describing how to render it. Each format&nbsp;<wbr>(f.e MathML, TeX, Qt Rich Text)&nbsp;<wbr>has its own set of control sequences, that can be handles by a special&nbsp;<wbr><code>QwtTextEngine</code>&nbsp;<wbr>for this format.</p>
<dt>&bull;</dt>
<dd>Background </dd>
<p>&nbsp;<wbr>A text might have a background, defined by a QPen and QBrush to improve its visibility. The corners of the background might be rounded.</p>
<dt>&bull;</dt>
<dd>Font </dd>
<p>&nbsp;<wbr>A text might have an individual font.</p>
<dt>&bull;</dt>
<dd>Color </dd>
<p>&nbsp;<wbr>A text might have an individual color.</p>
<dt>&bull;</dt>
<dd>Render Flags </dd>
<p>&nbsp;<wbr>Flags from Qt::AlignmentFlag and Qt::TextFlag used like in QPainter::drawText().</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTextEngine</code>, <code>QwtTextLabel</code></dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtText::LayoutAttribute</code></h3>
<p>Layout Attributes The layout attributes affects some aspects of the layout of the text. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>MinimumLayout </i></dt>
<dd>Layout the text without its margins. This mode is useful if a text needs to be aligned accurately, like the tick labels of a scale. If <code>QwtTextEngine::textMargins</code> is not implemented for the format of the text, MinimumLayout has no effect.</dd></dl>
<h3>enum <code>QwtText::PaintAttribute</code></h3>
<p>Paint Attributes. Font and color and background are optional attributes of a <code>QwtText</code>. The paint attributes hold the information, if they are set. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>PaintUsingTextFont </i></dt>
<dd>The text has an individual font.</dd>
<dt><i>PaintUsingTextColor </i></dt>
<dd>The text has an individual color.</dd>
<dt><i>PaintBackground </i></dt>
<dd>The text has an individual background.</dd></dl>
<h3>enum <code>QwtText::TextFormat</code></h3>
<p>Text format. The text format defines the <code>QwtTextEngine</code>, that is used to render the text. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTextEngine</code>, <code>setTextEngine()</code></dd></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AutoText </i></dt>
<dd>The text format is determined using <code>QwtTextEngine::mightRender()</code> for all available text engines in increasing order &gt; PlainText. If none of the text engines can render the text is rendered like <code>QwtText::PlainText</code>.</dd>
<dt><i>PlainText </i></dt>
<dd>Draw the text as it is, using a <code>QwtPlainTextEngine</code>.</dd>
<dt><i>RichText </i></dt>
<dd>Use the Scribe framework (Qt Rich Text) to render the text.</dd>
<dt><i>MathMLText </i></dt>
<dd></dd></dl>
<pre> Use a MathML (<a rel="nofollow" href="http://en.wikipedia.org/wiki/MathML)">http://en.wikipedia.org/wiki/MathML)</a> render engine
 to display the text. The Qwt MathML extension offers such an engine
 based on the MathML renderer of the Qt solutions package. 
 To enable MathML support the following code needs to be added to the
 application:</pre>
<p>&nbsp;<wbr> </p>
<pre>QwtText::setTextEngine(QwtText::MathMLText, new QwtMathMLTextEngine()); </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>TeXText </i></dt>
<dd>Use a TeX (<a rel="nofollow" href="http://en.wikipedia.org/wiki/TeX)">http://en.wikipedia.org/wiki/TeX)</a> render engine to display the text ( not implemented yet ).</dd>
<dt><i>OtherFormat </i></dt>
<dd>The number of text formats can be extended using setTextEngine. Formats &gt;= <code>QwtText::OtherFormat</code> are not used by Qwt.</dd></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtText::QwtText (const QString &amp;text = QString::null, <code>QwtText::TextFormat</code>textFormat = <code>AutoText</code>)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text content<br/>
 <i>textFormat</i> Text format</dd></dl>
<h2>Member Function Documentation</h2>
<h3>QBrush QwtText::backgroundBrush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Background brush</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBackgroundBrush()</code>, <code>borderPen()</code></dd></dl>
<h3>QPen QwtText::borderPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Background pen</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderPen()</code>, <code>backgroundBrush()</code></dd></dl>
<h3>double QwtText::borderRadius () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Radius for the corners of the border frame</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code>, <code>borderPen()</code>, <code>backgroundBrush()</code></dd></dl>
<h3>void QwtText::draw (QPainter *painter, const QRectF &amp;rect) const</h3>
<p>Draw a text into a rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br/>
 <i>rect</i> Rectangle</dd></dl>
<h3>double QwtText::heightForWidth (doublewidth, const QFont &amp;defaultFont = QFont()) const</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font, used for the calculation if the text has no font<br/>
 <i>width</i> Width</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dd></dl>
<h3>bool QwtText::isEmpty () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>text()</code>.<code>isEmpty()</code></dd></dl>
<h3>bool QwtText::isNull () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>text()</code>.<code>isNull()</code></dd></dl>
<h3>int QwtText::renderFlags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Render flags</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderFlags()</code></dd></dl>
<h3>void QwtText::setBackgroundBrush (const QBrush &amp;brush)</h3>
<p>Set the background brush </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Background brush</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>backgroundBrush()</code>, <code>setBorderPen()</code></dd></dl>
<h3>void QwtText::setBorderPen (const QPen &amp;pen)</h3>
<p>Set the background pen </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Background pen</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderPen()</code>, <code>setBackgroundBrush()</code></dd></dl>
<h3>void QwtText::setBorderRadius (doubleradius)</h3>
<p>Set the radius for the corners of the border frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>radius</i> Radius of a rounded corner</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderRadius()</code>, <code>setBorderPen()</code>, <code>setBackgroundBrush()</code></dd></dl>
<h3>void QwtText::setColor (const QColor &amp;color)</h3>
<p>Set the pen color used for drawing the text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Color</dd></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Setting the color might have no effect, when the text contains control sequences for setting colors.</dd></dl>
<h3>void QwtText::setFont (const QFont &amp;font)</h3>
<p>Set the font. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font</dd></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Setting the font might have no effect, when the text contains control sequences for setting fonts.</dd></dl>
<h3>void QwtText::setLayoutAttribute (<code>LayoutAttribute</code>attribute, boolon = true)</h3>
<p>Change a layout attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Layout attribute<br/>
 <i>on</i> On/Off</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testLayoutAttribute()</code></dd></dl>
<h3>void QwtText::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Change a paint attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br/>
 <i>on</i> On/Off</dd></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Used by <code>setFont()</code>, <code>setColor()</code>, <code>setBorderPen()</code> and <code>setBackgroundBrush()</code></dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dd></dl>
<h3>void QwtText::setRenderFlags (intrenderFlags)</h3>
<p>Change the render flags. The default setting is Qt::AlignCenter </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>renderFlags</i> Bitwise OR of the flags used like in QPainter::drawText()</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderFlags()</code>, <code>QwtTextEngine::draw()</code></dd></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some renderFlags might have no effect, depending on the text format.</dd></dl>
<h3>void QwtText::setText (const QString &amp;text, <code>QwtText::TextFormat</code>textFormat = <code>AutoText</code>)</h3>
<p>Assign a new text content </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text content<br/>
 <i>textFormat</i> Text format</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>text()</code></dd></dl>
<h3>void QwtText::setTextEngine (<code>QwtText::TextFormat</code>format, <code>QwtTextEngine</code> *engine) [static]</h3>
<p>Assign/Replace a text engine for a text format </p>
<p> With setTextEngine it is possible to extend Qwt with other types of text formats. </p>
<p> For <code>QwtText::PlainText</code> it is not allowed to assign a engine == NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> Text format<br/>
 <i>engine</i> Text engine</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtMathMLTextEngine</code></dd></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>Using <code>QwtText::AutoText</code> does nothing.</dd></dl>
<h3>bool QwtText::testLayoutAttribute (<code>LayoutAttribute</code>attribute) const</h3>
<p>Test a layout attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Layout attribute</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if attribute is enabled</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLayoutAttribute()</code></dd></dl>
<h3>bool QwtText::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p>Test a paint attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if attribute is enabled</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code></dd></dl>
<h3>QString QwtText::text () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Text as QString.</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setText()</code></dd></dl>
<h3>const <code>QwtTextEngine</code> * QwtText::textEngine (const QString &amp;text, <code>QwtText::TextFormat</code>format = <code>AutoText</code>) [static]</h3>
<p>Find the text engine for a text format </p>
<p> In case of <code>QwtText::AutoText</code> the first text engine (beside <code>QwtPlainTextEngine</code>) is returned, where <code>QwtTextEngine::mightRender</code> returns true. If there is none <code>QwtPlainTextEngine</code> is returned. </p>
<p> If no text engine is registered for the format <code>QwtPlainTextEngine</code> is returnd. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text, needed in case of AutoText<br/>
 <i>format</i> Text format</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Corresponding text engine</dd></dl>
<h3>const <code>QwtTextEngine</code> * QwtText::textEngine (<code>QwtText::TextFormat</code>format) [static]</h3>
<p>Find the text engine for a text format. textEngine can be used to find out if a text format is supported. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> Text format</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The text engine, or NULL if no engine is available.</dd></dl>
<h3>QSizeF QwtText::textSize (const QFont &amp;defaultFont = QFont()) const</h3>
<p>Find the height for a given width </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font, used for the calculation if the text has no font</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated height</dd></dl>
<p> Returns the size, that is needed to render text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Font of the text</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Caluclated size</dd></dl>
<h3>QColor QwtText::usedColor (const QColor &amp;defaultColor) const</h3>
<p>Return the color of the text, if it has one. Otherwise return defaultColor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultColor</i> Default color</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Color used for drawing the text</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColor()</code>, <code>color()</code>, <code>PaintAttributes</code></dd></dl>
<h3>QFont QwtText::usedFont (const QFont &amp;defaultFont) const</h3>
<p>Return the font of the text, if it has one. Otherwise return defaultFont. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>defaultFont</i> Default font</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Font used for drawing the text</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFont()</code>, <code>font()</code>, <code>PaintAttributes</code></dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
