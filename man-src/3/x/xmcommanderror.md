---
title: "xmcommanderror(3)"
name: "xmcommanderror"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcommanderror/"
description: "XmCommandError — A Command function that displays an error message"
---

<p><code>XmCommandError</code> &#8212; A Command function that displays an error message</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Command.h&gt;
<code>void XmCommandError</code>(
<code>Widget widget</code>,
<code>XmString error</code>);</pre>
<h2>Description</h2>
<p><code>XmCommandError</code> displays an error message in the history area of the Command widget. The <code>XmString</code> error is displayed until the next command entered occurs.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Command widget ID</p>
<dt><i>error</i></p>
<dd>Specifies the passed <code>XmString</code></dl>
<p> For a complete definition of Command and its associated resources, see <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
