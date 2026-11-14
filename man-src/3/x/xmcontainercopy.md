---
title: "xmcontainercopy(3)"
name: "xmcontainercopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainercopy/"
description: "XmContainerCopy — Container widget function to copy primary selection to the clipboard"
---

<p><code>XmContainerCopy</code> &#8212; Container widget function to copy primary selection to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>Boolean XmContainerCopy</code>(
<code>Widget container</code>,
<code>Time timestamp</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerCopy</code> copies the primary selected container items to the clipboard. This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmCOPY</code>.</p>
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
