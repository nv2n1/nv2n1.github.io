---
title: "xmcreateseparator(3)"
name: "xmcreateseparator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateseparator/"
description: "XmCreateSeparator — The Separator widget creation function"
---

<p><code>XmCreateSeparator</code> &#8212; The Separator widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Separator.h&gt;
<code>Widget XmCreateSeparator</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateSeparator</code> creates an instance of a Separator widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of Separator and its associated resources, see <code><a href="/docs/linux/man/3-xmseparator/">XmSeparator</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Separator widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmseparator/">XmSeparator</a></code>(3).</p>
