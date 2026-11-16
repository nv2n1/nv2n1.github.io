---
title: "xmcommandgetchild(3)"
name: "xmcommandgetchild"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcommandgetchild/"
description: "XmCommandGetChild — A Command function that is used to access a component"
---

<p><code>XmCommandGetChild</code> &#8212; A Command function that is used to access a component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Command.h&gt;
<code>Widget XmCommandGetChild</code>(
<code>Widget widget</code>,
<code>unsigned char child</code>);</pre>
<h2>Description</h2>
<p><code>XmCommandGetChild</code> is used to access a component within a Command. The parameters given to the function are the Command widget and a value indicating which component to access.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Command widget ID.</dd>
<dt><i>child</i></dt>
<dd>Specifies a component within the Command. The following values are legal for this parameter:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> &bull;</dt>
<dd><code>XmDIALOG_COMMAND_TEXT</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_PROMPT_LABEL</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_HISTORY_LIST</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_WORK_AREA</code></dd></dl>
</dl>
</dl>
<p> For a complete definition of Command and its associated resources, see <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the specified Command component. An application should not assume that the returned widget will be of any particular class.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3).</p>
