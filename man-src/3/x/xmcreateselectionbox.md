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
<dt> &bull;</p>
<dd>A scrolling list of alternatives</p>
<dt> &bull;</p>
<dd>An editable text field for the selected alternative</p>
<dt> &bull;</p>
<dd>Labels for the list and text field</p>
<dt> &bull;</p>
<dd>Three or four buttons</dl>
<p> The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. By default, an <code>Apply</code> button is also created. If the parent of the SelectionBox is a DialogShell, it is managed; otherwise it is unmanaged. Additional work area children may be added to the SelectionBox after creation.</p>
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
