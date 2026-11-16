---
title: "xmcreateinformationdialog(3)"
name: "xmcreateinformationdialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateinformationdialog/"
description: "XmCreateInformationDialog — The MessageBox InformationDialog convenience creation function"
---

<p><code>XmCreateInformationDialog</code> &#8212; The MessageBox InformationDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MessageB.h&gt;
<code>Widget XmCreateInformationDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateInformationDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged MessageBox child of the DialogShell. An InformationDialog gives the user information, such as the status of an action. It includes a symbol, a message, and three buttons. The default symbol is <code>i</code>. The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. </p>
<p> Use <code>XtManageChild</code> to pop up the InformationDialog (passing the MessageBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateInformationDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of MessageBox and its associated resources, see <code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the MessageBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
