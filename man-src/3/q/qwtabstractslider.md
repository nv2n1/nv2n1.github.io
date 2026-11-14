---
title: "qwtabstractslider(3)"
name: "qwtabstractslider"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtabstractslider/"
description: "QwtAbstractSlider –"
---

<p>QwtAbstractSlider &#8211; </p>
<p> An abstract base class for slider widgets with a scale.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_abstract_slider.h&gt; </p>
<p> Inherits <code>QwtAbstractScale</code>. </p>
<p> Inherited by <code>QwtDial</code>, <code>QwtKnob</code>, and <code>QwtSlider</code>.</p>
<h3>Public Slots</h3>
<p>void <code>setValue</code> (double val) </p>
<h3>Signals</h3>
<p>void <code>valueChanged</code> (double <code>value</code>)<br />
 <i>Notify a change of value. </i><br />
 void <code>sliderPressed</code> () </p>
<p> void <code>sliderReleased</code> () </p>
<p> void <code>sliderMoved</code> (double <code>value</code>) </p>
<h3>Public Member Functions</h3>
<p><code>QwtAbstractSlider</code> (QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtAbstractSlider</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setValid</code> (bool) </p>
<p> bool <code>isValid</code> () const </p>
<p> double <code>value</code> () const<br />
 <i>Returns the current value. </i><br />
 void <code>setWrapping</code> (bool) </p>
<p> bool <code>wrapping</code> () const </p>
<p> void <code>setTotalSteps</code> (uint)<br />
 <i>Set the number of steps. </i><br />
 uint <code>totalSteps</code> () const </p>
<p> void <code>setSingleSteps</code> (uint)<br />
 <i>Set the number of steps for a single increment. </i><br />
 uint <code>singleSteps</code> () const </p>
<p> void <code>setPageSteps</code> (uint)<br />
 <i>Set the number of steps for a page increment. </i><br />
 uint <code>pageSteps</code> () const </p>
<p> void <code>setStepAlignment</code> (bool)<br />
 <i>Enable step alignment. </i><br />
 bool <code>stepAlignment</code> () const </p>
<p> void <code>setTracking</code> (bool)<br />
 <i>Enables or disables tracking. </i><br />
 bool <code>isTracking</code> () const </p>
<p> void <code>setReadOnly</code> (bool) </p>
<p> bool <code>isReadOnly</code> () const </p>
<p> void <code>setInvertedControls</code> (bool) </p>
<p> bool <code>invertedControls</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>mousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>mouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>mouseMoveEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>keyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>wheelEvent</code> (QWheelEvent *) </p>
<p> virtual bool <code>isScrollPosition</code> (const QPoint &amp;pos) const =0<br />
 <i>Determine what to do when the user presses a mouse button. </i><br />
 virtual double <code>scrolledTo</code> (const QPoint &amp;pos) const =0<br />
 <i>Determine the value for a new position of the movable part of the slider. </i><br />
 void <code>incrementValue</code> (int numSteps) </p>
<p> virtual void <code>scaleChange</code> () </p>
<p> virtual void <code>sliderChange</code> ()<br />
 <i>Calling update() </i><br />
 double <code>incrementedValue</code> (double <code>value</code>, int stepCount) const </p>
<h2>Detailed Description</h2>
<p>An abstract base class for slider widgets with a scale. </p>
<p> A slider widget displays a value according to a scale. The class is designed as a common super class for widgets like <code>QwtKnob</code>, <code>QwtDial</code> and <code>QwtSlider</code>. </p>
<p> When the slider is nor readOnly() its value can be modified by keyboard, mouse and wheel inputs. </p>
<p> The range of the slider is divided into a number of steps from which the value increments according to user inputs depend. Only for linear scales the number of steps correspond with a fixed step size.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAbstractSlider::QwtAbstractSlider (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. The scale is initialized to [0.0, 100.0], the number of steps is set to 100 with 1 and 10 and single an page step sizes. Step alignment is enabled. </p>
<p> The initial value is invalid. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtAbstractSlider::incrementedValue (doublevalue, intstepCount) const [protected]</h3>
<p>Increment a value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value<br />
 <i>stepCount</i> Number of steps</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Incremented value</dl>
<h3>void QwtAbstractSlider::incrementValue (intstepCount) [protected]</h3>
<p>Increment the slider </p>
<p> The step size depends on the number of <code>totalSteps()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepCount</i> Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTotalSteps()</code>, <code>incrementedValue()</code></dl>
<h3>bool QwtAbstractSlider::invertedControls () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the controls are inverted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInvertedControls()</code></dl>
<h3>bool QwtAbstractSlider::isReadOnly () const</h3>
<p>In read only mode the slider can&#8217;t be controlled by mouse or keyboard. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if read only</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setReadOnly()</code></dl>
<h3>virtual bool QwtAbstractSlider::isScrollPosition (const QPoint &amp;pos) const [protected], [pure virtual]</h3>
<p>Determine what to do when the user presses a mouse button. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>True,when</i> pos is a valid scroll position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scrolledTo()</code></dl>
<p> Implemented in <code>QwtKnob</code>, <code>QwtDial</code>, and <code>QwtSlider</code>.</p>
<h3>bool QwtAbstractSlider::isTracking () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when tracking has been enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTracking()</code></dl>
<h3>bool QwtAbstractSlider::isValid () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the value is invalid</dl>
<h3>void QwtAbstractSlider::keyPressEvent (QKeyEvent *event) [protected], [virtual]</h3>
<p>Handles key events </p>
<p> <code>QwtAbstractSlider</code> handles the following keys: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::Key_Left </p>
<p>&nbsp;<wbr>Add/Subtract&nbsp;<wbr><code>singleSteps()</code>&nbsp;<wbr>in direction to&nbsp;<wbr><code>lowerBound()</code>;</p>
<dt>&bull;</p>
<dd>Qt::Key_Right </p>
<p>&nbsp;<wbr>Add/Subtract&nbsp;<wbr><code>singleSteps()</code>&nbsp;<wbr>in direction to&nbsp;<wbr><code>upperBound()</code>;</p>
<dt>&bull;</p>
<dd>Qt::Key_Down </p>
<p>&nbsp;<wbr>Subtract&nbsp;<wbr><code>singleSteps()</code>, when&nbsp;<wbr><code>invertedControls()</code>&nbsp;<wbr>is false</p>
<dt>&bull;</p>
<dd>Qt::Key_Up </p>
<p>&nbsp;<wbr>Add&nbsp;<wbr><code>singleSteps()</code>, when&nbsp;<wbr><code>invertedControls()</code>&nbsp;<wbr>is false</p>
<dt>&bull;</p>
<dd>Qt::Key_PageDown </p>
<p>&nbsp;<wbr>Subtract&nbsp;<wbr><code>pageSteps()</code>, when&nbsp;<wbr><code>invertedControls()</code>&nbsp;<wbr>is false</p>
<dt>&bull;</p>
<dd>Qt::Key_PageUp </p>
<p>&nbsp;<wbr>Add&nbsp;<wbr><code>pageSteps()</code>, when&nbsp;<wbr><code>invertedControls()</code>&nbsp;<wbr>is false</p>
<dt>&bull;</p>
<dd>Qt::Key_Home </p>
<p>&nbsp;<wbr>Set the value to the&nbsp;<wbr><code>minimum()</code></p>
<dt>&bull;</p>
<dd>Qt::Key_End </p>
<p>&nbsp;<wbr>Set the value to the&nbsp;<wbr><code>maximum()</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isReadOnly()</code></dl>
<p> Reimplemented in <code>QwtCompass</code>.</p>
<h3>void QwtAbstractSlider::mouseMoveEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse Move Event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<h3>void QwtAbstractSlider::mousePressEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse press event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<p> Reimplemented in <code>QwtSlider</code>.</p>
<h3>void QwtAbstractSlider::mouseReleaseEvent (QMouseEvent *event) [protected], [virtual]</h3>
<p>Mouse Release Event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Mouse event</dl>
<p> Reimplemented in <code>QwtSlider</code>.</p>
<h3>uint QwtAbstractSlider::pageSteps () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPageSteps()</code>, <code>totalSteps()</code>, <code>singleSteps()</code></dl>
<h3>void QwtAbstractSlider::scaleChange () [protected], [virtual]</h3>
<p>Update the slider according to modifications of the scale </p>
<p> Reimplemented from <code>QwtAbstractScale</code>. </p>
<p> Reimplemented in <code>QwtDial</code>, and <code>QwtSlider</code>.</p>
<h3>virtual double QwtAbstractSlider::scrolledTo (const QPoint &amp;pos) const [protected], [pure virtual]</h3>
<p>Determine the value for a new position of the movable part of the slider. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Value for the mouse position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isScrollPosition()</code></dl>
<p> Implemented in <code>QwtKnob</code>, <code>QwtDial</code>, and <code>QwtSlider</code>.</p>
<h3>void QwtAbstractSlider::setInvertedControls (boolon)</h3>
<p>Invert wheel and key events </p>
<p> Usually scrolling the mouse wheel &#8216;up&#8217; and using keys like page up will increase the slider&#8217;s value towards its maximum. When <code>invertedControls()</code> is enabled the value is scrolled towards its minimum. </p>
<p> Inverting the controls might be f.e. useful for a vertical slider with an inverted scale ( decreasing from top to bottom ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Invert controls, when true</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invertedControls()</code>, keyEvent(), <code>wheelEvent()</code></dl>
<h3>void QwtAbstractSlider::setPageSteps (uintstepCount)</h3>
<p>Set the number of steps for a page increment. The range of the slider is divided into a number of steps from which the value increments according to user inputs depend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepCount</i> Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pageSteps()</code>, <code>setTotalSteps()</code>, <code>setSingleSteps()</code></dl>
<h3>void QwtAbstractSlider::setReadOnly (boolon)</h3>
<p>En/Disable read only mode </p>
<p> In read only mode the slider can&#8217;t be controlled by mouse or keyboard. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enables in case of true</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isReadOnly()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The focus policy is set to Qt::StrongFocus or Qt::NoFocus</dl>
<h3>void QwtAbstractSlider::setSingleSteps (uintstepCount)</h3>
<p>Set the number of steps for a single increment. The range of the slider is divided into a number of steps from which the value increments according to user inputs depend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepCount</i> Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>singleSteps()</code>, <code>setTotalSteps()</code>, <code>setPageSteps()</code></dl>
<h3>void QwtAbstractSlider::setStepAlignment (boolon)</h3>
<p>Enable step alignment. When step alignment is enabled values resulting from slider movements are aligned to the step size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enable step alignment when true</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>stepAlignment()</code></dl>
<h3>void QwtAbstractSlider::setTotalSteps (uintstepCount)</h3>
<p>Set the number of steps. The range of the slider is divided into a number of steps from which the value increments according to user inputs depend. </p>
<p> The default setting is 100. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepCount</i> Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>totalSteps()</code>, <code>setSingleSteps()</code>, <code>setPageSteps()</code></dl>
<h3>void QwtAbstractSlider::setTracking (boolon)</h3>
<p>Enables or disables tracking. If tracking is enabled, the slider emits the <code>valueChanged()</code> signal while the movable part of the slider is being dragged. If tracking is disabled, the slider emits the <code>valueChanged()</code> signal only when the user releases the slider. </p>
<p> Tracking is enabled by default. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true (enable) or false (disable) tracking.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isTracking()</code>, <code>sliderMoved()</code></dl>
<h3>void QwtAbstractSlider::setValid (boolon)</h3>
<p>Set the value to be valid/invalid </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> When true, the value is invalidated</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValue()</code></dl>
<h3>void QwtAbstractSlider::setValue (doublevalue) [slot]</h3>
<p>Set the slider to the specified value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValid()</code>, <code>sliderChange()</code>, <code>valueChanged()</code></dl>
<h3>void QwtAbstractSlider::setWrapping (boolon)</h3>
<p>If wrapping is true stepping up from <code>upperBound()</code> value will take you to the <code>minimum()</code> value and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> En/Disable wrapping</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wrapping()</code></dl>
<h3>uint QwtAbstractSlider::singleSteps () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSingleSteps()</code>, <code>totalSteps()</code>, <code>pageSteps()</code></dl>
<h3>void QwtAbstractSlider::sliderMoved (doublevalue) [signal]</h3>
<p>This signal is emitted when the user moves the slider with the mouse. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>valueChanged()</code></dl>
<h3>void QwtAbstractSlider::sliderPressed () [signal]</h3>
<p>This signal is emitted when the user presses the movable part of the slider.</p>
<h3>void QwtAbstractSlider::sliderReleased () [signal]</h3>
<p>This signal is emitted when the user releases the movable part of the slider.</p>
<h3>bool QwtAbstractSlider::stepAlignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when step alignment is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStepAlignment()</code></dl>
<h3>uint QwtAbstractSlider::totalSteps () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTotalSteps()</code>, <code>singleSteps()</code>, <code>pageSteps()</code></dl>
<h3>void QwtAbstractSlider::valueChanged (doublevalue) [signal]</h3>
<p>Notify a change of value. When tracking is enabled (default setting), this signal will be emitted every time the value changes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTracking()</code>, <code>sliderMoved()</code></dl>
<h3>void QwtAbstractSlider::wheelEvent (QWheelEvent *event) [protected], [virtual]</h3>
<p>Wheel Event handler </p>
<p> In/decreases the value by s number of steps. The direction depends on the <code>invertedControls()</code> property. </p>
<p> When the control or shift modifier is pressed the wheel delta ( divided by 120 ) is mapped to an increment according to <code>pageSteps()</code>. Otherwise it is mapped to <code>singleSteps()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Wheel event</dl>
<p> Reimplemented in <code>QwtDial</code>.</p>
<h3>bool QwtAbstractSlider::wrapping () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when wrapping is set</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWrapping()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
