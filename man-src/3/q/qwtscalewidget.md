---
title: "qwtscalewidget(3)"
name: "qwtscalewidget"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscalewidget/"
description: "QwtScaleWidget –"
---

<p>QwtScaleWidget &#8211; </p>
<p> A Widget which contains a scale.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_widget.h&gt; </p>
<p> Inherits QWidget.</p>
<h3>Public Types</h3>
<p>enum <code>LayoutFlag</code> { <code>TitleInverted</code> = 1 }<br />
 <i>Layout flags of the title. </i><br />
 typedef QFlags&lt; <code>LayoutFlag</code> &gt; <code>LayoutFlags</code><br />
 <i>Layout flags of the title. </i></p>
<h3>Signals</h3>
<p>void <code>scaleDivChanged</code> ()<br />
 <i>Signal emitted, whenever the scale division changes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleWidget</code> (QWidget *parent=NULL)<br />
 <i>Create a scale with the position QwtScaleWidget::Left. </i><br />
 <code>QwtScaleWidget</code> (<code>QwtScaleDraw::Alignment</code>, QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtScaleWidget</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setTitle</code> (const QString &amp;<code>title</code>) </p>
<p> void <code>setTitle</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> <code>QwtText</code> <code>title</code> () const </p>
<p> void <code>setLayoutFlag</code> (<code>LayoutFlag</code>, bool on) </p>
<p> bool <code>testLayoutFlag</code> (<code>LayoutFlag</code>) const </p>
<p> void <code>setBorderDist</code> (int start, int end) </p>
<p> int <code>startBorderDist</code> () const </p>
<p> int <code>endBorderDist</code> () const </p>
<p> void <code>getBorderDistHint</code> (int &amp;start, int &amp;end) const<br />
 <i>Calculate a hint for the border distances. </i><br />
 void <code>getMinBorderDist</code> (int &amp;start, int &amp;end) const </p>
<p> void <code>setMinBorderDist</code> (int start, int end) </p>
<p> void <code>setMargin</code> (int)<br />
 <i>Specify the margin to the colorBar/base line. </i><br />
 int <code>margin</code> () const </p>
<p> void <code>setSpacing</code> (int td)<br />
 <i>Specify the distance between color bar, scale and title. </i><br />
 int <code>spacing</code> () const </p>
<p> void <code>setScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;sd)<br />
 <i>Assign a scale division. </i><br />
 void <code>setTransformation</code> (<code>QwtTransform</code> *) </p>
<p> void <code>setScaleDraw</code> (<code>QwtScaleDraw</code> *) </p>
<p> const <code>QwtScaleDraw</code> * <code>scaleDraw</code> () const </p>
<p> <code>QwtScaleDraw</code> * <code>scaleDraw</code> () </p>
<p> void <code>setLabelAlignment</code> (Qt::Alignment)<br />
 <i>Change the alignment for the labels. </i><br />
 void <code>setLabelRotation</code> (double rotation)<br />
 <i>Change the rotation for the labels. See </i><code>QwtScaleDraw::setLabelRotation()</code>.<br />
 void <code>setColorBarEnabled</code> (bool) </p>
<p> bool <code>isColorBarEnabled</code> () const </p>
<p> void <code>setColorBarWidth</code> (int) </p>
<p> int <code>colorBarWidth</code> () const </p>
<p> void <code>setColorMap</code> (const <code>QwtInterval</code> &amp;, <code>QwtColorMap</code> *) </p>
<p> <code>QwtInterval</code> <code>colorBarInterval</code> () const </p>
<p> const <code>QwtColorMap</code> * <code>colorMap</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> int <code>titleHeightForWidth</code> (int width) const<br />
 <i>Find the height of the title for a given width. </i><br />
 int <code>dimForLength</code> (int length, const QFont &amp;scaleFont) const<br />
 <i>Find the minimum dimension for a given length. dim is the height, length the width seen in direction of the title. </i><br />
 void <code>drawColorBar</code> (QPainter *painter, const QRectF &amp;) const </p>
<p> void <code>drawTitle</code> (QPainter *painter, <code>QwtScaleDraw::Alignment</code>, const QRectF &amp;rect) const </p>
<p> void <code>setAlignment</code> (<code>QwtScaleDraw::Alignment</code>) </p>
<p> <code>QwtScaleDraw::Alignment</code> <code>alignment</code> () const </p>
<p> QRectF <code>colorBarRect</code> (const QRectF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *)<br />
 <i>paintEvent </i><br />
 virtual void <code>resizeEvent</code> (QResizeEvent *) </p>
<p> void <code>draw</code> (QPainter *p) const<br />
 <i>draw the scale </i><br />
 void <code>scaleChange</code> ()<br />
 <i>Notify a change of the scale. </i><br />
 void <code>layoutScale</code> (bool update=true) </p>
<h2>Detailed Description</h2>
<p>A Widget which contains a scale. </p>
<p> This Widget can be used to decorate composite widgets with a scale.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtScaleWidget::LayoutFlag</code></h3>
<p>Layout flags of the title. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>TitleInverted </i></p>
<dd>The title of vertical scales is painted from top to bottom. Otherwise it is painted from bottom to top.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleWidget::QwtScaleWidget (QWidget *parent = NULL) [explicit]</h3>
<p>Create a scale with the position QwtScaleWidget::Left. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h3>QwtScaleWidget::QwtScaleWidget (<code>QwtScaleDraw::Alignment</code>align, QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>align</i> Alignment.<br />
 <i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtScaleDraw::Alignment</code> QwtScaleWidget::alignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>setPosition()</dl>
<h3><code>QwtInterval</code> QwtScaleWidget::colorBarInterval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value interval for the color bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorMap()</code>, <code>colorMap()</code></dl>
<h3>QRectF QwtScaleWidget::colorBarRect (const QRectF &amp;rect) const</h3>
<p>Calculate the the rectangle for the color bar </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle for all components of the scale</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle for the color bar</dl>
<h3>int QwtScaleWidget::colorBarWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the color bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorBarEnabled()</code>, <code>setColorBarEnabled()</code></dl>
<h3>const <code>QwtColorMap</code> * QwtScaleWidget::colorMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Color map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorMap()</code>, <code>colorBarInterval()</code></dl>
<h3>int QwtScaleWidget::dimForLength (intlength, const QFont &amp;scaleFont) const</h3>
<p>Find the minimum dimension for a given length. dim is the height, length the width seen in direction of the title. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>length</i> width for horizontal, height for vertical scales<br />
 <i>scaleFont</i> Font of the scale</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>height for horizontal, width for vertical scales</dl>
<h3>void QwtScaleWidget::drawColorBar (QPainter *painter, const QRectF &amp;rect) const</h3>
<p>Draw the color bar of the scale widget </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Bounding rectangle for the color bar</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorBarEnabled()</code></dl>
<h3>void QwtScaleWidget::drawTitle (QPainter *painter, <code>QwtScaleDraw::Alignment</code>align, const QRectF &amp;rect) const</h3>
<p>Rotate and paint a title according to its position into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>align</i> Alignment<br />
 <i>rect</i> Bounding rectangle</dl>
<h3>int QwtScaleWidget::endBorderDist () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>end border distance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderDist()</code></dl>
<h3>void QwtScaleWidget::getBorderDistHint (int &amp;start, int &amp;end) const</h3>
<p>Calculate a hint for the border distances. This member function calculates the distance of the scale&#8217;s endpoints from the widget borders which is required for the mark labels to fit into the widget. The maximum of this distance an the minimum border distance is returned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>start</i> Return parameter for the border width at the beginning of the scale<br />
 <i>end</i> Return parameter for the border width at the end of the scale</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>The minimum border distance depends on the font.</dl>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinBorderDist()</code>, <code>getMinBorderDist()</code>, <code>setBorderDist()</code></dl>
<h3>void QwtScaleWidget::getMinBorderDist (int &amp;start, int &amp;end) const</h3>
<p>Get the minimum value for the distances of the scale&#8217;s endpoints from the widget borders. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>start</i> Return parameter for the border width at the beginning of the scale<br />
 <i>end</i> Return parameter for the border width at the end of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinBorderDist()</code>, <code>getBorderDistHint()</code></dl>
<h3>bool QwtScaleWidget::isColorBarEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true, when the color bar is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorBarEnabled()</code>, <code>setColorBarWidth()</code></dl>
<h3>void QwtScaleWidget::layoutScale (boolupdate_geometry = true) [protected]</h3>
<p>Recalculate the scale&#8217;s geometry and layout based on the current geometry and fonts. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>update_geometry</i> Notify the layout system and call update to redraw the scale</dl>
<h3>int QwtScaleWidget::margin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code></dl>
<h3>QSize QwtScaleWidget::minimumSizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>a minimum size hint</dl>
<h3>void QwtScaleWidget::resizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Event handler for resize events </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<h3>void QwtScaleWidget::scaleChange () [protected]</h3>
<p>Notify a change of the scale. This virtual function can be overloaded by derived classes. The default implementation updates the geometry and repaints the widget.</p>
<h3>const <code>QwtScaleDraw</code> * QwtScaleWidget::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>scaleDraw of this scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code>, QwtScaleDraw::setScaleDraw()</dl>
<h3><code>QwtScaleDraw</code> * QwtScaleWidget::scaleDraw ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>scaleDraw of this scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtScaleDraw::setScaleDraw()</dl>
<h3>void QwtScaleWidget::setAlignment (<code>QwtScaleDraw::Alignment</code>alignment)</h3>
<p>Change the alignment </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alignment</i> New alignment</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alignment()</code></dl>
<h3>void QwtScaleWidget::setBorderDist (intdist1, intdist2)</h3>
<p>Specify distances of the scale&#8217;s endpoints from the widget&#8217;s borders. The actual borders will never be less than minimum border distance. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dist1</i> Left or top Distance<br />
 <i>dist2</i> Right or bottom distance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>borderDist()</dl>
<h3>void QwtScaleWidget::setColorBarEnabled (boolon)</h3>
<p>En/disable a color bar associated to the scale </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isColorBarEnabled()</code>, <code>setColorBarWidth()</code></dl>
<h3>void QwtScaleWidget::setColorBarWidth (intwidth)</h3>
<p>Set the width of the color bar </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>colorBarWidth()</code>, <code>setColorBarEnabled()</code></dl>
<h3>void QwtScaleWidget::setColorMap (const <code>QwtInterval</code> &amp;interval, <code>QwtColorMap</code> *colorMap)</h3>
<p>Set the color map and value interval, that are used for displaying the color bar. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Value interval<br />
 <i>colorMap</i> Color map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>colorMap()</code>, <code>colorBarInterval()</code></dl>
<h3>void QwtScaleWidget::setLabelAlignment (Qt::Alignmentalignment)</h3>
<p>Change the alignment for the labels. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDraw::setLabelAlignment()</code>, <code>setLabelRotation()</code></dl>
<h3>void QwtScaleWidget::setLabelRotation (doublerotation)</h3>
<p>Change the rotation for the labels. See <code>QwtScaleDraw::setLabelRotation()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rotation</i> Rotation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDraw::setLabelRotation()</code>, setLabelFlags()</dl>
<h3>void QwtScaleWidget::setLayoutFlag (<code>LayoutFlag</code>flag, boolon)</h3>
<p>Toggle an layout flag </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Layout flag<br />
 <i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testLayoutFlag()</code>, <code>LayoutFlag</code></dl>
<h3>void QwtScaleWidget::setMargin (intmargin)</h3>
<p>Specify the margin to the colorBar/base line. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> Margin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>margin()</code></dl>
<h3>void QwtScaleWidget::setMinBorderDist (intstart, intend)</h3>
<p>Set a minimum value for the distances of the scale&#8217;s endpoints from the widget borders. This is useful to avoid that the scales are &#8216;jumping&#8217;, when the tick labels or their positions change often. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>start</i> Minimum for the start border<br />
 <i>end</i> Minimum for the end border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getMinBorderDist()</code>, <code>getBorderDistHint()</code></dl>
<h3>void QwtScaleWidget::setScaleDiv (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Assign a scale division. The scale division determines where to set the tick marks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale Division</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>For more information about scale divisions, see <code>QwtScaleDiv</code>.</dl>
<h3>void QwtScaleWidget::setScaleDraw (<code>QwtScaleDraw</code> *scaleDraw)</h3>
<p>Set a scale draw </p>
<p> scaleDraw has to be created with new and will be deleted in <code>~QwtScaleWidget()</code> or the next call of <code>setScaleDraw()</code>. scaleDraw will be initialized with the attributes of the previous scaleDraw object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDraw</i> ScaleDraw object</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleDraw()</code></dl>
<h3>void QwtScaleWidget::setSpacing (intspacing)</h3>
<p>Specify the distance between color bar, scale and title. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code></dl>
<h3>void QwtScaleWidget::setTitle (const QString &amp;title)</h3>
<p>Give title new text contents </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> New title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code>, <code>setTitle(const QwtText &amp;)</code>;</dl>
<h3>void QwtScaleWidget::setTitle (const <code>QwtText</code> &amp;title)</h3>
<p>Give title new text contents </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> New title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>title()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The title flags are interpreted in direction of the label, AlignTop, AlignBottom can&#8217;t be set as the title will always be aligned to the scale.</dl>
<h3>void QwtScaleWidget::setTransformation (<code>QwtTransform</code> *transformation)</h3>
<p>Set the transformation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>transformation</i> Transformation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtAbstractScaleDraw::scaleDraw(), <code>QwtScaleMap</code></dl>
<h3>QSize QwtScaleWidget::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>a size hint</dl>
<h3>int QwtScaleWidget::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>distance between scale and title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargin()</code></dl>
<h3>int QwtScaleWidget::startBorderDist () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>start border distance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderDist()</code></dl>
<h3>bool QwtScaleWidget::testLayoutFlag (<code>LayoutFlag</code>flag) const</h3>
<p>Test a layout flag </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Layout flag</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLayoutFlag()</code>, <code>LayoutFlag</code></dl>
<h3><code>QwtText</code> QwtScaleWidget::title () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTitle()</code></dl>
<h3>int QwtScaleWidget::titleHeightForWidth (intwidth) const</h3>
<p>Find the height of the title for a given width. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>height Height</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
