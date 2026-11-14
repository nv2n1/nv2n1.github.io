---
title: "qwtscaledraw(3)"
name: "qwtscaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscaledraw/"
description: "QwtScaleDraw –"
---

<p>QwtScaleDraw &#8211; </p>
<p> A class for drawing scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_draw.h&gt; </p>
<p> Inherits <code>QwtAbstractScaleDraw</code>. </p>
<p> Inherited by <code>QwtDateScaleDraw</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Alignment</code> { <code>BottomScale</code>, <code>TopScale</code>, <code>LeftScale</code>, <code>RightScale</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleDraw</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtScaleDraw</code> ()<br />
 <i>Destructor. </i><br />
 void <code>getBorderDistHint</code> (const QFont &amp;, int &amp;start, int &amp;end) const<br />
 <i>Determine the minimum border distance. </i><br />
 int <code>minLabelDist</code> (const QFont &amp;) const </p>
<p> int <code>minLength</code> (const QFont &amp;) const </p>
<p> virtual double <code>extent</code> (const QFont &amp;) const </p>
<p> void <code>move</code> (double x, double y) </p>
<p> void <code>move</code> (const QPointF &amp;)<br />
 <i>Move the position of the scale. </i><br />
 void <code>setLength</code> (double <code>length</code>) </p>
<p> <code>Alignment</code> <code>alignment</code> () const </p>
<p> void <code>setAlignment</code> (<code>Alignment</code>) </p>
<p> Qt::Orientation <code>orientation</code> () const </p>
<p> QPointF <code>pos</code> () const </p>
<p> double <code>length</code> () const </p>
<p> void <code>setLabelAlignment</code> (Qt::Alignment)<br />
 <i>Change the label flags. </i><br />
 Qt::Alignment <code>labelAlignment</code> () const </p>
<p> void <code>setLabelRotation</code> (double rotation) </p>
<p> double <code>labelRotation</code> () const </p>
<p> int <code>maxLabelHeight</code> (const QFont &amp;) const </p>
<p> int <code>maxLabelWidth</code> (const QFont &amp;) const </p>
<p> QPointF <code>labelPosition</code> (double val) const </p>
<p> QRectF <code>labelRect</code> (const QFont &amp;, double val) const </p>
<p> QSizeF <code>labelSize</code> (const QFont &amp;, double val) const </p>
<p> QRect <code>boundingLabelRect</code> (const QFont &amp;, double val) const<br />
 <i>Find the bounding rectangle for the label. </i></p>
<h3>Protected Member Functions</h3>
<p>QTransform <code>labelTransformation</code> (const QPointF &amp;, const QSizeF &amp;) const </p>
<p> virtual void <code>drawTick</code> (QPainter *, double val, double len) const </p>
<p> virtual void <code>drawBackbone</code> (QPainter *) const </p>
<p> virtual void <code>drawLabel</code> (QPainter *, double val) const </p>
<h2>Detailed Description</h2>
<p>A class for drawing scales. </p>
<p> <code>QwtScaleDraw</code> can be used to draw linear or logarithmic scales. A scale has a position, an alignment and a length, which can be specified . The labels can be rotated and aligned to the ticks using <code>setLabelRotation()</code> and <code>setLabelAlignment()</code>. </p>
<p> After a scale division has been specified as a <code>QwtScaleDiv</code> object using <code>QwtAbstractScaleDraw::setScaleDiv(const QwtScaleDiv &amp;s)</code>, the scale can be drawn with the <code>QwtAbstractScaleDraw::draw()</code> member.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtScaleDraw::Alignment</code></h3>
<p>Alignment of the scale draw </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignment()</code>, <code>alignment()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>BottomScale </i></p>
<dd>The scale is below.</p>
<dt><i>TopScale </i></p>
<dd>The scale is above.</p>
<dt><i>LeftScale </i></p>
<dd>The scale is left.</p>
<dt><i>RightScale </i></p>
<dd>The scale is right.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleDraw::QwtScaleDraw ()</h3>
<p>Constructor. The range of the scale is initialized to [0, 100], The position is at (0, 0) with a length of 100. The orientation is QwtAbstractScaleDraw::Bottom.</p>
<h2>Member Function Documentation</h2>
<h3><code>QwtScaleDraw::Alignment</code> QwtScaleDraw::alignment () const</h3>
<p>Return alignment of the scale </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignment()</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Alignment of the scale</dl>
<h3>QRect QwtScaleDraw::boundingLabelRect (const QFont &amp;font, doublevalue) const</h3>
<p>Find the bounding rectangle for the label. The coordinates of the rectangle are absolute ( calculated from <code>pos()</code> ). in direction of the tick. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for painting<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>labelRect()</code></dl>
<h3>void QwtScaleDraw::drawBackbone (QPainter *painter) const [protected], [virtual]</h3>
<p>Draws the baseline of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawLabel()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtScaleDraw::drawLabel (QPainter *painter, doublevalue) const [protected], [virtual]</h3>
<p>Draws the label for a major scale tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawBackbone()</code>, <code>boundingLabelRect()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtScaleDraw::drawTick (QPainter *painter, doublevalue, doublelen) const [protected], [virtual]</h3>
<p>Draw a tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value of the tick<br />
 <i>len</i> Length of the tick</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawBackbone()</code>, <code>drawLabel()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>double QwtScaleDraw::extent (const QFont &amp;font) const [virtual]</h3>
<p>Calculate the width/height that is needed for a vertical/horizontal scale. </p>
<p> The extent is calculated from the pen width of the backbone, the major tick length, the spacing and the maximum width/height of the labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for painting the labels</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Extent</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minLength()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtScaleDraw::getBorderDistHint (const QFont &amp;font, int &amp;start, int &amp;end) const</h3>
<p>Determine the minimum border distance. This member function returns the minimum space needed to draw the mark labels at the scale&#8217;s endpoints. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font<br />
 <i>start</i> Start border distance<br />
 <i>end</i> End border distance</dl>
<h3>Qt::Alignment QwtScaleDraw::labelAlignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the label flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelAlignment()</code>, <code>labelRotation()</code></dl>
<h3>QPointF QwtScaleDraw::labelPosition (doublevalue) const</h3>
<p>Find the position, where to paint a label </p>
<p> The position has a distance that depends on the length of the ticks in direction of the <code>alignment()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position, where to paint a label</dl>
<h3>QRectF QwtScaleDraw::labelRect (const QFont &amp;font, doublevalue) const</h3>
<p>Find the bounding rectangle for the label. The coordinates of the rectangle are relative to spacing + tick length from the backbone in direction of the tick. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for painting<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle that is needed to draw a label</dl>
<h3>double QwtScaleDraw::labelRotation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the label rotation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelRotation()</code>, <code>labelAlignment()</code></dl>
<h3>QSizeF QwtScaleDraw::labelSize (const QFont &amp;font, doublevalue) const</h3>
<p>Calculate the size that is needed to draw a label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Label font<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Size that is needed to draw a label</dl>
<h3>QTransform QwtScaleDraw::labelTransformation (const QPointF &amp;pos, const QSizeF &amp;size) const [protected]</h3>
<p>Calculate the transformation that is needed to paint a label depending on its alignment and rotation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position where to paint the label<br />
 <i>size</i> Size of the label</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Transformation matrix</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelAlignment()</code>, <code>setLabelRotation()</code></dl>
<h3>double QwtScaleDraw::length () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the length of the backbone</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLength()</code>, <code>pos()</code></dl>
<h3>int QwtScaleDraw::maxLabelHeight (const QFont &amp;font) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum height of a label</dl>
<h3>int QwtScaleDraw::maxLabelWidth (const QFont &amp;font) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum width of a label</dl>
<h3>int QwtScaleDraw::minLabelDist (const QFont &amp;font) const</h3>
<p>Determine the minimum distance between two labels, that is necessary that the texts don&#8217;t overlap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum width of a label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getBorderDistHint()</code></dl>
<h3>int QwtScaleDraw::minLength (const QFont &amp;font) const</h3>
<p>Calculate the minimum length that is needed to draw the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for painting the labels</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum length that is needed to draw the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>extent()</code></dl>
<h3>void QwtScaleDraw::move (doublex, doubley) [inline]</h3>
<p>Move the position of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X coordinate<br />
 <i>y</i> Y coordinate</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>move(const QPointF &amp;)</code></dl>
<h3>void QwtScaleDraw::move (const QPointF &amp;pos)</h3>
<p>Move the position of the scale. The meaning of the parameter pos depends on the alignment:</p>
<dl COMPACT>
<dt><code>QwtScaleDraw::LeftScale</code></p>
<dd>The origin is the topmost point of the backbone. The backbone is a vertical line. Scale marks and labels are drawn at the left of the backbone.</p>
<dt><code>QwtScaleDraw::RightScale</code></p>
<dd>The origin is the topmost point of the backbone. The backbone is a vertical line. Scale marks and labels are drawn at the right of the backbone.</p>
<dt><code>QwtScaleDraw::TopScale</code></p>
<dd>The origin is the leftmost point of the backbone. The backbone is a horizontal line. Scale marks and labels are drawn above the backbone.</p>
<dt><code>QwtScaleDraw::BottomScale</code></p>
<dd>The origin is the leftmost point of the backbone. The backbone is a horizontal line Scale marks and labels are drawn below the backbone.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Origin of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pos()</code>, <code>setLength()</code></dl>
<h3>Qt::Orientation QwtScaleDraw::orientation () const</h3>
<p>Return the orientation </p>
<p> TopScale, BottomScale are horizontal (Qt::Horizontal) scales, LeftScale, RightScale are vertical (Qt::Vertical) scales. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alignment()</code></dl>
<h3>QPointF QwtScaleDraw::pos () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Origin of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>move()</code>, <code>length()</code></dl>
<h3>void QwtScaleDraw::setAlignment (<code>Alignment</code>align)</h3>
<p>Set the alignment of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>align</i> Alignment of the scale</dl>
<p> The default alignment is <code>QwtScaleDraw::BottomScale</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alignment()</code></dl>
<h3>void QwtScaleDraw::setLabelAlignment (Qt::Alignmentalignment)</h3>
<p>Change the label flags. Labels are aligned to the point tick length + spacing away from the backbone. </p>
<p> The alignment is relative to the orientation of the label text. In case of an flags of 0 the label will be aligned depending on the orientation of the scale: </p>
<pre>QwtScaleDraw::TopScale: Qt::AlignHCenter | Qt::AlignTopQwtScaleDraw::BottomScale: Qt::AlignHCenter | Qt::AlignBottomQwtScaleDraw::LeftScale: Qt::AlignLeft | Qt::AlignVCenterQwtScaleDraw::RightScale: Qt::AlignRight | Qt::AlignVCenter</pre>
<p>Changing the alignment is often necessary for rotated labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alignment</i> Or&#8217;d Qt::AlignmentFlags see &lt;qnamespace.h&gt;</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelRotation()</code>, <code>labelRotation()</code>, <code>labelAlignment()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The various alignments might be confusing. The alignment of the label is not the alignment of the scale and is not the alignment of the flags ( QwtText::flags() ) returned from <code>QwtAbstractScaleDraw::label()</code>.</dl>
<h3>void QwtScaleDraw::setLabelRotation (doublerotation)</h3>
<p>Rotate all labels. </p>
<p> When changing the rotation, it might be necessary to adjust the label flags too. Finding a useful combination is often the result of try and error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rotation</i> Angle in degrees. When changing the label rotation, the label flags often needs to be adjusted too.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelAlignment()</code>, <code>labelRotation()</code>, <code>labelAlignment()</code>.</dl>
<h3>void QwtScaleDraw::setLength (doublelength)</h3>
<p>Set the length of the backbone. </p>
<p> The length doesn&#8217;t include the space needed for overlapping labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>length</i> Length of the backbone</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>move()</code>, <code>minLabelDist()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
