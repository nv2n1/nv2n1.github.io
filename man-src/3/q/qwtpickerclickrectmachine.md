---
title: "qwtpickerclickrectmachine(3)"
name: "qwtpickerclickrectmachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickerclickrectmachine/"
description: "QwtPickerClickRectMachine –"
---

<p>QwtPickerClickRectMachine &#8211; </p>
<p> A state machine for rectangle selections.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherits <code>QwtPickerMachine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerClickRectMachine</code> ()<br />
 <i>Constructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)<br />
 <i>Transition. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A state machine for rectangle selections. </p>
<p> Pressing <code>QwtEventPattern::MouseSelect1</code> starts the selection, releasing it selects the first point. Pressing it again selects the second point and terminates the selection. Pressing <code>QwtEventPattern::KeySelect1</code> also starts the selection, a second press selects the first point. A third one selects the second point and terminates the selection. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtEventPattern::MousePatternCode</code>, <code>QwtEventPattern::KeyPatternCode</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
