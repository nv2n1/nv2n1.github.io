---
title: "xmstringgetnexttriple(3)"
name: "xmstringgetnexttriple"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringgetnexttriple/"
description: "XmStringGetNextTriple — An XmString function that returns the type, length, and value of the next component in the compound string"
---

<p><code>XmStringGetNextTriple</code> &#8212; An XmString function that returns the type, length, and value of the next component in the compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmStringComponentType XmStringGetNextTriple</code>(
<code>XmStringContext context</code>,
<code>unsigned int *length</code>,
<code>XtPointer *value</code>);</pre>
<h2>Description</h2>
<p><code>XmStringGetNextTriple</code> returns the type, length, and value of the next component in the compound string identified by <i>context</i>. This function returns one component at a time.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure that was allocated by the <code>XmStringInitContext</code> function.</p>
<dt><i>length</i></p>
<dd>Specifies a pointer to the length of the value of the returned component.</p>
<dt><i>value</i></p>
<dd>Specifies a pointer to the value of the returned component. If the returned value is not NULL, the function allocates space to hold the returned value. When the application no longer needs the returned compound string, the application should call <code>XtFree</code>.</dl>
<h2>Return</h2>
<p>Returns the type of the component found. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a list of component types.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetnextcomponent/">XmStringGetNextComponent</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringpeeknexttriple/">XmStringPeekNextTriple</a></code>(3).</p>
