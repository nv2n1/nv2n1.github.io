---
title: "xmcreateworkingdialog(3)"
name: "xmcreateworkingdialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateworkingdialog/"
description: "XmCreateWorkingDialog — The MessageBox WorkingDialog convenience creation function"
---

<p><code>XmCreateWorkingDialog</code> &#8212; The MessageBox WorkingDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MessageB.h&gt;
<code>Widget XmCreateWorkingDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateWorkingDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged MessageBox child of the DialogShell. A WorkingDialog informs users that there is a time-consuming operation in progress and allows them to cancel the operation. It includes a symbol, a message, and three buttons. The default symbol is an hourglass. The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. </p>
<p> Use <code>XtManageChild</code> to pop up the WorkingDialog (passing the MessageBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateWorkingDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of MessageBox and its associated resources, see <code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the MessageBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
