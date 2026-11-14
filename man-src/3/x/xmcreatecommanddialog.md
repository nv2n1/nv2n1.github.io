---
title: "xmcreatecommanddialog(3)"
name: "xmcreatecommanddialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatecommanddialog/"
description: "XmCreateCommandDialog — The Command CommandDialog convenience creation function"
---

<p><code>XmCreateCommandDialog</code> &#8212; The Command CommandDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Command.h&gt;
<code>Widget XmCreateCommandDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateCommandDialog</code> is a convenience function that creates a DialogShell and an unmanaged Command child of the DialogShell. A CommandDialog is used for entering commands for processing. </p>
<p> Use <code>XtManageChild</code> to pop up the CommandDialog (passing the Command as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateCommandDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of Command and its associated resources, see <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Command widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
