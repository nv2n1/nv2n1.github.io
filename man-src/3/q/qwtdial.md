---
title: "qwtdial(3)"
name: "qwtdial"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdial/"
description: "QwtDial –"
---

<p>QwtDial &#8211; </p>
<p> <code>QwtDial</code> class provides a rounded range control.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dial.h&gt; </p>
<p> Inherits <code>QwtAbstractSlider</code>. </p>
<p> Inherited by <code>QwtAnalogClock</code>, and <code>QwtCompass</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Shadow</code> { <code>Plain</code> = QFrame::Plain, <code>Raised</code> = QFrame::Raised, <code>Sunken</code> = QFrame::Sunken }<br />
 <i>Frame shadow. </i><br />
 enum <code>Mode</code> { <code>RotateNeedle</code>, <code>RotateScale</code> }<br />
 <i>Mode controlling whether the needle or the scale is rotating. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtDial</code> (QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtDial</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setFrameShadow</code> (<code>Shadow</code>) </p>
<p> <code>Shadow</code> <code>frameShadow</code> () const </p>
<p> void <code>setLineWidth</code> (int) </p>
<p> int <code>lineWidth</code> () const </p>
<p> void <code>setMode</code> (<code>Mode</code>)<br />
 <i>Change the mode of the dial. </i><br />
 <code>Mode</code> <code>mode</code> () const </p>
<p> void <code>setScaleArc</code> (double min, double max) </p>
<p> void <code>setMinScaleArc</code> (double min) </p>
<p> double <code>minScaleArc</code> () const </p>
<p> void <code>setMaxScaleArc</code> (double min) </p>
<p> double <code>maxScaleArc</code> () const </p>
<p> virtual void <code>setOrigin</code> (double)<br />
 <i>Change the origin. </i><br />
 double <code>origin</code> () const </p>
<p> void <code>setNeedle</code> (<code>QwtDialNeedle</code> *) </p>
<p> const <code>QwtDialNeedle</code> * <code>needle</code> () const </p>
<p> <code>QwtDialNeedle</code> * <code>needle</code> () </p>
<p> QRect <code>boundingRect</code> () const </p>
<p> QRect <code>innerRect</code> () const </p>
<p> virtual QRect <code>scaleInnerRect</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> void <code>setScaleDraw</code> (<code>QwtRoundScaleDraw</code> *) </p>
<p> <code>QwtRoundScaleDraw</code> * <code>scaleDraw</code> () </p>
<p> const <code>QwtRoundScaleDraw</code> * <code>scaleDraw</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>wheelEvent</code> (QWheelEvent *) </p>
<p> virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>changeEvent</code> (QEvent *) </p>
<p> virtual void <code>drawFrame</code> (QPainter *p) </p>
<p> virtual void <code>drawContents</code> (QPainter *) const<br />
 <i>Draw the contents inside the frame. </i><br />
 virtual void <code>drawFocusIndicator</code> (QPainter *) const </p>
<p> void <code>invalidateCache</code> () </p>
<p> virtual void <code>drawScale</code> (QPainter *, const QPointF &amp;center, double radius) const </p>
<p> virtual void <code>drawScaleContents</code> (QPainter *painter, const QPointF &amp;center, double radius) const </p>
<p> virtual void <code>drawNeedle</code> (QPainter *, const QPointF &amp;, double radius, double direction, QPalette::ColorGroup) const </p>
<p> virtual double <code>scrolledTo</code> (const QPoint &amp;) const<br />
 <i>Determine the value for a new position of the slider handle. </i><br />
 virtual bool <code>isScrollPosition</code> (const QPoint &amp;) const<br />
 <i>Determine what to do when the user presses a mouse button. </i><br />
 virtual void <code>sliderChange</code> ()<br />
 <i>Calling update() </i><br />
 virtual void <code>scaleChange</code> () </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>QwtDial</code> class provides a rounded range control. </p>
<p> <code>QwtDial</code> is intended as base class for dial widgets like speedometers, compass widgets, clocks &#8230; </p>
<p> A dial contains a scale and a needle indicating the current value of the dial. Depending on Mode one of them is fixed and the other is rotating. If not <code>isReadOnly()</code> the dial can be rotated by dragging the mouse or using keyboard inputs (see <code>QwtAbstractSlider::keyPressEvent()</code>). A dial might be wrapping, what means a rotation below/above one limit continues on the other limit (f.e compass). The scale might cover any arc of the dial, its values are related to the <code>origin()</code> of the dial. </p>
<p> Often dials have to be updated very often according to values from external devices. For these high refresh rates <code>QwtDial</code> caches as much as possible. For derived classes it might be necessary to clear these caches manually according to attribute changes using <code>invalidateCache()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtCompass</code>, <code>QwtAnalogClock</code>, <code>QwtDialNeedle</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The controls and dials examples shows different types of dials. </p>
<p> QDial is more similar to <code>QwtKnob</code> than to <code>QwtDial</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtDial::Mode</code></h3>
<p>Mode controlling whether the needle or the scale is rotating. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>RotateNeedle </i></p>
<dd>The needle is rotating.</p>
<dt><i>RotateScale </i></p>
<dd>The needle is fixed, the scales are rotating.</dl>
<h3>enum <code>QwtDial::Shadow</code></h3>
<p>Frame shadow. Unfortunately it is not possible to use QFrame::Shadow as a property of a widget that is not derived from QFrame. The following enum is made for the designer only. It is safe to use QFrame::Shadow instead. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Plain </i></p>
<dd>QFrame::Plain.</p>
<dt><i>Raised </i></p>
<dd>QFrame::Raised.</p>
<dt><i>Sunken </i></p>
<dd>QFrame::Sunken.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDial::QwtDial (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<p> Create a dial widget with no needle. The scale is initialized to [ 0.0, 360.0 ] and 360 steps ( <code>QwtAbstractSlider::setTotalSteps()</code> ). The origin of the scale is at 90°, </p>
<p> The value is set to 0.0. </p>
<p> The default mode is <code>QwtDial::RotateNeedle</code>.</p>
<h2>Member Function Documentation</h2>
<h3>QRect QwtDial::boundingRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>bounding rectangle of the dial including the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>scaleInnerRect()</code>, <code>innerRect()</code></dl>
<h3>void QwtDial::changeEvent (QEvent *event) [protected], [virtual]</h3>
<p>Change Event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Change event</dl>
<p> Invalidates internal paint caches if necessary</p>
<h3>void QwtDial::drawContents (QPainter *painter) const [protected], [virtual]</h3>
<p>Draw the contents inside the frame. QPalette::Window is the background color outside of the frame. QPalette::Base is the background color inside the frame. QPalette::WindowText is the background color inside the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>boundingRect()</code>, <code>innerRect()</code>, <code>scaleInnerRect()</code>, QWidget::setPalette()</dl>
<h3>void QwtDial::drawFocusIndicator (QPainter *painter) const [protected], [virtual]</h3>
<p>Draw the focus indicator </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>void QwtDial::drawFrame (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the frame around the dial </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lineWidth()</code>, <code>frameShadow()</code></dl>
<h3>void QwtDial::drawNeedle (QPainter *painter, const QPointF &amp;center, doubleradius, doubledirection, QPalette::ColorGroupcolorGroup) const [protected], [virtual]</h3>
<p>Draw the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the dial<br />
 <i>radius</i> Length for the needle<br />
 <i>direction</i> Direction of the needle in degrees, counter clockwise<br />
 <i>colorGroup</i> ColorGroup</dl>
<p> Reimplemented in <code>QwtAnalogClock</code>.</p>
<h3>void QwtDial::drawScale (QPainter *painter, const QPointF &amp;center, doubleradius) const [protected], [virtual]</h3>
<p>Draw the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the dial<br />
 <i>radius</i> Radius of the scale</dl>
<h3>void QwtDial::drawScaleContents (QPainter *painter, const QPointF &amp;center, doubleradius) const [protected], [virtual]</h3>
<p>Draw the contents inside the scale </p>
<p> Paints nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the contents circle<br />
 <i>radius</i> Radius of the contents circle</dl>
<p> Reimplemented in <code>QwtCompass</code>.</p>
<h3><code>QwtDial::Shadow</code> QwtDial::frameShadow () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Frame shadow /sa <code>setFrameShadow()</code>, <code>lineWidth()</code>, QFrame::frameShadow()</dl>
<h3>QRect QwtDial::innerRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>bounding rectangle of the circle inside the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>scaleInnerRect()</code>, <code>boundingRect()</code></dl>
<h3>void QwtDial::invalidateCache () [protected]</h3>
<p>Invalidate the internal caches used to speed up repainting</p>
<h3>bool QwtDial::isScrollPosition (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine what to do when the user presses a mouse button. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>True,when</i> the inner circle contains pos</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scrolledTo()</code></dl>
<p> Implements <code>QwtAbstractSlider</code>.</p>
<h3>int QwtDial::lineWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Line width of the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>frameShadow()</code>, <code>lineWidth()</code></dl>
<h3>double QwtDial::maxScaleArc () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Upper limit of the scale arc</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleArc()</code></dl>
<h3>QSize QwtDial::minimumSizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>sizeHint()</code></dl>
<h3>double QwtDial::minScaleArc () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Lower limit of the scale arc</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleArc()</code></dl>
<h3><code>QwtDial::Mode</code> QwtDial::mode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode of the dial.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMode()</code>, <code>origin()</code>, <code>setScaleArc()</code>, <code>value()</code></dl>
<h3>const <code>QwtDialNeedle</code> * QwtDial::needle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>needle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNeedle()</code></dl>
<h3><code>QwtDialNeedle</code> * QwtDial::needle ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>needle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNeedle()</code></dl>
<h3>double QwtDial::origin () const</h3>
<p>The origin is the angle where scale and needle is relative to. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Origin of the dial</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrigin()</code></dl>
<h3>void QwtDial::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint the dial </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>void QwtDial::scaleChange () [protected], [virtual]</h3>
<p>Invalidate the internal caches and call <code>QwtAbstractSlider::scaleChange()</code> </p>
<p> Reimplemented from <code>QwtAbstractSlider</code>.</p>
<h3><code>QwtRoundScaleDraw</code> * QwtDial::scaleDraw ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw</dl>
<h3>const <code>QwtRoundScaleDraw</code> * QwtDial::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw</dl>
<h3>QRect QwtDial::scaleInnerRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>rectangle inside the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>boundingRect()</code>, <code>innerRect()</code></dl>
<h3>double QwtDial::scrolledTo (const QPoint &amp;pos) const [protected], [virtual]</h3>
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
<h3>void QwtDial::setFrameShadow (<code>Shadow</code>shadow)</h3>
<p>Sets the frame shadow value from the frame style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shadow</i> Frame shadow</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, QFrame::setFrameShadow()</dl>
<h3>void QwtDial::setLineWidth (intlineWidth)</h3>
<p>Sets the line width of the frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lineWidth</i> Line width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFrameShadow()</code></dl>
<h3>void QwtDial::setMaxScaleArc (doublemax)</h3>
<p>Set the upper limit for the scale arc </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>max</i> Upper limit of the scale arc</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleArc()</code>, <code>setMinScaleArc()</code></dl>
<h3>void QwtDial::setMinScaleArc (doublemin)</h3>
<p>Set the lower limit for the scale arc </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>min</i> Lower limit of the scale arc</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleArc()</code>, <code>setMaxScaleArc()</code></dl>
<h3>void QwtDial::setMode (<code>Mode</code>mode)</h3>
<p>Change the mode of the dial. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> New mode</dl>
<p> In case of <code>QwtDial::RotateNeedle</code> the needle is rotating, in case of <code>QwtDial::RotateScale</code>, the needle points to <code>origin()</code> and the scale is rotating. </p>
<p> The default mode is <code>QwtDial::RotateNeedle</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mode()</code>, <code>setValue()</code>, <code>setOrigin()</code></dl>
<h3>void QwtDial::setNeedle (<code>QwtDialNeedle</code> *needle)</h3>
<p>Set a needle for the dial </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>needle</i> Needle</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The needle will be deleted, when a different needle is set or in <code>~QwtDial()</code></dl>
<h3>void QwtDial::setOrigin (doubleorigin) [virtual]</h3>
<p>Change the origin. The origin is the angle where scale and needle is relative to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>origin</i> New origin</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>origin()</code></dl>
<h3>void QwtDial::setScaleArc (doubleminArc, doublemaxArc)</h3>
<p>Change the arc of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minArc</i> Lower limit<br />
 <i>maxArc</i> Upper limit</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minScaleArc()</code>, <code>maxScaleArc()</code></dl>
<h3>void QwtDial::setScaleDraw (<code>QwtRoundScaleDraw</code> *scaleDraw)</h3>
<p>Set an individual scale draw </p>
<p> The motivation for setting a scale draw is often to overload <code>QwtRoundScaleDraw::label()</code> to return individual tick labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDraw</i> Scale draw</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The previous scale draw is deleted</dl>
<h3>QSize QwtDial::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimumSizeHint()</code></dl>
<h3>void QwtDial::wheelEvent (QWheelEvent *event) [protected], [virtual]</h3>
<p>Wheel Event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Wheel event</dl>
<p> Reimplemented from <code>QwtAbstractSlider</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
