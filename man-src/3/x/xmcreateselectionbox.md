---
title: "xmcreateselectionbox(3)"
name: "xmcreateselectionbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateselectionbox/"
description: "XmCreateSelectionBox — The SelectionBox widget creation function"
---

<p><code>XmCreateSelectionBox</code> &#8212; The SelectionBox widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SelectioB.h&gt;
<code>Widget XmCreateSelectionBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateSelectionBox</code> creates an unmanaged SelectionBox. A SelectionBox is used to get a selection from a list of alternatives from the user and includes the following:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd>A scrolling list of alternatives</dd>
<dt> &bull;</dt>
<dd>An editable text field for the selected alternative</dd>
<dt> &bull;</dt>
<dd>Labels for the list and text field</dd>
<dt> &bull;</dt>
<dd>Three or four buttons</dd></dl>
<p> The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. By default, an <code>Apply</code> button is also created. If the parent of the SelectionBox is a DialogShell, it is managed; otherwise it is unmanaged. Additional work area children may be added to the SelectionBox after creation.</p>
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
