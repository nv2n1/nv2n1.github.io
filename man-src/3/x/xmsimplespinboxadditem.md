---
title: "xmsimplespinboxadditem(3)"
name: "xmsimplespinboxadditem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsimplespinboxadditem/"
description: "XmSimpleSpinBoxAddItem — add an item to the XmSimpleSpinBox"
---

<p><code>XmSimpleSpinBoxAddItem</code> &#8212; add an item to the XmSimpleSpinBox</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SSpinB.h&gt;
<code>void XmSimpleSpinBoxAddItem</code>(
<code>Widget w</code>,
<code>XmString item</code>,
<code>int pos</code>);</pre>
<h2>Description</h2>
<p>The <code>XmSimpleSpinBoxAddItem</code> function adds the given item to the XmSimpleSpinBox at the given position. </p>
<p> The <i>w</i> argument specifies the widget ID. </p>
<p> The <i>item</i> argument specifies the <code>XmString</code> for the new item. </p>
<p> The <i>pos</i> argument specifies the position of the new item.</p>
<h2>Return Value</h2>
<p>The <code>XmSimpleSpinBoxAddItem</code> function returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmsimplespinbox/">XmSimpleSpinBox</a></code>(3), </p>
<p> <code><a href="/docs/linux/man/3-xmsimplespinboxdeletepos/">XmSimpleSpinBoxDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxsetitem/">XmSimpleSpinBoxSetItem</a></code>(3).</p>
