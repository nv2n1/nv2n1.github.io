---
title: "xmcreatetemplatedialog(3)"
name: "xmcreatetemplatedialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatetemplatedialog/"
description: "XmCreateTemplateDialog — A MessageBox TemplateDialog convenience creation function"
---

<p><code>XmCreateTemplateDialog</code> &#8212; A MessageBox TemplateDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MessageB.h&gt;
<code>Widget XmCreateTemplateDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateTemplateDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged MessageBox child of the DialogShell. The MessageBox widget&#8217;s <code>XmNdialogType</code> resource is set to <code>XmDIALOG_TEMPLATE</code>. By default, the TemplateDialog widget contains only the separator child. You can build a customized dialog by adding children to the TemplateDialog. </p>
<p> You can create the standard MessageBox pushbuttons, <code>Cancel</code>, <code>Help</code>, and <code>OK</code>, by specifying the associated callback and label string resources. Setting <code>XmNsymbolPixmap</code> or <code>XmNmessageString</code> creates a symbol or message label. </p>
<p> Use <code>XtManageChild</code> to pop up the TemplateDialog (passing the MessageBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateTemplateDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
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
