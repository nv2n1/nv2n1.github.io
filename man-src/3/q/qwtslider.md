---
title: "qwtslider(3)"
name: "qwtslider"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtslider/"
description: "QwtSlider –"
---

<p>QwtSlider &#8211; </p>
<p> The Slider Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_slider.h&gt; </p>
<p> Inherits <code>QwtAbstractSlider</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ScalePosition</code> { <code>NoScale</code>, <code>LeadingScale</code>, <code>TrailingScale</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtSlider</code> (QWidget *parent=NULL) </p>
<p> <code>QwtSlider</code> (Qt::Orientation, QWidget *parent=NULL) </p>
<p> virtual <code>~QwtSlider</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setOrientation</code> (Qt::Orientation)<br />
 <i>Set the orientation. </i><br />
 Qt::Orientation <code>orientation</code> () const </p>
<p> void <code>setScalePosition</code> (<code>ScalePosition</code>)<br />
 <i>Change the position of the scale. </i><br />
 <code>ScalePosition</code> <code>scalePosition</code> () const </p>
<p> void <code>setTrough</code> (bool) </p>
<p> bool <code>hasTrough</code> () const </p>
<p> void <code>setGroove</code> (bool) </p>
<p> bool <code>hasGroove</code> () const </p>
<p> void <code>setHandleSize</code> (const QSize &amp;)<br />
 <i>Set the slider&#8217;s handle size. </i><br />
 QSize <code>handleSize</code> () const </p>
<p> void <code>setBorderWidth</code> (int bw)<br />
 <i>Change the slider&#8217;s border width. </i><br />
 int <code>borderWidth</code> () const </p>
<p> void <code>setSpacing</code> (int)<br />
 <i>Change the spacing between trough and scale. </i><br />
 int <code>spacing</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> void <code>setScaleDraw</code> (<code>QwtScaleDraw</code> *)<br />
 <i>Set a scale draw. </i><br />
 const <code>QwtScaleDraw</code> * <code>scaleDraw</code> () const </p>
<p> void <code>setUpdateInterval</code> (int)<br />
 <i>Specify the update interval for automatic scrolling. </i><br />
 int <code>updateInterval</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual double <code>scrolledTo</code> (const QPoint &amp;) const<br />
 <i>Determine the value for a new position of the slider handle. </i><br />
 virtual bool <code>isScrollPosition</code> (const QPoint &amp;) const<br />
 <i>Determine what to do when the user presses a mouse button. </i><br />
 virtual void <code>drawSlider</code> (QPainter *, const QRect &amp;) const </p>
<p> virtual void <code>drawHandle</code> (QPainter *, const QRect &amp;, int pos) const </p>
<p> virtual void <code>mousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>mouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>resizeEvent</code> (QResizeEvent *) </p>
<p> virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>changeEvent</code> (QEvent *) </p>
<p> virtual void <code>timerEvent</code> (QTimerEvent *) </p>
<p> virtual void <code>scaleChange</code> ()<br />
 <i>Notify changed scale. </i><br />
 QRect <code>sliderRect</code> () const </p>
<p> QRect <code>handleRect</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>The Slider Widget. </p>
<p> <code>QwtSlider</code> is a slider widget which operates on an interval of type double. Its position is related to a scale showing the current value. </p>
<p> The slider can be customized by having a through, a groove &#8211; or both. </p>
<p>&nbsp;<wbr></p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtSlider::ScalePosition</code></h3>
<p>Position of the scale </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtSlider()</code>, <code>setScalePosition()</code>, <code>setOrientation()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoScale </i></p>
<dd>The slider has no scale.</p>
<dt><i>LeadingScale </i></p>
<dd>The scale is right of a vertical or below a horizontal slider.</p>
<dt><i>TrailingScale </i></p>
<dd>The scale is left of a vertical or above a horizontal slider.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSlider::QwtSlider (QWidget *parent = NULL) [explicit]</h3>
<p>Construct vertical slider in QwtSlider::Trough style with a scale to the left. </p>
<p> The scale is initialized to [0.0, 100.0] and the value set to 0.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code>, <code>setScalePosition()</code>, setBackgroundStyle()</dl>
<h3>QwtSlider::QwtSlider (Qt::Orientationorientation, QWidget *parent = NULL) [explicit]</h3>
<p>Construct a slider in QwtSlider::Trough style </p>
<p> When orientation is Qt::Vertical the scale will be aligned to the left &#8211; otherwise at the the top of the slider. </p>
<p> The scale is initialized to [0.0, 100.0] and the value set to 0.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget<br />
 <i>orientation</i> Orientation of the slider.</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtSlider::borderWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the border width.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderWidth()</code></dl>
<h3>void QwtSlider::changeEvent (QEvent *event) [protected], [virtual]</h3>
<p>Handles QEvent::StyleChange and QEvent::FontChange events </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Change event</dl>
<h3>void QwtSlider::drawHandle (QPainter *painter, const QRect &amp;handleRect, intpos) const [protected], [virtual]</h3>
<p>Draw the thumb at a position </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>handleRect</i> Bounding rectangle of the handle<br />
 <i>pos</i> Position of the handle marker in widget coordinates</dl>
<h3>void QwtSlider::drawSlider (QPainter *painter, const QRect &amp;sliderRect) const [protected], [virtual]</h3>
<p>Draw the slider into the specified rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>sliderRect</i> Bounding rectangle of the slider</dl>
<h3>QRect QwtSlider::handleRect () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the slider handle</dl>
<h3>QSize QwtSlider::handleSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the handle.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setHandleSize()</code></dl>
<h3>bool QwtSlider::hasGroove () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the groove is visisble</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setGroove()</code>, <code>hasTrough()</code></dl>
<h3>bool QwtSlider::hasTrough () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the trough is visisble</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTrough()</code>, <code>hasGroove()</code></dl>
<h3>bool QwtSlider::isScrollPosition (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine what to do when the user presses a mouse button. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>True,when</i> <code>handleRect()</code> contains pos</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scrolledTo()</code></dl>
<p> Implements <code>QwtAbstractSlider</code>.</p>
<h3>QSize QwtSlider::minimumSizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>sizeHint()</code></dl>
<h3>void QwtSlider::mousePressEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse press event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<p> Reimplemented from <code>QwtAbstractSlider</code>.</p>
<h3>void QwtSlider::mouseReleaseEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse release event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<p> Reimplemented from <code>QwtAbstractSlider</code>.</p>
<h3>Qt::Orientation QwtSlider::orientation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code></dl>
<h3>void QwtSlider::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Qt paint event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>void QwtSlider::resizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Qt resize event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<h3>const <code>QwtScaleDraw</code> * QwtSlider::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw of the slider</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3><code>QwtSlider::ScalePosition</code> QwtSlider::scalePosition () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Position of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScalePosition()</code></dl>
<h3>double QwtSlider::scrolledTo (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine the value for a new position of the slider handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Value for the mouse position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isScrollPosition()</code></dl>
<p> Implements <code>QwtAbstractSlider</code>.</p>
<h3>void QwtSlider::setBorderWidth (intwidth)</h3>
<p>Change the slider&#8217;s border width. The border width is used for drawing the slider handle and the trough. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderWidth()</code></dl>
<h3>void QwtSlider::setGroove (boolon)</h3>
<p>En/Disable the groove </p>
<p> The slider can be cutomized by showing a groove for the handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> When true, the groove is visible</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hasGroove()</code>, setThrough()</dl>
<h3>void QwtSlider::setHandleSize (const QSize &amp;size)</h3>
<p>Set the slider&#8217;s handle size. When the size is empty the slider handle will be painted with a default size depending on its <code>orientation()</code> and backgroundStyle(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> New size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>handleSize()</code></dl>
<h3>void QwtSlider::setOrientation (Qt::Orientationorientation)</h3>
<p>Set the orientation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Allowed values are Qt::Horizontal and Qt::Vertical.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientation()</code>, <code>scalePosition()</code></dl>
<h3>void QwtSlider::setScaleDraw (<code>QwtScaleDraw</code> *scaleDraw)</h3>
<p>Set a scale draw. For changing the labels of the scales, it is necessary to derive from <code>QwtScaleDraw</code> and overload <code>QwtScaleDraw::label()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDraw</i> ScaleDraw object, that has to be created with new and will be deleted in <code>~QwtSlider()</code> or the next call of <code>setScaleDraw()</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>scaleDraw()</dl>
<h3>void QwtSlider::setScalePosition (<code>ScalePosition</code>scalePosition)</h3>
<p>Change the position of the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scalePosition</i> Position of the scale.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ScalePosition</code>, <code>scalePosition()</code></dl>
<h3>void QwtSlider::setSpacing (intspacing)</h3>
<p>Change the spacing between trough and scale. A spacing of 0 means, that the backbone of the scale is covered by the trough. </p>
<p> The default setting is 4 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Number of pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>;</dl>
<h3>void QwtSlider::setTrough (boolon)</h3>
<p>En/Disable the trough </p>
<p> The slider can be cutomized by showing a trough for the handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> When true, the groove is visible</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hasTrough()</code>, <code>setGroove()</code></dl>
<h3>void QwtSlider::setUpdateInterval (intinterval)</h3>
<p>Specify the update interval for automatic scrolling. The minimal accepted value is 50 ms. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Update interval in milliseconds</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setUpdateInterval()</code></dl>
<h3>QSize QwtSlider::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>minimumSizeHint()</code></dl>
<h3>QRect QwtSlider::sliderRect () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the slider &#8211; without the scale</dl>
<h3>int QwtSlider::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of pixels between slider and scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code></dl>
<h3>void QwtSlider::timerEvent (QTimerEvent *event) [protected], [virtual]</h3>
<p>Timer event handler </p>
<p> Handles the timer, when the mouse stays pressed inside the <code>sliderRect()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<h3>int QwtSlider::updateInterval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Update interval in milliseconds for automatic scrolling</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setUpdateInterval()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
