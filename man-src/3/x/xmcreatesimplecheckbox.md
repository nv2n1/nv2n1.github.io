---
title: "xmcreatesimplecheckbox(3)"
name: "xmcreatesimplecheckbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatesimplecheckbox/"
description: "XmCreateSimpleCheckBox — A RowColumn widget convenience creation function"
---

<p><code>XmCreateSimpleCheckBox</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateSimpleCheckBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateSimpleCheckBox</code> creates an instance of a RowColumn widget of type <code>XmWORK_AREA</code> and returns the associated widget ID. </p>
<p> This routine creates a CheckBox and its ToggleButtonGadget children. A CheckBox is similar to a RadioBox, except that more than one button can be selected at a time. The name of each button is <code>button_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of buttons in the menu minus 1. Buttons are named and created in the order they are specified in the RowColumn simple menu creation resources supplied in the argument list.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> A number of resources exist specifically for use with this and other simple menu creation routines. The only button type allowed in the <code>XmNbuttonType</code> resource is <code>XmCHECKBUTTON</code>. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleradiobox/">XmVaCreateSimpleRadioBox</a></code>(3).</p>
