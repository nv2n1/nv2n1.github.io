---
title: "xmvacreatedropdown(3)"
name: "xmvacreatedropdown"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatedropdown/"
description: "XmVaCreateDropDown, XmVaCreateManagedDropDown — A DropDown widget convenience creation functions."
---

<p><code>XmVaCreateDropDown</code>, <code>XmVaCreateManagedDropDown</code> &#8212; A DropDown widget convenience creation functions.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DropDown.h&gt;
<code>Widget XmVaCreateDropDown</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);
<code>Widget XmVaCreateManagedDropDown</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);</pre>
<h2>Description</h2>
<p>These functions create an instance of a DropDown widget and returns the associated widget ID. These routines use the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> The <code>XmVaCreateDropDown</code> function is a convenience routine that calls <code>XtCreateWidget</code>. </p>
<p> The <code>XmVaCreateManagedDropDown</code> function is a convenience routine that calls <code>XtCreateManagedWidget</code>. </p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID.</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget.</dd>
<dt><i>&#8230;</i></dt>
<dd>Specifies the variable argument list to override the resource defaults.</dd></dl>
<p> For a complete definition of DropDown and its associated resources, see <code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the DropDown widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatedropdown/">XmCreateDropDown</a></code>(3), <code><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xtcreatemanagedwidget/">XtCreateManagedWidget</a></code>(3).</p>
