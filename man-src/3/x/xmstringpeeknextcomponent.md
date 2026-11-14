---
title: "xmstringpeeknextcomponent(3)"
name: "xmstringpeeknextcomponent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringpeeknextcomponent/"
description: "XmStringPeekNextComponent — A compound string function that returns the component type of the next component to be fetched"
---

<p><code>XmStringPeekNextComponent</code> &#8212; A compound string function that returns the component type of the next component to be fetched</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmStringComponentType XmStringPeekNextComponent</code>(
<code>XmStringContext context</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringPeekNextTriple</code>. <code>XmStringPeekNextComponent</code> examines the next component that would be fetched by <code>XmStringGetNextComponent</code> and returns the component type.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure that was allocated by the <code>XmStringInitContext</code> function</dl>
<h2>Return</h2>
<p>Returns the type of component found. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a list of component types.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetnextcomponent/">XmStringGetNextComponent</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringinitcontext/">XmStringInitContext</a></code>(3).</p>
