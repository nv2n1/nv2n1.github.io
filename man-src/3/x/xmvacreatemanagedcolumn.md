---
title: "xmvacreatemanagedcolumn(3)"
name: "xmvacreatemanagedcolumn"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatemanagedcolumn/"
description: "XmVaCreateColumn, XmVaCreateManagedColumn — A Column widget convenience creation functions."
---

<p><code>XmVaCreateColumn</code>, <code>XmVaCreateManagedColumn</code> &#8212; A Column widget convenience creation functions.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Column.h&gt;
<code>Widget XmVaCreateColumn</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);
<code>Widget XmVaCreateManagedColumn</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);</pre>
<h2>Description</h2>
<p>These functions create an instance of a Column widget and returns the associated widget ID. These routines use the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> The <code>XmVaCreateColumn</code> function is a convenience routine that calls <code>XtCreateWidget</code>. </p>
<p> The <code>XmVaCreateManagedColumn</code> function is a convenience routine that calls <code>XtCreateManagedWidget</code>. </p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<p> For a complete definition of Column and its associated resources, see <code><a href="/docs/linux/man/3-xmcolumn/">XmColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Column widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcolumn/">XmColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecolumn/">XmCreateColumn</a></code>(3), <code><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xtcreatemanagedwidget/">XtCreateManagedWidget</a></code>(3).</p>
