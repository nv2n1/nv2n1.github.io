---
title: "xmcreateworkarea(3)"
name: "xmcreateworkarea"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateworkarea/"
description: "XmCreateWorkArea — A function that creates a RowColumn WorkArea"
---

<p><code>XmCreateWorkArea</code> &#8212; A function that creates a RowColumn WorkArea</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateWorkArea</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateWorkArea</code> creates an instance of a RowColumn widget and returns the associated widget ID. The widget is created with <code>XmNrowColumnType</code> set to <code>XmWORK_AREA</code>.</p>
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
<p><code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplecheckbox/">XmCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleradiobox/">XmVaCreateSimpleRadioBox</a></code>(3).</p>
