---
title: "xmstringtableparsestringarray(3)"
name: "xmstringtableparsestringarray"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringtableparsestringarray/"
description: "XmStringTableParseStringArray — A convenience function that converts an array of strings to a compound string table"
---

<p><code>XmStringTableParseStringArray</code> &#8212; A convenience function that converts an array of strings to a compound string table</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmStringTable XmStringTableParseStringArray</code>(
<code>XtPointer *strings</code>,
<code>Cardinal count</code>,
<code>XmStringTag tag</code>,
<code>XmTextType type</code>,
<code>XmParseTable parse</code>,
<code>Cardinal parse_count</code>,
<code>XtPointer call_data</code>);</pre>
<h2>Description</h2>
<p><code>XmStringTableParseStringArray</code> takes an array of strings, allocates an <code>XmStringTable</code> with an equal number of slots, calls <code>XmStringParseText</code> on each string in <i>strings</i>, and inserts the resulting <code>XmString</code> in the corresponding slot in the <code>XmStringTable</code>.</p>
<dl COMPACT>
<dt><i>strings</i></p>
<dd>Specifies an array of strings of characters as determined by <i>type</i>.</p>
<dt><i>count</i></p>
<dd>Specifies the number of strings in <i>strings</i>.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in creating the result. The type of tag created (charset or locale) depends on the type of the text and the value given. If the value specified is NULL, and <i>type</i> indicates that a charset tag should be created, then the tag will have the value of <code>XmFONTLIST_DEFAULT_TAG</code>. If <i>type</i> indicates a locale tag, then the tag will have the value of <code>XmFONTLIST_DEFAULT_TAG</code>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of text to be passed in and the type of tag. If the type is either <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>, a locale tag should be created. If the type is <code>XmCHARSET_TEXT</code>, a charset tag will be created.</p>
<dt><i>parse</i></p>
<dd>Specifies the parse table to be used.</p>
<dt><i>parse_count</i></p>
<dd>Specifies the number of entries in the parse table.</p>
<dt><i>call_data</i></p>
<dd>Specifies data to be passed to the parse procedures.</dl>
<h2>Return</h2>
<p>Returns a new <code>XmStringTable</code>. The function allocates space to hold the <code>XmStringTable</code>. When the application no longer needs the returned <code>XmStringTable</code>, the application should call <code>XmStringFree</code> <i>count</i> times (that is, one time for each returned compound string) and then call <code>XtFree</code> to deallocate the <code>XmStringTable</code> itself.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3).</p>
