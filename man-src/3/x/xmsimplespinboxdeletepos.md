---
title: "xmsimplespinboxdeletepos(3)"
name: "xmsimplespinboxdeletepos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsimplespinboxdeletepos/"
description: "XmSimpleSpinBoxDeletePos — delete a XmSimpleSpinBox item"
---

<p><code>XmSimpleSpinBoxDeletePos</code> &#8212; delete a XmSimpleSpinBox item</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SpinB.h&gt;
<code>void XmSimpleSpinBoxDeletePos</code>(
<code>Widget w</code>,
<code>int pos</code>);</pre>
<h2>Description</h2>
<p>The <code>XmSimpleSpinBoxDeletePos</code> function deletes a specified item from a XmSimpleSpinBox widget. </p>
<p> The <i>w</i> argument specifies the widget ID. </p>
<p> The <i>pos</i> argument specifies the position of the item to be deleted. A value of 1 means the first item in the list; zero means the last item.</p>
<h2>Return Value</h2>
<p>The <code>XmSimpleSpinBoxDeletePos</code> function returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmsimplespinbox/">XmSimpleSpinBox</a></code>(3), </p>
<p> <code><a href="/docs/linux/man/3-xmsimplespinboxadditem/">XmSimpleSpinBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxsetitem/">XmSimpleSpinBoxSetItem</a></code>(3).</p>
