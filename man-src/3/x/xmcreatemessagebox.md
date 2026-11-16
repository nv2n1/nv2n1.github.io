---
title: "xmcreatemessagebox(3)"
name: "xmcreatemessagebox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatemessagebox/"
description: "XmCreateMessageBox — The MessageBox widget creation function"
---

<p><code>XmCreateMessageBox</code> &#8212; The MessageBox widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MessageB.h&gt;
<code>Widget XmCreateMessageBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateMessageBox</code> creates an unmanaged MessageBox. A MessageBox is used for common interaction tasks, which include giving information, asking questions, and reporting errors. It includes an optional symbol, a message, and three buttons. </p>
<p> By default, there is no symbol. The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. </p>
<p> If the parent of the MessageBox is a DialogShell, use <code>XtManageChild</code> to pop up the MessageBox (passing the MessageBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down.</p>
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
