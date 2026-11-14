---
title: "xmstringinitcontext(3)"
name: "xmstringinitcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringinitcontext/"
description: "XmStringInitContext — A compound string function that creates a data structure for scanning an XmString component by component"
---

<p><code>XmStringInitContext</code> &#8212; A compound string function that creates a data structure for scanning an XmString component by component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringInitContext</code>(
<code>XmStringContext * context</code>,
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringInitContext</code> creates a context to allow applications to read out the contents of a compound string component by component. A Boolean status is returned to indicate that the context could not be initalized. </p>
<p> If the function returns True, the function will allocate space to hold the returned <i>context</i>. The application is responsible for managing the allocated space. The memory can be recovered by calling <code>XmStringFreeContext</code>.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies a pointer to the allocated context</p>
<dt><i>string</i></p>
<dd>Specifies the string</dl>
<h2>Return</h2>
<p>Returns True if the context was allocated</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
