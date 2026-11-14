---
title: "xmcreateformdialog(3)"
name: "xmcreateformdialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateformdialog/"
description: "XmCreateFormDialog — A Form FormDialog convenience creation function"
---

<p><code>XmCreateFormDialog</code> &#8212; A Form FormDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Form.h&gt;
<code>Widget XmCreateFormDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateFormDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged Form child of the DialogShell. A FormDialog is used for interactions not supported by the standard dialog set. This function does not automatically create any labels, buttons, or other dialog components. Such components should be added by the application after the FormDialog is created. </p>
<p> Use <code>XtManageChild</code> to pop up the FormDialog (passing the Form as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateFormDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of Form and its associated resources, see <code><a href="/docs/linux/man/3-xmform/">XmForm</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Form widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmform/">XmForm</a></code>(3).</p>
