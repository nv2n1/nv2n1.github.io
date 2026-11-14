---
title: "qwteventpattern(3)"
name: "qwteventpattern"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwteventpattern/"
description: "QwtEventPattern –"
---

<p>QwtEventPattern &#8211; </p>
<p> A collection of event patterns.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_event_pattern.h&gt; </p>
<p> Inherited by <code>QwtPicker</code>.</p>
<h3>Classes</h3>
<p>class <code>KeyPattern</code><br />
 <i>A pattern for key events. </i><br />
 class <code>MousePattern</code><br />
 <i>A pattern for mouse events. </i></p>
<h3>Public Types</h3>
<p>enum <code>MousePatternCode</code> { <code>MouseSelect1</code>, <code>MouseSelect2</code>, <code>MouseSelect3</code>, <code>MouseSelect4</code>, <code>MouseSelect5</code>, <code>MouseSelect6</code>, <code>MousePatternCount</code> }<br />
 <i>Symbolic mouse input codes. </i><br />
 enum <code>KeyPatternCode</code> { <code>KeySelect1</code>, <code>KeySelect2</code>, <code>KeyAbort</code>, <code>KeyLeft</code>, <code>KeyRight</code>, <code>KeyUp</code>, <code>KeyDown</code>, <code>KeyRedo</code>, <code>KeyUndo</code>, <code>KeyHome</code>, <code>KeyPatternCount</code> }<br />
 <i>Symbolic keyboard input codes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtEventPattern</code> () </p>
<p> virtual <code>~QwtEventPattern</code> ()<br />
 <i>Destructor. </i><br />
 void <code>initMousePattern</code> (int numButtons) </p>
<p> void <code>initKeyPattern</code> () </p>
<p> void <code>setMousePattern</code> (<code>MousePatternCode</code>, Qt::MouseButton button, Qt::KeyboardModifiers=Qt::NoModifier) </p>
<p> void <code>setKeyPattern</code> (<code>KeyPatternCode</code>, int keyCode, Qt::KeyboardModifiers modifierCodes=Qt::NoModifier) </p>
<p> void <code>setMousePattern</code> (const QVector&lt; <code>MousePattern</code> &gt; &amp;)<br />
 <i>Change the mouse event patterns. </i><br />
 void <code>setKeyPattern</code> (const QVector&lt; <code>KeyPattern</code> &gt; &amp;)<br />
 <i>Change the key event patterns. </i><br />
 const QVector&lt; <code>MousePattern</code> &gt; &amp; <code>mousePattern</code> () const </p>
<p> const QVector&lt; <code>KeyPattern</code> &gt; &amp; <code>keyPattern</code> () const </p>
<p> QVector&lt; <code>MousePattern</code> &gt; &amp; <code>mousePattern</code> () </p>
<p> QVector&lt; <code>KeyPattern</code> &gt; &amp; <code>keyPattern</code> () </p>
<p> bool <code>mouseMatch</code> (<code>MousePatternCode</code>, const QMouseEvent *) const<br />
 <i>Compare a mouse event with an event pattern. </i><br />
 bool <code>keyMatch</code> (<code>KeyPatternCode</code>, const QKeyEvent *) const<br />
 <i>Compare a key event with an event pattern. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual bool <code>mouseMatch</code> (const <code>MousePattern</code> &amp;, const QMouseEvent *) const<br />
 <i>Compare a mouse event with an event pattern. </i><br />
 virtual bool <code>keyMatch</code> (const <code>KeyPattern</code> &amp;, const QKeyEvent *) const<br />
 <i>Compare a key event with an event pattern. </i></p>
<h2>Detailed Description</h2>
<p>A collection of event patterns. </p>
<p> <code>QwtEventPattern</code> introduces an level of indirection for mouse and keyboard inputs. Those are represented by symbolic names, so the application code can be configured by individual mappings. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPicker</code>, <code>QwtPickerMachine</code>, <code>QwtPlotZoomer</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtEventPattern::KeyPatternCode</code></h3>
<p>Symbolic keyboard input codes. Individual settings can be configured using <code>setKeyPattern()</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setKeyPattern()</code>, <code>setMousePattern()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>KeySelect1 </i></p>
<dd>Qt::Key_Return.</p>
<dt><i>KeySelect2 </i></p>
<dd>Qt::Key_Space.</p>
<dt><i>KeyAbort </i></p>
<dd>Qt::Key_Escape.</p>
<dt><i>KeyLeft </i></p>
<dd>Qt::Key_Left.</p>
<dt><i>KeyRight </i></p>
<dd>Qt::Key_Right.</p>
<dt><i>KeyUp </i></p>
<dd>Qt::Key_Up.</p>
<dt><i>KeyDown </i></p>
<dd>Qt::Key_Down.</p>
<dt><i>KeyRedo </i></p>
<dd>Qt::Key_Plus.</p>
<dt><i>KeyUndo </i></p>
<dd>Qt::Key_Minus.</p>
<dt><i>KeyHome </i></p>
<dd>Qt::Key_Escape.</p>
<dt><i>KeyPatternCount </i></p>
<dd>Number of key patterns.</dl>
<h3>enum <code>QwtEventPattern::MousePatternCode</code></h3>
<p>Symbolic mouse input codes. <code>QwtEventPattern</code> implements 3 different settings for mice with 1, 2, or 3 buttons that can be activated using <code>initMousePattern()</code>. The default setting is for 3 button mice. </p>
<p> Individual settings can be configured using <code>setMousePattern()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>initMousePattern()</code>, <code>setMousePattern()</code>, <code>setKeyPattern()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>MouseSelect1 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton</p>
<dt>&bull;</p>
<dd>Qt::LeftButton</p>
<dt>&bull;</p>
<dd>Qt::LeftButton</dl>
<dl COMPACT>
<dt><i>MouseSelect2 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::ControlModifier</p>
<dt>&bull;</p>
<dd>Qt::RightButton</p>
<dt>&bull;</p>
<dd>Qt::RightButton</dl>
<dl COMPACT>
<dt><i>MouseSelect3 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::AltModifier</p>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::AltModifier</p>
<dt>&bull;</p>
<dd>Qt::MidButton</dl>
<dl COMPACT>
<dt><i>MouseSelect4 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::ShiftModifier</dl>
<dl COMPACT>
<dt><i>MouseSelect5 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::ControlButton | Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::RightButton + Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::RightButton + Qt::ShiftModifier</dl>
<dl COMPACT>
<dt><i>MouseSelect6 </i></p>
<dd>The default setting for 1, 2 and 3 button mice is:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::AltModifier + Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::LeftButton + Qt::AltModifier | Qt::ShiftModifier</p>
<dt>&bull;</p>
<dd>Qt::MidButton + Qt::ShiftModifier</dl>
<dl COMPACT>
<dt><i>MousePatternCount </i></p>
<dd>Number of mouse patterns.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtEventPattern::QwtEventPattern ()</h3>
<p>Constructor </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>MousePatternCode</code>, <code>KeyPatternCode</code></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtEventPattern::initKeyPattern ()</h3>
<p>Set default mouse patterns. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>KeyPatternCode</code></dl>
<h3>void QwtEventPattern::initMousePattern (intnumButtons)</h3>
<p>Set default mouse patterns, depending on the number of mouse buttons </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numButtons</i> Number of mouse buttons ( &lt;= 3 )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>MousePatternCode</code></dl>
<h3>bool QwtEventPattern::keyMatch (<code>KeyPatternCode</code>code, const QKeyEvent *event) const</h3>
<p>Compare a key event with an event pattern. A key event matches the pattern when both have the same key value and in the state value the same key flags (Qt::KeyButtonMask) are set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>code</i> Index of the event pattern<br />
 <i>event</i> Key event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if matches</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mouseMatch()</code></dl>
<h3>bool QwtEventPattern::keyMatch (const <code>KeyPattern</code> &amp;pattern, const QKeyEvent *event) const [protected], [virtual]</h3>
<p>Compare a key event with an event pattern. A key event matches the pattern when both have the same key value and in the state value the same key flags (Qt::KeyButtonMask) are set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pattern</i> Key event pattern<br />
 <i>event</i> Key event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if matches</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mouseMatch()</code></dl>
<h3>const QVector&lt; <code>QwtEventPattern::KeyPattern</code> &gt; &amp; QwtEventPattern::keyPattern () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Key pattern</dl>
<h3>QVector&lt; <code>QwtEventPattern::KeyPattern</code> &gt; &amp; QwtEventPattern::keyPattern ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Key pattern</dl>
<h3>bool QwtEventPattern::mouseMatch (<code>MousePatternCode</code>code, const QMouseEvent *event) const</h3>
<p>Compare a mouse event with an event pattern. A mouse event matches the pattern when both have the same button value and in the state value the same key flags(Qt::KeyButtonMask) are set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>code</i> Index of the event pattern<br />
 <i>event</i> Mouse event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if matches</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>keyMatch()</code></dl>
<h3>bool QwtEventPattern::mouseMatch (const <code>MousePattern</code> &amp;pattern, const QMouseEvent *event) const [protected], [virtual]</h3>
<p>Compare a mouse event with an event pattern. A mouse event matches the pattern when both have the same button value and in the state value the same key flags(Qt::KeyButtonMask) are set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pattern</i> Mouse event pattern<br />
 <i>event</i> Mouse event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if matches</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>keyMatch()</code></dl>
<h3>const QVector&lt; <code>QwtEventPattern::MousePattern</code> &gt; &amp; QwtEventPattern::mousePattern () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mouse pattern</dl>
<h3>QVector&lt; <code>QwtEventPattern::MousePattern</code> &gt; &amp; QwtEventPattern::mousePattern ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mouse pattern</dl>
<h3>void QwtEventPattern::setKeyPattern (<code>KeyPatternCode</code>pattern, intkey, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Change one key pattern </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pattern</i> Index of the pattern<br />
 <i>key</i> Key<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QKeyEvent</dl>
<h3>void QwtEventPattern::setMousePattern (<code>MousePatternCode</code>pattern, Qt::MouseButtonbutton, Qt::KeyboardModifiersmodifiers = Qt::NoModifier)</h3>
<p>Change one mouse pattern </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pattern</i> Index of the pattern<br />
 <i>button</i> Button<br />
 <i>modifiers</i> Keyboard modifiers</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QMouseEvent</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
