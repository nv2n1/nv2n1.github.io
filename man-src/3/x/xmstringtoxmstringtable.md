---
title: "xmstringtoxmstringtable(3)"
name: "xmstringtoxmstringtable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringtoxmstringtable/"
description: "XmStringToXmStringTable — A convenience function that converts a single compound string to a table of compound strings"
---

<p><code>XmStringToXmStringTable</code> &#8212; A convenience function that converts a single compound string to a table of compound strings</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Cardinal XmStringToXmStringTable</code>(
<code>XmString string</code>,
<code>XmString break_component</code>,
<code>XmStringTable *table</code>);</pre>
<h2>Description</h2>
<p><code>XmStringToXmStringTable</code> takes as input a single compound string and a specified string component (such as a tab) and returns a table of compound strings consisting of portions of <i>string</i> delimited by components matching <i>break_component</i>. The components marking breaks will not appear in the resulting table.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the <code>XmString</code> to be converted.</p>
<dt><i>break_component</i></p>
<dd>Specifies the <code>XmStringComponent</code> that will be used to indicate where to split <i>string</i> to form the individual elements of <i>table</i>. The most useful types will be <code>XmSTRING_COMPONENT_SEPARATOR</code> and <code>XmSTRING_COMPONENT_TAB</code>. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a complete list of possible component types. Note, however, that the <code>XmSTRING_COMPONENT_UNKNOWN</code> component is not a possible type.</p>
<dt><i>table</i></p>
<dd>Returns the equivalent <code>XmStringTable</code>. The function will allocate space to hold the returned <code>XmStringTable</code>. When the applicaiton no longer needs the returned <code>XmStringTable</code>, the application should call <code>XmStringFree</code> once for each compound string in the table, and then calling <code>XtFree</code> to deallocate the <code>XmStringTable</code> itself.</dl>
<h2>Return</h2>
<p>Returns the number of compound strings in <i>table</i>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringtable/">XmStringTable</a></code>(3).</p>
