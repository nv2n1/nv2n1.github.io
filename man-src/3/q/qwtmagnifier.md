---
title: "qwtmagnifier(3)"
name: "qwtmagnifier"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtmagnifier/"
description: "QwtMagnifier –"
---

<p>QwtMagnifier &#8211; </p>
<p> <code>QwtMagnifier</code> provides zooming, by magnifying in steps.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_magnifier.h&gt; </p>
<p> Inherits QObject. </p>
<p> Inherited by <code>QwtPlotMagnifier</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtMagnifier</code> (QWidget *) </p>
<p> virtual <code>~QwtMagnifier</code> ()<br />
 <i>Destructor. </i><br />
 QWidget * <code>parentWidget</code> () </p>
<p> const QWidget * <code>parentWidget</code> () const </p>
<p> void <code>setEnabled</code> (bool)<br />
 <i>En/disable the magnifier. </i><br />
 bool <code>isEnabled</code> () const </p>
<p> void <code>setMouseFactor</code> (double)<br />
 <i>Change the mouse factor. </i><br />
 double <code>mouseFactor</code> () const </p>
<p> void <code>setMouseButton</code> (Qt::MouseButton, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>getMouseButton</code> (Qt::MouseButton &amp;, Qt::KeyboardModifiers &amp;) const </p>
<p> void <code>setWheelFactor</code> (double)<br />
 <i>Change the wheel factor. </i><br />
 double <code>wheelFactor</code> () const </p>
<p> void <code>setWheelModifiers</code> (Qt::KeyboardModifiers) </p>
<p> Qt::KeyboardModifiers <code>wheelModifiers</code> () const </p>
<p> void <code>setKeyFactor</code> (double)<br />
 <i>Change the key factor. </i><br />
 double <code>keyFactor</code> () const </p>
<p> void <code>setZoomInKey</code> (int key, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>getZoomInKey</code> (int &amp;key, Qt::KeyboardModifiers &amp;) const<br />
 <i>Retrieve the settings of the zoom in key. </i><br />
 void <code>setZoomOutKey</code> (int key, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>getZoomOutKey</code> (int &amp;key, Qt::KeyboardModifiers &amp;) const<br />
 <i>Retrieve the settings of the zoom out key. </i><br />
 virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>rescale</code> (double factor)=0 </p>
<p> virtual void <code>widgetMousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseMoveEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetWheelEvent</code> (QWheelEvent *) </p>
<p> virtual void <code>widgetKeyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>widgetKeyReleaseEvent</code> (QKeyEvent *) </p>
<h2>Detailed Description</h2>
<p><code>QwtMagnifier</code> provides zooming, by magnifying in steps. </p>
<p> Using <code>QwtMagnifier</code> a plot can be zoomed in/out in steps using keys, the mouse wheel or moving a mouse button in vertical direction.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtMagnifier::QwtMagnifier (QWidget *parent) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Widget to be magnified</dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtMagnifier::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Event filter. When <code>isEnabled()</code> is true, the mouse events of the observed widget are filtered. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Forwarded to QObject::eventFilter()</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code> <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtMagnifier::getMouseButton (Qt::MouseButton &amp;button, Qt::KeyboardModifiers &amp;modifiers) const</h3>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMouseButton()</code></dl>
<h3>void QwtMagnifier::getZoomInKey (int &amp;key, Qt::KeyboardModifiers &amp;modifiers) const</h3>
<p>Retrieve the settings of the zoom in key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> Key code, see Qt::Key<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setZoomInKey()</code></dl>
<h3>void QwtMagnifier::getZoomOutKey (int &amp;key, Qt::KeyboardModifiers &amp;modifiers) const</h3>
<p>Retrieve the settings of the zoom out key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> Key code, see Qt::Key<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setZoomOutKey()</code></dl>
<h3>bool QwtMagnifier::isEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true when enabled, false otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setEnabled()</code>, <code>eventFilter()</code></dl>
<h3>double QwtMagnifier::keyFactor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Key factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setKeyFactor()</code></dl>
<h3>double QwtMagnifier::mouseFactor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mouse factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMouseFactor()</code></dl>
<h3>QWidget * QwtMagnifier::parentWidget ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Parent widget, where the rescaling happens</dl>
<h3>const QWidget * QwtMagnifier::parentWidget () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Parent widget, where the rescaling happens</dl>
<h3>virtual void QwtMagnifier::rescale (doublefactor) [protected], [pure virtual]</h3>
<p>Rescale the parent widget </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> Scale factor</dl>
<p> Implemented in <code>QwtPlotMagnifier</code>.</p>
<h3>void QwtMagnifier::setEnabled (boolon)</h3>
<p>En/disable the magnifier. When enabled is true an event filter is installed for the observed widget, otherwise the event filter is removed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true or false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isEnabled()</code>, <code>eventFilter()</code></dl>
<h3>void QwtMagnifier::setKeyFactor (doublefactor)</h3>
<p>Change the key factor. The key factor defines the ratio between the current range on the parent widget and the zoomed range for each key press of the zoom in/out keys. The default value is 0.9. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> Key factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>keyFactor()</code>, <code>setZoomInKey()</code>, <code>setZoomOutKey()</code>, <code>setWheelFactor</code>, <code>setMouseFactor()</code></dl>
<h3>void QwtMagnifier::setMouseButton (Qt::MouseButtonbutton, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Assign the mouse button, that is used for zooming in/out. The default value is Qt::RightButton. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>button</i> Button<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getMouseButton()</code></dl>
<h3>void QwtMagnifier::setMouseFactor (doublefactor)</h3>
<p>Change the mouse factor. The mouse factor defines the ratio between the current range on the parent widget and the zoomed range for each vertical mouse movement. The default value is 0.95. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> Wheel factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mouseFactor()</code>, <code>setMouseButton()</code>, <code>setWheelFactor()</code>, <code>setKeyFactor()</code></dl>
<h3>void QwtMagnifier::setWheelFactor (doublefactor)</h3>
<p>Change the wheel factor. The wheel factor defines the ratio between the current range on the parent widget and the zoomed range for each step of the wheel. </p>
<p> Use values &gt; 1 for magnification (i.e. 2.0) and values &lt; 1 for scaling down (i.e. 1/2.0 = 0.5). You can use this feature for inverting the direction of the wheel. </p>
<p> The default value is 0.9. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> Wheel factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wheelFactor()</code>, setWheelButtonState(), <code>setMouseFactor()</code>, <code>setKeyFactor()</code></dl>
<h3>void QwtMagnifier::setWheelModifiers (Qt::KeyboardModifiersmodifiers)</h3>
<p>Assign keyboard modifiers for zooming in/out using the wheel. The default modifiers are Qt::NoModifiers. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wheelModifiers()</code></dl>
<h3>void QwtMagnifier::setZoomInKey (intkey, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Assign the key, that is used for zooming in. The default combination is Qt::Key_Plus + Qt::NoModifier. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i><br />
 <i>modifiers</i></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getZoomInKey()</code>, <code>setZoomOutKey()</code></dl>
<h3>void QwtMagnifier::setZoomOutKey (intkey, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Assign the key, that is used for zooming out. The default combination is Qt::Key_Minus + Qt::NoModifier. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i><br />
 <i>modifiers</i></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>getZoomOutKey()</code>, <code>setZoomOutKey()</code></dl>
<h3>double QwtMagnifier::wheelFactor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Wheel factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWheelFactor()</code></dl>
<h3>Qt::KeyboardModifiers QwtMagnifier::wheelModifiers () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Wheel modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWheelModifiers()</code></dl>
<h3>void QwtMagnifier::widgetKeyPressEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key press event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtMagnifier::widgetKeyReleaseEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key release event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtMagnifier::widgetMouseMoveEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse move event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>,</dl>
<h3>void QwtMagnifier::widgetMousePressEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse press event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseMoveEvent()</code></dl>
<h3>void QwtMagnifier::widgetMouseReleaseEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse release event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseMoveEvent()</code>,</dl>
<h3>void QwtMagnifier::widgetWheelEvent (QWheelEvent *wheelEvent) [protected], [virtual]</h3>
<p>Handle a wheel event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>wheelEvent</i> Wheel event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
