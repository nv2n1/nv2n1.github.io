---
title: "qwtplottextlabel(3)"
name: "qwtplottextlabel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplottextlabel/"
description: "QwtPlotTextLabel –"
---

<p>QwtPlotTextLabel &#8211; </p>
<p> A plot item, which displays a text label.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_textlabel.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotTextLabel</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotTextLabel</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setText</code> (const <code>QwtText</code> &amp;) </p>
<p> <code>QwtText</code> <code>text</code> () const </p>
<p> void <code>setMargin</code> (int <code>margin</code>) </p>
<p> int <code>margin</code> () const </p>
<p> virtual QRectF <code>textRect</code> (const QRectF &amp;, const QSizeF &amp;) const<br />
 <i>Align the text label. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>draw</code> (QPainter *, const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QRectF &amp;) const </p>
<p> void <code>invalidateCache</code> ()<br />
 <i>Invalidate all internal cache. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A plot item, which displays a text label. </p>
<p> <code>QwtPlotTextLabel</code> displays a text label aligned to the plot canvas. </p>
<p> In opposite to <code>QwtPlotMarker</code> the position of the label is unrelated to plot coordinates. </p>
<p> As drawing a text is an expensive operation the label is cached in a pixmap to speed up replots. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>The following code shows how to add a title.</dl>
<pre> QwtText title( &quot;Plot Title&quot; );
 title.setRenderFlags( Qt::AlignHCenter | Qt::AlignTop );
 QFont font;
 font.setBold( true );
 title.setFont( font );
 QwtPlotTextLabel *titleItem = new QwtPlotTextLabel();
 titleItem-&gt;setText( title );
 titleItem-&gt;attach( this );</pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotMarker</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotTextLabel::QwtPlotTextLabel ()</h3>
<p>Constructor. Initializes an text label with an empty text </p>
<p> Sets the following item attributes: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: true</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> The z value is initialized by 150 </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setItemAttribute()</code>, <code>QwtPlotItem::setZ()</code></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotTextLabel::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [protected], [virtual]</h3>
<p>Draw the text label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x Scale Map<br />
 <i>yMap</i> y Scale Map<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>textRect()</code></dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>int QwtPlotTextLabel::margin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Margin added to the contentsMargins() of the canvas</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code></dl>
<h3>int QwtPlotTextLabel::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotTextLabel</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotTextLabel::setMargin (intmargin)</h3>
<p>Set the margin </p>
<p> The margin is the distance between the contentsRect() of the plot canvas and the rectangle where the label can be displayed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>margin()</code>, <code>textRect()</code></dl>
<h3>void QwtPlotTextLabel::setText (const <code>QwtText</code> &amp;text)</h3>
<p>Set the text </p>
<p> The label will be aligned to the plot canvas according to the alignment flags of text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text to be displayed</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>text()</code>, <code>QwtText::renderFlags()</code></dl>
<h3><code>QwtText</code> QwtPlotTextLabel::text () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Text to be displayed</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setText()</code></dl>
<h3>QRectF QwtPlotTextLabel::textRect (const QRectF &amp;rect, const QSizeF &amp;textSize) const [virtual]</h3>
<p>Align the text label. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Canvas rectangle with margins subtracted<br />
 <i>textSize</i> Size required to draw the text</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A rectangle aligned according the the alignment flags of the text.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code>, <code>QwtText::renderFlags()</code>, <code>QwtText::textSize()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
