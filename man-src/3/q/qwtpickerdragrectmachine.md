---
title: "qwtpickerdragrectmachine(3)"
name: "qwtpickerdragrectmachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickerdragrectmachine/"
description: "QwtPickerDragRectMachine –"
---

<p>QwtPickerDragRectMachine &#8211; </p>
<p> A state machine for rectangle selections.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherits <code>QwtPickerMachine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerDragRectMachine</code> ()<br />
 <i>Constructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)<br />
 <i>Transition. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A state machine for rectangle selections. </p>
<p> Pressing <code>QwtEventPattern::MouseSelect1</code> selects the first point, releasing it the second point. Pressing <code>QwtEventPattern::KeySelect1</code> also selects the first point, a second press selects the second point and terminates the selection. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtEventPattern::MousePatternCode</code>, <code>QwtEventPattern::KeyPatternCode</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
