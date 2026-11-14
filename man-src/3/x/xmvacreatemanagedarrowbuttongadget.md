---
title: "xmvacreatemanagedarrowbuttongadget(3)"
name: "xmvacreatemanagedarrowbuttongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatemanagedarrowbuttongadget/"
description: "XmVaCreateArrowButtonGadget, XmVaCreateManagedArrowButtonGadget — A ArrowButtonGadget widget convenience creation functions."
---

<p><code>XmVaCreateArrowButtonGadget</code>, <code>XmVaCreateManagedArrowButtonGadget</code> &#8212; A ArrowButtonGadget widget convenience creation functions.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ArrowBG.h&gt;
<code>Widget XmVaCreateArrowButtonGadget</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);
<code>Widget XmVaCreateManagedArrowButtonGadget</code>(
<code>Widget parent</code>,
<code>String name</code>,
...);</pre>
<h2>Description</h2>
<p>These functions create an instance of a ArrowButtonGadget widget and returns the associated widget ID. These routines use the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> The <code>XmVaCreateArrowButtonGadget</code> function is a convenience routine that calls <code>XtCreateWidget</code>. </p>
<p> The <code>XmVaCreateManagedArrowButtonGadget</code> function is a convenience routine that calls <code>XtCreateManagedWidget</code>. </p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<p> For a complete definition of ArrowButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ArrowButtonGadget widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatearrowbuttongadget/">XmCreateArrowButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xtcreatemanagedwidget/">XtCreateManagedWidget</a></code>(3).</p>
