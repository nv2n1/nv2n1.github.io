---
title: "xmcontainercopylink(3)"
name: "xmcontainercopylink"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainercopylink/"
description: "XmContainerCopyLink — Container widget function to copy links to the clipboard"
---

<p><code>XmContainerCopyLink</code> &#8212; Container widget function to copy links to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>Boolean XmContainerCopyLink</code>(
<code>Widget container</code>,
<code>Time timestamp</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerCopyLink</code> copies links to the primary selected items to the clipboard. This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmLINK</code>. The Container widget itself does not copy any links; <code>XmNconvertCallback</code> procedures are responsible for copying the link to the clipboard and for taking any related actions.</p>
<dl COMPACT>
<dt><i>container</i></p>
<dd>Specifies the Container widget ID.</p>
<dt><i>timestamp</i></p>
<dd>Specifies the server time at which to modify the selection value.</dl>
<p> For a complete definition of Container and its associated resources, see <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
<h2>Return</h2>
<p>The function returns False in the following cases: if the primary selection is NULL, if the widget does not own the primary selection, or if the function is unable to gain ownership of the clipboard selection. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
