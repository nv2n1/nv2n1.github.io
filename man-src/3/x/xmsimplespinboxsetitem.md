---
title: "xmsimplespinboxsetitem(3)"
name: "xmsimplespinboxsetitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsimplespinboxsetitem/"
description: "XmSimpleSpinBoxSetItem — set an item in the XmSimpleSpinBox list"
---

<p><code>XmSimpleSpinBoxSetItem</code> &#8212; set an item in the XmSimpleSpinBox list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SpinB.h&gt;
<code>void XmSimpleSpinBoxSetItem</code>(
<code>Widget w</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p>The <code>XmSimpleSpinBoxSetItem</code> function selects an item in the list of the given XmSimpleSpinBox widget and makes it the current value. </p>
<p> The <i>w</i> argument specifies the widget ID. </p>
<p> The <i>item</i> argument specifies the <code>XmString</code> for the item to be set in the XmSimpleSpinBox. If the <i>item</i> is not found on the list, <code>XmSimpleSpinBoxSetItem</code> notifies the user via the <code>XtWarning</code> function.</p>
<h2>Return Value</h2>
<p>The <code>XmSimpleSpinBoxSetItem</code> function returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmsimplespinbox/">XmSimpleSpinBox</a></code>(3), </p>
<p> <code><a href="/docs/linux/man/3-xmsimplespinboxadditem/">XmSimpleSpinBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxdeletepos/">XmSimpleSpinBoxDeletePos</a></code>(3); <code><a href="/docs/linux/man/3-xtwarning/">XtWarning</a></code>(3). in the CAE Specification, Window Management: X Toolkit Intrinsics.</p>
