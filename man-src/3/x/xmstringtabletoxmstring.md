---
title: "xmstringtabletoxmstring(3)"
name: "xmstringtabletoxmstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringtabletoxmstring/"
description: "XmStringTableToXmString — A convenience function that converts a compound string table to a single compound string"
---

<p><code>XmStringTableToXmString</code> &#8212; A convenience function that converts a compound string table to a single compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringTableToXmString</code>(
<code>XmStringTable table</code>,
<code>Cardinal count</code>,
<code>XmString break_component</code>);</pre>
<h2>Description</h2>
<p><code>XmStringTableToXmString</code> takes as input <i>table</i> of compound strings and a specified string component (such as a tab) and returns a single compound string consisting of each of the elements of <i>table</i> concatenated together with a single copy of <i>break_component</i> inserted between each element.</p>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies an <code>XmStringTable</code> containing the compound strings to be converted.</p>
<dt><i>count</i></p>
<dd>Specifies the number of compound strings in <i>table</i>.</p>
<dt><i>break_component</i></p>
<dd>Specifies the <code>XmStringComponent</code> that will be inserted in the result to separate the individual elements of <i>table</i>. The most useful types will be <code>XmSTRING_COMPONENT_SEPARATOR</code> and <code>XmSTRING_COMPONENT_TAB</code>. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a complete list of possible component types. Note, however, that the <code>XmSTRING_COMPONENT_UNKNOWN</code> component is not a possible type.</dl>
<h2>Return</h2>
<p>Returns a new <code>XmString</code>. The function will allocate space to hold the returned compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
