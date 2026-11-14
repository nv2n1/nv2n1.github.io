---
title: "qwttextlabel(3)"
name: "qwttextlabel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwttextlabel/"
description: "QwtTextLabel –"
---

<p>QwtTextLabel &#8211; </p>
<p> A Widget which displays a <code>QwtText</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_text_label.h&gt; </p>
<p> Inherits QFrame. </p>
<p> Inherited by <code>QwtLegendLabel</code>.</p>
<h3>Public Slots</h3>
<p>void <code>setText</code> (const QString &amp;, <code>QwtText::TextFormat</code> textFormat=<code>QwtText::AutoText</code>) </p>
<p> virtual void <code>setText</code> (const <code>QwtText</code> &amp;) </p>
<p> void <code>clear</code> ()<br />
 <i>Clear the text and all </i><code>QwtText</code> attributes.</p>
<h3>Public Member Functions</h3>
<p><code>QwtTextLabel</code> (QWidget *parent=NULL) </p>
<p> <code>QwtTextLabel</code> (const <code>QwtText</code> &amp;, QWidget *parent=NULL) </p>
<p> virtual <code>~QwtTextLabel</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setPlainText</code> (const QString &amp;) </p>
<p> QString <code>plainText</code> () const </p>
<p> const <code>QwtText</code> &amp; <code>text</code> () const<br />
 <i>Return the text. </i><br />
 int <code>indent</code> () const<br />
 <i>Return label&#8217;s text indent in pixels. </i><br />
 void <code>setIndent</code> (int) </p>
<p> int <code>margin</code> () const<br />
 <i>Return label&#8217;s text indent in pixels. </i><br />
 void <code>setMargin</code> (int) </p>
<p> virtual QSize <code>sizeHint</code> () const<br />
 <i>Return label&#8217;s margin in pixels. </i><br />
 virtual QSize <code>minimumSizeHint</code> () const<br />
 <i>Return a minimum size hint. </i><br />
 virtual int <code>heightForWidth</code> (int) const </p>
<p> QRect <code>textRect</code> () const </p>
<p> virtual void <code>drawText</code> (QPainter *, const QRectF &amp;)<br />
 <i>Redraw the text. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *e) </p>
<p> virtual void <code>drawContents</code> (QPainter *)<br />
 <i>Redraw the text and focus indicator. </i></p>
<h2>Detailed Description</h2>
<p>A Widget which displays a <code>QwtText</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtTextLabel::QwtTextLabel (QWidget *parent = NULL) [explicit]</h3>
<p>Constructs an empty label. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h3>QwtTextLabel::QwtTextLabel (const <code>QwtText</code> &amp;text, QWidget *parent = NULL) [explicit]</h3>
<p>Constructs a label that displays the text, text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget<br />
 <i>text</i> Text</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtTextLabel::heightForWidth (intwidth) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Preferred height for this widget, given the width.</dl>
<h3>void QwtTextLabel::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Qt paint event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<p> Reimplemented in <code>QwtLegendLabel</code>.</p>
<h3>QString QwtTextLabel::plainText () const</h3>
<p>Interface for the designer plugin </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Text as plain text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPlainText()</code>, <code>text()</code></dl>
<h3>void QwtTextLabel::setIndent (intindent)</h3>
<p>Set label&#8217;s text indent in pixels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>indent</i> Indentation in pixels</dl>
<h3>void QwtTextLabel::setMargin (intmargin)</h3>
<p>Set label&#8217;s margin in pixels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin in pixels</dl>
<h3>void QwtTextLabel::setPlainText (const QString &amp;text)</h3>
<p>Interface for the designer plugin &#8211; does the same as <code>setText()</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>plainText()</code></dl>
<h3>void QwtTextLabel::setText (const QString &amp;text, <code>QwtText::TextFormat</code>textFormat = <code>QwtText::AutoText</code>) [slot]</h3>
<p>Change the label&#8217;s text, keeping all other <code>QwtText</code> attributes </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> New text<br />
 <i>textFormat</i> Format of text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtText</code></dl>
<h3>void QwtTextLabel::setText (const <code>QwtText</code> &amp;text) [virtual], [slot]</h3>
<p>Change the label&#8217;s text </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> New text</dl>
<p> Reimplemented in <code>QwtLegendLabel</code>.</p>
<h3>QRect QwtTextLabel::textRect () const</h3>
<p>Calculate geometry for the text in widget coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the text</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
