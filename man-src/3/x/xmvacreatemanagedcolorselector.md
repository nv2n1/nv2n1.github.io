---
title: "xmvacreatemanagedcolorselector(3)"
name: "xmvacreatemanagedcolorselector"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatemanagedcolorselector/"
description: "XmVaCreateColorSelector, XmVaCreateManagedColorSelector — A ColorSelector widget convenience creation functions."
---

<p><code>XmVaCreateColorSelector</code>, <code>XmVaCreateManagedColorSelector</code> &#8212; A ColorSelector widget convenience creation functions.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ColorS.h&gt;
<code>Widget XmVaCreateColorSelector</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);
<code>Widget XmVaCreateManagedColorSelector</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);</pre>
<h2>Description</h2>
<p>These functions create an instance of a ColorSelector widget and returns the associated widget ID. These routines use the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> The <code>XmVaCreateColorSelector</code> function is a convenience routine that calls <code>XtCreateWidget</code>. </p>
<p> The <code>XmVaCreatemanagedColorSelector</code> function is a convenience routine that calls <code>XtCreateManagedWidget</code>. </p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<p> For a complete definition of ColorSelector and its associated resources, see <code><a href="/docs/linux/man/3-xmcolorselector/">XmColorSelector</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ColorSelector widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcolorselector/">XmColorSelector</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecolorselector/">XmCreateColorSelector</a></code>(3), <code><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xtcreatemanagedwidget/">XtCreateManagedWidget</a></code>(3).</p>
