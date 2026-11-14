---
title: "qwtpickertrackermachine(3)"
name: "qwtpickertrackermachine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpickertrackermachine/"
description: "QwtPickerTrackerMachine –"
---

<p>QwtPickerTrackerMachine &#8211; </p>
<p> A state machine for indicating mouse movements.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker_machine.h&gt; </p>
<p> Inherits <code>QwtPickerMachine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPickerTrackerMachine</code> ()<br />
 <i>Constructor. </i><br />
 virtual QList&lt; <code>Command</code> &gt; <code>transition</code> (const <code>QwtEventPattern</code> &amp;, const QEvent *)<br />
 <i>Transition. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A state machine for indicating mouse movements. </p>
<p> <code>QwtPickerTrackerMachine</code> supports displaying information corresponding to mouse movements, but is not intended for selecting anything. Begin/End are related to Enter/Leave events. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
