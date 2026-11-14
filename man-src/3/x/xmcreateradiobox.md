---
title: "xmcreateradiobox(3)"
name: "xmcreateradiobox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateradiobox/"
description: "XmCreateRadioBox — A RowColumn widget convenience creation function"
---

<p><code>XmCreateRadioBox</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateRadioBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateRadioBox</code> creates an instance of a RowColumn widget of type <code>XmWORK_AREA</code> and returns the associated widget ID. Typically, this is a composite widget that contains multiple ToggleButtonGadgets. The RadioBox arbitrates and ensures that at most one ToggleButtonGadget is on at any time. </p>
<p> Unless the application supplies other values in the <i>arglist</i>, this function provides initial values for several RowColumn resources. It initializes <code>XmNpacking</code> to <code>XmPACK_COLUMN</code>, <code>XmNradioBehavior</code> to True, <code>XmNisHomogeneous</code> to True, and <code>XmNentryClass</code> to <code>XmToggleButtonGadgetClass</code>. </p>
<p> In a RadioBox, the ToggleButton or ToggleButtonGadget resource <code>XmNindicatorType</code> defaults to <code>XmONE_OF_MANY</code>, and the ToggleButton or ToggleButtonGadget resource<code>XmNvisibleWhenOff</code> defaults to True. </p>
<p> This routine is provided as a convenience function for creating RowColumn widgets.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplecheckbox/">XmCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateworkarea/">XmCreateWorkArea</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleradiobox/">XmVaCreateSimpleRadioBox</a></code>(3).</p>
