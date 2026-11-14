---
title: "qwtpickerdragpointmachine(3)"
name: "qwtpickerdragpointmachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickerdragpointmachine/"
description: "QwtPickerDragPointMachine –"
---

<p>QwtPickerDragPointMachine &#8211; </p>
<p> A state machine for point selections.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherits <code>QwtPickerMachine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerDragPointMachine</code> ()<br />
 <i>Constructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)<br />
 <i>Transition. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A state machine for point selections. </p>
<p> Pressing <code>QwtEventPattern::MouseSelect1</code> or <code>QwtEventPattern::KeySelect1</code> starts the selection, releasing <code>QwtEventPattern::MouseSelect1</code> or a second press of <code>QwtEventPattern::KeySelect1</code> terminates it. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
