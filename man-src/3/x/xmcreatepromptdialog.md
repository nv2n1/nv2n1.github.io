---
title: "xmcreatepromptdialog(3)"
name: "xmcreatepromptdialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatepromptdialog/"
description: "XmCreatePromptDialog — The SelectionBox PromptDialog convenience creation function"
---

<p><code>XmCreatePromptDialog</code> &#8212; The SelectionBox PromptDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SelectioB.h&gt;
<code>Widget XmCreatePromptDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreatePromptDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged SelectionBox child of the DialogShell. A PromptDialog prompts the user for text input. It includes a message, a text input region, and three managed buttons. The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. An additional button, with <code>Apply</code> as the default label, is created unmanaged; it may be explicitly managed if needed. One additional <code>WorkArea</code> child may be added to the SelectionBox after creation. </p>
<p> <code>XmCreatePromptDialog</code> forces the value of the SelectionBox resource <code>XmNdialogType</code> to <code>XmDIALOG_PROMPT</code>. </p>
<p> Use <code>XtManageChild</code> to pop up the PromptDialog (passing the SelectionBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreatePromptDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of SelectionBox and its associated resources, see <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the SelectionBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
