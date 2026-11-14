---
title: "qwtpanner(3)"
name: "qwtpanner"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpanner/"
description: "QwtPanner –"
---

<p>QwtPanner &#8211; </p>
<p> <code>QwtPanner</code> provides panning of a widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_panner.h&gt; </p>
<p> Inherits QWidget. </p>
<p> Inherited by <code>QwtPlotPanner</code>.</p>
<h3>Signals</h3>
<p>void <code>panned</code> (int dx, int dy) </p>
<p> void <code>moved</code> (int dx, int dy) </p>
<h3>Public Member Functions</h3>
<p><code>QwtPanner</code> (QWidget *parent) </p>
<p> virtual <code>~QwtPanner</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setEnabled</code> (bool)<br />
 <i>En/disable the panner. </i><br />
 bool <code>isEnabled</code> () const </p>
<p> void <code>setMouseButton</code> (Qt::MouseButton, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>getMouseButton</code> (Qt::MouseButton &amp;button, Qt::KeyboardModifiers &amp;) const<br />
 <i>Get mouse button and modifiers used for panning. </i><br />
 void <code>setAbortKey</code> (int key, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>getAbortKey</code> (int &amp;key, Qt::KeyboardModifiers &amp;) const<br />
 <i>Get the abort key and modifiers. </i><br />
 void <code>setCursor</code> (const QCursor &amp;) </p>
<p> const QCursor <code>cursor</code> () const </p>
<p> void <code>setOrientations</code> (Qt::Orientations) </p>
<p> Qt::Orientations <code>orientations</code> () const<br />
 <i>Return the orientation, where paning is enabled. </i><br />
 bool <code>isOrientationEnabled</code> (Qt::Orientation) const </p>
<p> virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>widgetMousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseMoveEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetKeyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>widgetKeyReleaseEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>paintEvent</code> (QPaintEvent *)<br />
 <i>Paint event. </i><br />
 virtual QBitmap <code>contentsMask</code> () const<br />
 <i>Calculate a mask for the contents of the panned widget. </i><br />
 virtual QPixmap <code>grab</code> () const </p>
<h2>Detailed Description</h2>
<p><code>QwtPanner</code> provides panning of a widget. </p>
<p> <code>QwtPanner</code> grabs the contents of a widget, that can be dragged in all directions. The offset between the start and the end position is emitted by the panned signal. </p>
<p> <code>QwtPanner</code> grabs the content of the widget into a pixmap and moves the pixmap around, without initiating any repaint events for the widget. Areas, that are not part of content are not painted while panning. This makes panning fast enough for widgets, where repaints are too slow for mouse movements. </p>
<p> For widgets, where repaints are very fast it might be better to implement panning manually by mapping mouse events into paint events.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPanner::QwtPanner (QWidget *parent)</h3>
<p>Creates an panner that is enabled for the left mouse button. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget to be panned</dl>
<h2>Member Function Documentation</h2>
<h3>QBitmap QwtPanner::contentsMask () const [protected], [virtual]</h3>
<p>Calculate a mask for the contents of the panned widget. Sometimes only parts of the contents of a widget should be panned. F.e. for a widget with a styled background with rounded borders only the area inside of the border should be panned. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An empty bitmap, indicating no mask</dl>
<p> Reimplemented in <code>QwtPlotPanner</code>.</p>
<h3>const QCursor QwtPanner::cursor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Cursor that is active while panning</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCursor()</code></dl>
<h3>bool QwtPanner::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Event filter. When <code>isEnabled()</code> is true mouse events of the observed widget are filtered. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Always false, beside for paint events for the parent widget.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseMoveEvent()</code></dl>
<h3>QPixmap QwtPanner::grab () const [protected], [virtual]</h3>
<p>Grab the widget into a pixmap. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Grabbed pixmap</dl>
<p> Reimplemented in <code>QwtPlotPanner</code>.</p>
<h3>bool QwtPanner::isEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true when enabled, false otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setEnabled</code>, <code>eventFilter()</code></dl>
<h3>bool QwtPanner::isOrientationEnabled (Qt::Orientationo) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True if an orientation is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientations()</code>, <code>setOrientations()</code></dl>
<h3>void QwtPanner::moved (intdx, intdy) [signal]</h3>
<p>Signal emitted, while the widget moved, but panning is not finished. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dx</i> Offset in horizontal direction<br />
 <i>dy</i> Offset in vertical direction</dl>
<h3>void QwtPanner::paintEvent (QPaintEvent *pe) [protected], [virtual]</h3>
<p>Paint event. Repaint the grabbed pixmap on its current position and fill the empty spaces by the background of the parent widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pe</i> Paint event</dl>
<h3>void QwtPanner::panned (intdx, intdy) [signal]</h3>
<p>Signal emitted, when panning is done </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dx</i> Offset in horizontal direction<br />
 <i>dy</i> Offset in vertical direction</dl>
<h3>void QwtPanner::setAbortKey (intkey, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Change the abort key The defaults are Qt::Key_Escape and Qt::NoModifiers </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> Key ( See Qt::Keycode )<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<h3>void QwtPanner::setCursor (const QCursor &amp;cursor)</h3>
<p>Change the cursor, that is active while panning The default is the cursor of the parent widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cursor</i> New cursor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCursor()</code></dl>
<h3>void QwtPanner::setEnabled (boolon)</h3>
<p>En/disable the panner. When enabled is true an event filter is installed for the observed widget, otherwise the event filter is removed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true or false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isEnabled()</code>, <code>eventFilter()</code></dl>
<h3>void QwtPanner::setMouseButton (Qt::MouseButtonbutton, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Change the mouse button and modifiers used for panning The defaults are Qt::LeftButton and Qt::NoModifier</p>
<h3>void QwtPanner::setOrientations (Qt::Orientationso)</h3>
<p>Set the orientations, where panning is enabled The default value is in both directions: Qt::Horizontal | Qt::Vertical </p>
<p> /param o Orientation</p>
<h3>void QwtPanner::widgetKeyPressEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key press event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPanner::widgetKeyReleaseEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key release event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPanner::widgetMouseMoveEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse move event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code></dl>
<h3>void QwtPanner::widgetMousePressEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse press event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseMoveEvent()</code>,</dl>
<h3>void QwtPanner::widgetMouseReleaseEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse release event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseMoveEvent()</code>,</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
