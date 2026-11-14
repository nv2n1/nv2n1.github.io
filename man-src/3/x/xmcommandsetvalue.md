---
title: "xmcommandsetvalue(3)"
name: "xmcommandsetvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcommandsetvalue/"
description: "XmCommandSetValue — A Command function that replaces a displayed string"
---

<p><code>XmCommandSetValue</code> &#8212; A Command function that replaces a displayed string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Command.h&gt;
<code>void XmCommandSetValue</code>(
<code>Widget widget</code>,
<code>XmString command</code>);</pre>
<h2>Description</h2>
<p><code>XmCommandSetValue</code> replaces the string displayed in the command area of the Command widget with the passed <code>XmString</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Command widget ID</p>
<dt><i>command</i></p>
<dd>Specifies the passed <code>XmString</code></dl>
<p> For a complete definition of Command and its associated resources, see <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
