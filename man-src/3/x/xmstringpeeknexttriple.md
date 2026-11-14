---
title: "xmstringpeeknexttriple(3)"
name: "xmstringpeeknexttriple"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringpeeknexttriple/"
description: "XmStringPeekNextTriple — A function that returns the component type of the next component"
---

<p><code>XmStringPeekNextTriple</code> &#8212; A function that returns the component type of the next component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmStringComponentType XmStringPeekNextTriple</code>(
<code>XmStringContext context</code>);</pre>
<h2>Description</h2>
<p><code>XmStringPeekNextTriple</code> examines the next component that would be fetched by <code>XmStringGetNextTriple</code> and returns the component type.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure that was allocated by the <code>XmStringInitContext</code> function.</dl>
<h2>Return</h2>
<p>Returns the type of the component found. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a list of component types.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringgetnexttriple/">XmStringGetNextTriple</a></code>(3).</p>
