---
title: "xmvacreatemanageddrawnbutton(3)"
name: "xmvacreatemanageddrawnbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatemanageddrawnbutton/"
description: "XmVaCreateDrawnButton, XmVaCreateManagedDrawnButton — A DrawnButton widget convenience creation functions."
---

<p><code>XmVaCreateDrawnButton</code>, <code>XmVaCreateManagedDrawnButton</code> &#8212; A DrawnButton widget convenience creation functions.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DrawnB.h&gt;
<code>Widget XmVaCreateDrawnButton</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);
<code>Widget XmVaCreateManagedDrawnButton</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);</pre>
<h2>Description</h2>
<p>These functions create an instance of a DrawnButton widget and returns the associated widget ID. These routines use the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> The <code>XmVaCreateDrawnButton</code> function is a convenience routine that calls <code>XtCreateWidget</code>. </p>
<p> The <code>XmVaCreateManagedDrawnButton</code> function is a convenience routine that calls <code>XtCreateManagedWidget</code>. </p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<p> For a complete definition of DrawnButton and its associated resources, see <code><a href="/docs/linux/man/3-xmdrawnbutton/">XmDrawnButton</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the DrawnButton widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdrawnbutton/">XmDrawnButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatedrawnbutton/">XmCreateDrawnButton</a></code>(3), <code><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xtcreatemanagedwidget/">XtCreateManagedWidget</a></code>(3).</p>
