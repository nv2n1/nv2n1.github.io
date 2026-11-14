---
title: "xmcreatefileselectiondialog(3)"
name: "xmcreatefileselectiondialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatefileselectiondialog/"
description: "XmCreateFileSelectionDialog — The FileSelectionBox FileSelectionDialog convenience creation function"
---

<p><code>XmCreateFileSelectionDialog</code> &#8212; The FileSelectionBox FileSelectionDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/FileSB.h&gt;
<code>Widget XmCreateFileSelectionDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateFileSelectionDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged FileSelectionBox child of the DialogShell. A FileSelectionDialog selects a file. It includes the following:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>An editable text field for the directory mask</p>
<dt> &bull;</p>
<dd>A scrolling list of filenames</p>
<dt> &bull;</p>
<dd>An editable text field for the selected file</p>
<dt> &bull;</p>
<dd>Labels for the list and text fields</p>
<dt> &bull;</p>
<dd>Four buttons</dl>
<p> The default button labels are <code>OK</code>, <code>Filter</code>, <code>Cancel</code>, and <code>Help</code>. One additional <code>WorkArea</code> child may be added to the FileSelectionBox after creation. </p>
<p> Use <code>XtManageChild</code> to pop up the FileSelectionDialog (passing the FileSelectionBox as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateFileSelectionDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of FileSelectionBox and its associated resources, see <code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the FileSelectionBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3).</p>
