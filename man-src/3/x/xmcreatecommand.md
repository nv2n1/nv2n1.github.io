---
title: "xmcreatecommand(3)"
name: "xmcreatecommand"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatecommand/"
description: "XmCreateCommand — The Command widget creation function"
---

<p><code>XmCreateCommand</code> &#8212; The Command widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Command.h&gt;
<code>Widget XmCreateCommand</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateCommand</code> creates an instance of a Command widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of Command and its associated resources, see <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Command widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
