---
title: "xmcreateselectiondialog(3)"
name: "xmcreateselectiondialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateselectiondialog/"
description: "XmCreateSelectionDialog — The SelectionBox SelectionDialog convenience creation function"
---

<p><code>XmCreateSelectionDialog</code> &#8212; The SelectionBox SelectionDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SelectioB.h&gt;
<code>Widget XmCreateSelectionDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateSelectionDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged SelectionBox child of the DialogShell. A SelectionDialog offers the user a choice from a list of alternatives and gets a selection. It includes the following:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd>A scrolling list of alternatives</dd>
<dt> &bull;</dt>
<dd>An editable text field for the selected alternative</dd>
<dt> &bull;</dt>
<dd>Labels for the text field</dd>
<dt> &bull;</dt>
<dd>Four buttons</dd></dl>
<p> The default button labels are <code>OK</code>, <code>Cancel</code>, <code>Apply</code>, and <code>Help</code>. One additional <code>WorkArea</code> child may be added to the SelectionBox after creation. </p>
<p> <code>XmCreateSelectionDialog</code> forces the value of the SelectionBox resource <code>XmNdialogType</code> to <code>XmDIALOG_SELECTION</code>. </p>
<p> <code>XmCreateSelectionDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True. </p>
<p> Use <code>XtManageChild</code> to pop up the SelectionDialog (passing the SelectionBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of SelectionBox and its associated resources, see <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the SelectionBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
