---
title: "xmcreatesimplespinbox(3)"
name: "xmcreatesimplespinbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatesimplespinbox/"
description: "XmCreateSimpleSpinBox — the SimpleSpinBox widget creation function"
---

<p><code>XmCreateSimpleSpinBox</code> &#8212; the SimpleSpinBox widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SSpinB.h&gt;
<code>Widget XmCreateSimpleSpinBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p>The <code>XmCreateSimpleSpinBox</code> function creates an instance of a SpinBox widget and returns the associated widget ID. </p>
<p> The <i>parent</i> argument specifies the parent widget ID. </p>
<p> The <i>name</i> argument specifies the name of the created widget. </p>
<p> The <i>arglist</i> argument specifies the argument list. </p>
<p> The <i>argcount</i> argument specifies the number of attribute/value pairs in the argument list.</p>
<h2>Return Value</h2>
<p>Upon successful completion, the <code>XmCreateSimpleSpinBox</code> function returns the SimpleSpinBox widget ID.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmsimplespinbox/">XmSimpleSpinBox</a></code>(3).</p>
