---
title: "qwtpickermachine(3)"
name: "qwtpickermachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickermachine/"
description: "QwtPickerMachine –"
---

<p>QwtPickerMachine &#8211; </p>
<p> A state machine for <code>QwtPicker</code> selections.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherited by <code>QwtPickerClickPointMachine</code>, <code>QwtPickerClickRectMachine</code>, <code>QwtPickerDragLineMachine</code>, <code>QwtPickerDragPointMachine</code>, <code>QwtPickerDragRectMachine</code>, <code>QwtPickerPolygonMachine</code>, and <code>QwtPickerTrackerMachine</code>.</p>
<h3>Public Types</h3>
<p>enum <code>SelectionType</code> { <code>NoSelection</code> = -1, <code>PointSelection</code>, <code>RectSelection</code>, <code>PolygonSelection</code> } </p>
<p> enum <code>Command</code> { <code>Begin</code>, <code>Append</code>, <code>Move</code>, <code>Remove</code>, <code>End</code> }<br />
 <i>Commands &#8211; the output of a state machine. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerMachine</code> (<code>SelectionType</code>)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPickerMachine</code> ()<br />
 <i>Destructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)=0<br />
 <i>Transition. </i><br />
 void <code>reset</code> ()<br />
 <i>Set the current state to 0. </i><br />
 int <code>state</code> () const<br />
 <i>Return the current state. </i><br />
 void <code>setState</code> (int)<br />
 <i>Change the current state. </i><br />
 <code>SelectionType</code> <code>selectionType</code> () const<br />
 <i>Return the selection type. </i></p>
<h2>Detailed Description</h2>
<p>A state machine for <code>QwtPicker</code> selections. </p>
<p> <code>QwtPickerMachine</code> accepts key and mouse events and translates them into selection commands. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtEventPattern::MousePatternCode</code>, <code>QwtEventPattern::KeyPatternCode</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPickerMachine::SelectionType</code></h3>
<p>Type of a selection. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>selectionType()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoSelection </i></p>
<dd>The state machine not usable for any type of selection.</p>
<dt><i>PointSelection </i></p>
<dd>The state machine is for selecting a single point.</p>
<dt><i>RectSelection </i></p>
<dd>The state machine is for selecting a rectangle (2 points).</p>
<dt><i>PolygonSelection </i></p>
<dd>The state machine is for selecting a polygon (many points). </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
