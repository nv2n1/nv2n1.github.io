---
title: "xmstringcomponentcreate(3)"
name: "xmstringcomponentcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcomponentcreate/"
description: "XmStringComponentCreate — A compound string function that creates arbitrary components"
---

<p><code>XmStringComponentCreate</code> &#8212; A compound string function that creates arbitrary components</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringComponentCreate</code>(
<code>XmStringComponentType c_type</code>,
<code>unsigned int length</code>,
<code>XtPointer value</code>);</pre>
<h2>Description</h2>
<p><code>XmStringComponentCreate</code> creates a new <code>XmString</code> component of type <i>c_type</i>, containing <i>value</i>. If <i>value</i> is invalid for the particular component type, this function fails and returns NULL.</p>
<dl COMPACT>
<dt><i>c_type</i></p>
<dd>Specifies the type of component to be created.</p>
<dt><i>length</i></p>
<dd>Specifies the length in bytes of <i>value</i>. Note that this must be precisely the length of the <i>value</i> string, <i>not</i> including any trailing null characters.</p>
<dt><i>value</i></p>
<dd>Specifies the value to be used in the creation of the component.</dl>
<p> Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a list of the possible <code>XmString</code> component types.</p>
<h2>Return</h2>
<p>If <i>value</i> is invalid for <i>c_type</i>, fails and returns NULL. Otherwise, this function returns a new compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code>XmStringGetNextTriple</code>, <code>XmStringComponentType</code>, and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
