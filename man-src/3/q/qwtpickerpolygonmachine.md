---
title: "qwtpickerpolygonmachine(3)"
name: "qwtpickerpolygonmachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickerpolygonmachine/"
description: "QwtPickerPolygonMachine –"
---

<p>QwtPickerPolygonMachine &#8211; </p>
<p> A state machine for polygon selections.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherits <code>QwtPickerMachine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerPolygonMachine</code> ()<br />
 <i>Constructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)<br />
 <i>Transition. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A state machine for polygon selections. </p>
<p> Pressing <code>QwtEventPattern::MouseSelect1</code> or <code>QwtEventPattern::KeySelect1</code> starts the selection and selects the first point, or appends a point. Pressing <code>QwtEventPattern::MouseSelect2</code> or <code>QwtEventPattern::KeySelect2</code> appends the last point and terminates the selection. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtEventPattern::MousePatternCode</code>, <code>QwtEventPattern::KeyPatternCode</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
