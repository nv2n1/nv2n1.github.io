---
title: "qwtwheel(3)"
name: "qwtwheel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtwheel/"
description: "QwtWheel –"
---

<p>QwtWheel &#8211; </p>
<p> The Wheel Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_wheel.h&gt; </p>
<p> Inherits QWidget.</p>
<h3>Public Slots</h3>
<p>void <code>setValue</code> (double)<br />
 <i>Set a new value without adjusting to the step raster. </i><br />
 void <code>setTotalAngle</code> (double)<br />
 <i>Set the total angle which the wheel can be turned. </i><br />
 void <code>setViewAngle</code> (double)<br />
 <i>Specify the visible portion of the wheel. </i><br />
 void <code>setMass</code> (double)<br />
 <i>Set the slider&#8217;s mass for flywheel effect. </i></p>
<h3>Signals</h3>
<p>void <code>valueChanged</code> (double <code>value</code>)<br />
 <i>Notify a change of value. </i><br />
 void <code>wheelPressed</code> () </p>
<p> void <code>wheelReleased</code> () </p>
<p> void <code>wheelMoved</code> (double <code>value</code>) </p>
<h3>Public Member Functions</h3>
<p><code>QwtWheel</code> (QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtWheel</code> ()<br />
 <i>Destructor. </i><br />
 double <code>value</code> () const </p>
<p> void <code>setOrientation</code> (Qt::Orientation)<br />
 <i>Set the wheel&#8217;s orientation. </i><br />
 Qt::Orientation <code>orientation</code> () const </p>
<p> double <code>totalAngle</code> () const </p>
<p> double <code>viewAngle</code> () const </p>
<p> void <code>setTickCount</code> (int)<br />
 <i>Adjust the number of grooves in the wheel&#8217;s surface. </i><br />
 int <code>tickCount</code> () const </p>
<p> void <code>setWheelWidth</code> (int)<br />
 <i>Set the width of the wheel. </i><br />
 int <code>wheelWidth</code> () const </p>
<p> void <code>setWheelBorderWidth</code> (int)<br />
 <i>Set the wheel border width of the wheel. </i><br />
 int <code>wheelBorderWidth</code> () const </p>
<p> void <code>setBorderWidth</code> (int)<br />
 <i>Set the border width. </i><br />
 int <code>borderWidth</code> () const </p>
<p> void <code>setInverted</code> (bool tf)<br />
 <i>En/Disable inverted appearance. </i><br />
 bool <code>isInverted</code> () const </p>
<p> void <code>setWrapping</code> (bool tf)<br />
 <i>En/Disable wrapping. </i><br />
 bool <code>wrapping</code> () const </p>
<p> void <code>setSingleStep</code> (double)<br />
 <i>Set the step size of the counter. </i><br />
 double <code>singleStep</code> () const </p>
<p> void <code>setPageStepCount</code> (int)<br />
 <i>Set the page step count. </i><br />
 int <code>pageStepCount</code> () const </p>
<p> void <code>setStepAlignment</code> (bool on)<br />
 <i>En/Disable step alignment. </i><br />
 bool <code>stepAlignment</code> () const </p>
<p> void <code>setRange</code> (double vmin, double vmax)<br />
 <i>Set the minimum and maximum values. </i><br />
 void <code>setMinimum</code> (double min) </p>
<p> double <code>minimum</code> () const </p>
<p> void <code>setMaximum</code> (double max) </p>
<p> double <code>maximum</code> () const </p>
<p> void <code>setUpdateInterval</code> (int)<br />
 <i>Specify the update interval when the wheel is flying. </i><br />
 int <code>updateInterval</code> () const </p>
<p> void <code>setTracking</code> (bool enable)<br />
 <i>En/Disable tracking. </i><br />
 bool <code>isTracking</code> () const </p>
<p> double <code>mass</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *)<br />
 <i>Qt Paint Event. </i><br />
 virtual void <code>mousePressEvent</code> (QMouseEvent *)<br />
 <i>Mouse press event handler. </i><br />
 virtual void <code>mouseReleaseEvent</code> (QMouseEvent *)<br />
 <i>Mouse Release Event handler. </i><br />
 virtual void <code>mouseMoveEvent</code> (QMouseEvent *)<br />
 <i>Mouse Move Event handler. </i><br />
 virtual void <code>keyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>wheelEvent</code> (QWheelEvent *)<br />
 <i>Handle wheel events. </i><br />
 virtual void <code>timerEvent</code> (QTimerEvent *)<br />
 <i>Qt timer event. </i><br />
 void <code>stopFlying</code> ()<br />
 <i>Stop the flying movement of the wheel. </i><br />
 QRect <code>wheelRect</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> virtual void <code>drawTicks</code> (QPainter *, const QRectF &amp;) </p>
<p> virtual void <code>drawWheelBackground</code> (QPainter *, const QRectF &amp;) </p>
<p> virtual double <code>valueAt</code> (const QPoint &amp;) const </p>
<h2>Detailed Description</h2>
<p>The Wheel Widget. </p>
<p> The wheel widget can be used to change values over a very large range in very small steps. Using the <code>setMass()</code> member, it can be configured as a flying wheel. </p>
<p> The default range of the wheel is [0.0, 100.0] </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>The radio example.</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtWheel::borderWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderWidth()</code></dl>
<h3>void QwtWheel::drawTicks (QPainter *painter, const QRectF &amp;rect) [protected], [virtual]</h3>
<p>Draw the Wheel&#8217;s ticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Geometry for the wheel</dl>
<h3>void QwtWheel::drawWheelBackground (QPainter *painter, const QRectF &amp;rect) [protected], [virtual]</h3>
<p>Draw the Wheel&#8217;s background gradient </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Geometry for the wheel</dl>
<h3>bool QwtWheel::isInverted () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the wheel is inverted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInverted()</code></dl>
<h3>bool QwtWheel::isTracking () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when tracking is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTracking()</code>, <code>valueChanged()</code>, <code>wheelMoved()</code></dl>
<h3>void QwtWheel::keyPressEvent (QKeyEvent *event) [protected], [virtual]</h3>
<p>Handle key events </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::Key_Home </p>
<p>&nbsp;<wbr>Step to&nbsp;<wbr><code>minimum()</code></p>
<dt>&bull;</p>
<dd>Qt::Key_End </p>
<p>&nbsp;<wbr>Step to&nbsp;<wbr><code>maximum()</code></p>
<dt>&bull;</p>
<dd>Qt::Key_Up </p>
<p>&nbsp;<wbr>In case of a horizontal or not inverted vertical wheel the value will be incremented by the step size. For an inverted vertical wheel the value will be decremented by the step size.</p>
<dt>&bull;</p>
<dd>Qt::Key_Down </p>
<p>&nbsp;<wbr>In case of a horizontal or not inverted vertical wheel the value will be decremented by the step size. For an inverted vertical wheel the value will be incremented by the step size.</p>
<dt>&bull;</p>
<dd>Qt::Key_PageUp </p>
<p>&nbsp;<wbr>The value will be incremented by pageStepSize()&nbsp;<wbr>*&nbsp;<wbr>singleStepSize().</p>
<dt>&bull;</p>
<dd>Qt::Key_PageDown </p>
<p>&nbsp;<wbr>The value will be decremented by pageStepSize()&nbsp;<wbr>*&nbsp;<wbr>singleStepSize().</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Key event</dl>
<h3>double QwtWheel::mass () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>mass</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMass()</code></dl>
<h3>double QwtWheel::maximum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum of the range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMaximum()</code>, <code>minimum()</code></dl>
<h3>double QwtWheel::minimum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The minimum of the range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMinimum()</code>, <code>maximum()</code></dl>
<h3>QSize QwtWheel::minimumSizeHint () const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The return value is based on the wheel width.</dl>
<h3>void QwtWheel::mouseMoveEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse Move Event handler. Turn the wheel according to the mouse position </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<h3>void QwtWheel::mousePressEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse press event handler. Start movement of the wheel. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<h3>void QwtWheel::mouseReleaseEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse Release Event handler. When the wheel has no mass the movement of the wheel stops, otherwise it starts flying. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<h3>Qt::Orientation QwtWheel::orientation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code></dl>
<h3>int QwtWheel::pageStepCount () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Page step count</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPageStepCount()</code>, <code>singleStep()</code></dl>
<h3>void QwtWheel::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Qt Paint Event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>void QwtWheel::setBorderWidth (intwidth)</h3>
<p>Set the border width. The border defaults to 2. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderWidth()</code></dl>
<h3>void QwtWheel::setInverted (boolon)</h3>
<p>En/Disable inverted appearance. An inverted wheel increases its values in the opposite direction. The direction of an inverted horizontal wheel will be from right to left an inverted vertical wheel will increase from bottom to top. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> En/Disable inverted appearance</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isInverted()</code></dl>
<h3>void QwtWheel::setMass (doublemass) [slot]</h3>
<p>Set the slider&#8217;s mass for flywheel effect. If the slider&#8217;s mass is greater then 0, it will continue to move after the mouse button has been released. Its speed decreases with time at a rate depending on the slider&#8217;s mass. A large mass means that it will continue to move for a long time. </p>
<p> Derived widgets may overload this function to make it public. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mass</i> New mass in kg</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mass()</code></dl>
<h3>void QwtWheel::setMaximum (doublevalue)</h3>
<p>Set the maximum value of the range </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Maximum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMinimum()</code>, <code>maximum()</code></dl>
<h3>void QwtWheel::setMinimum (doublevalue)</h3>
<p>Set the minimum value of the range </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Minimum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMaximum()</code>, <code>minimum()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The maximum is adjusted if necessary to ensure that the range remains valid.</dl>
<h3>void QwtWheel::setOrientation (Qt::Orientationorientation)</h3>
<p>Set the wheel&#8217;s orientation. The default orientation is Qt::Horizontal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Qt::Horizontal or Qt::Vertical.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientation()</code></dl>
<h3>void QwtWheel::setPageStepCount (intcount)</h3>
<p>Set the page step count. pageStepCount is a multiplicator for the single step size that typically corresponds to the user pressing PageUp or PageDown. </p>
<p> A value of 0 disables page stepping. </p>
<p> The default value is 1. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>count</i> Multiplicator for the single step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pageStepCount()</code>, <code>setSingleStep()</code></dl>
<h3>void QwtWheel::setRange (doublemin, doublemax)</h3>
<p>Set the minimum and maximum values. The maximum is adjusted if necessary to ensure that the range remains valid. The value might be modified to be inside of the range. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>min</i> Minimum value<br />
 <i>max</i> Maximum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimum()</code>, <code>maximum()</code></dl>
<h3>void QwtWheel::setSingleStep (doublestepSize)</h3>
<p>Set the step size of the counter. A value &lt;= 0.0 disables stepping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepSize</i> Single step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>singleStep()</code>, <code>setPageStepCount()</code></dl>
<h3>void QwtWheel::setStepAlignment (boolon)</h3>
<p>En/Disable step alignment. When step alignment is enabled value changes initiated by user input ( mouse, keyboard, wheel ) are aligned to the multiples of the single step. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>stepAlignment()</code>, <code>setSingleStep()</code></dl>
<h3>void QwtWheel::setTickCount (intcount)</h3>
<p>Adjust the number of grooves in the wheel&#8217;s surface. The number of grooves is limited to 6 &lt;= count &lt;= 50. Values outside this range will be clipped. The default value is 10. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>count</i> Number of grooves per 360 degrees</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>tickCount()</code></dl>
<h3>void QwtWheel::setTotalAngle (doubleangle) [slot]</h3>
<p>Set the total angle which the wheel can be turned. One full turn of the wheel corresponds to an angle of 360 degrees. A total angle of n*360 degrees means that the wheel has to be turned n times around its axis to get from the minimum value to the maximum value. </p>
<p> The default setting of the total angle is 360 degrees. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>angle</i> total angle in degrees</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>totalAngle()</code></dl>
<h3>void QwtWheel::setTracking (boolenable)</h3>
<p>En/Disable tracking. If tracking is enabled (the default), the wheel emits the <code>valueChanged()</code> signal while the wheel is moving. If tracking is disabled, the wheel emits the <code>valueChanged()</code> signal only when the wheel movement is terminated. </p>
<p> The <code>wheelMoved()</code> signal is emitted regardless id tracking is enabled or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enable</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isTracking()</code></dl>
<h3>void QwtWheel::setUpdateInterval (intinterval)</h3>
<p>Specify the update interval when the wheel is flying. Default and minimum value is 50 ms. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval in milliseconds</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateInterval()</code>, <code>setMass()</code>, <code>setTracking()</code></dl>
<h3>void QwtWheel::setValue (doublevalue) [slot]</h3>
<p>Set a new value without adjusting to the step raster. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>value()</code>, <code>valueChanged()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The value is clipped when it lies outside the range.</dl>
<h3>void QwtWheel::setViewAngle (doubleangle) [slot]</h3>
<p>Specify the visible portion of the wheel. You may use this function for fine-tuning the appearance of the wheel. The default value is 175 degrees. The value is limited from 10 to 175 degrees. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>angle</i> Visible angle in degrees</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>viewAngle()</code>, <code>setTotalAngle()</code></dl>
<h3>void QwtWheel::setWheelBorderWidth (intborderWidth)</h3>
<p>Set the wheel border width of the wheel. The wheel border must not be smaller than 1 and is limited in dependence on the wheel&#8217;s size. Values outside the allowed range will be clipped. </p>
<p> The wheel border defaults to 2. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>borderWidth</i> Border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>internalBorder()</dl>
<h3>void QwtWheel::setWheelWidth (intwidth)</h3>
<p>Set the width of the wheel. Corresponds to the wheel height for horizontal orientation, and the wheel width for vertical orientation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> the wheel&#8217;s width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wheelWidth()</code></dl>
<h3>void QwtWheel::setWrapping (boolon)</h3>
<p>En/Disable wrapping. If wrapping is true stepping up from <code>maximum()</code> value will take you to the <code>minimum()</code> value and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> En/Disable wrapping</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wrapping()</code></dl>
<h3>double QwtWheel::singleStep () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Single step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSingleStep()</code></dl>
<h3>QSize QwtWheel::sizeHint () const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>a size hint</dl>
<h3>bool QwtWheel::stepAlignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the step alignment is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStepAlignment()</code>, <code>singleStep()</code></dl>
<h3>int QwtWheel::tickCount () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of grooves in the wheel&#8217;s surface.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>setTickCnt()</dl>
<h3>void QwtWheel::timerEvent (QTimerEvent *event) [protected], [virtual]</h3>
<p>Qt timer event. The flying wheel effect is implemented using a timer </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Timer event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateInterval()</code></dl>
<h3>double QwtWheel::totalAngle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Total angle which the wheel can be turned.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTotalAngle()</code></dl>
<h3>int QwtWheel::updateInterval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Update interval when the wheel is flying</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setUpdateInterval()</code>, <code>mass()</code>, <code>isTracking()</code></dl>
<h3>double QwtWheel::value () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current value of the wheel</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValue()</code>, <code>valueChanged()</code></dl>
<h3>double QwtWheel::valueAt (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine the value corresponding to a specified point </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Value corresponding to pos</dl>
<h3>void QwtWheel::valueChanged (doublevalue) [signal]</h3>
<p>Notify a change of value. When tracking is enabled this signal will be emitted every time the value changes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> new value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTracking()</code></dl>
<h3>double QwtWheel::viewAngle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Visible portion of the wheel</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setViewAngle()</code>, <code>totalAngle()</code></dl>
<h3>int QwtWheel::wheelBorderWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Wheel border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWheelBorderWidth()</code></dl>
<h3>void QwtWheel::wheelEvent (QWheelEvent *event) [protected], [virtual]</h3>
<p>Handle wheel events. In/Decrement the value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Wheel event</dl>
<h3>void QwtWheel::wheelMoved (doublevalue) [signal]</h3>
<p>This signal is emitted when the user moves the wheel with the mouse. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> new value</dl>
<h3>void QwtWheel::wheelPressed () [signal]</h3>
<p>This signal is emitted when the user presses the the wheel with the mouse</p>
<h3>QRect QwtWheel::wheelRect () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle of the wheel without the outer border</dl>
<h3>void QwtWheel::wheelReleased () [signal]</h3>
<p>This signal is emitted when the user releases the mouse</p>
<h3>int QwtWheel::wheelWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the wheel</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWheelWidth()</code></dl>
<h3>bool QwtWheel::wrapping () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when wrapping is set</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWrapping()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
