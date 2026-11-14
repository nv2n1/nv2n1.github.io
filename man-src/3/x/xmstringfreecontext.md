---
title: "xmstringfreecontext(3)"
name: "xmstringfreecontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringfreecontext/"
description: "XmStringFreeContext — A compound string function that releases the string scanning context data structure"
---

<p><code>XmStringFreeContext</code> &#8212; A compound string function that releases the string scanning context data structure</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmStringFreeContext</code>(
<code>XmStringContext context</code>);</pre>
<h2>Description</h2>
<p><code>XmStringFreeContext</code> releases the string scanning context data structure.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure that was allocated by the <code>XmStringInitContext</code> function</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringinitcontext/">XmStringInitContext</a></code>(3).</p>
