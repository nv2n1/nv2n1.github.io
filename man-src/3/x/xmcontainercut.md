---
title: "xmcontainercut(3)"
name: "xmcontainercut"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainercut/"
description: "XmContainerCut — Container widget function to move items to the clipboard"
---

<p><code>XmContainerCut</code> &#8212; Container widget function to move items to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>Boolean XmContainerCut</code>(
<code>Widget container</code>,
<code>Time timestamp</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerCut</code> cuts the primary selected items to the clipboard. This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmMOVE</code>. If the transfer is successful, this routine then calls the <code>XmNconvertCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>DELETE</code> target.</p>
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
