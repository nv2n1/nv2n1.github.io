---
title: "xmstringgetnextsegment(3)"
name: "xmstringgetnextsegment"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringgetnextsegment/"
description: "XmStringGetNextSegment — A compound string function that fetches the bytes in the next segment of a compound string"
---

<p><code>XmStringGetNextSegment</code> &#8212; A compound string function that fetches the bytes in the next segment of a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringGetNextSegment</code>(
<code>XmStringContext context</code>,
<code>char **text</code>,
<code>XmStringTag *tag</code>,
<code>XmStringDirection *direction</code>,
<code>Boolean *separator</code>);</pre>
<h2>Description</h2>
<p>This routine is obsolete and exists for compatibility with previous releases. To read the contents of a compound string, read each component of the string with <code>XmStringGetNextTriple</code>. This <code>XmString</code> function returns the type, length, and value of the next component in the compound string. <code>XmStringGetNextSegment</code> fetches the bytes in the next segment; repeated calls fetch sequential segments. The <i>text</i>, <i>tag</i>, and <i>direction</i> of the fetched segment are returned each time. A Boolean status is returned to indicate whether a valid segment was successfully parsed. </p>
<p> If the function returns True, then the function allocates space to hold the returned <i>text</i> and <i>tag</i>. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure which was allocated by the <code>XmStringInitContext</code> function</p>
<dt><i>text</i></p>
<dd>Specifies a pointer to a NULL-terminated string</p>
<dt><i>tag</i></p>
<dd>Specifies a pointer to the font list element tag associated with the text</p>
<dt><i>direction</i></p>
<dd>Specifies a pointer to the direction of the text</p>
<dt><i>separator</i></p>
<dd>Specifies whether the next component of the compound string is a separator</dl>
<h2>Return</h2>
<p>Returns True if a valid segment is found.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringinitcontext/">XmStringInitContext</a></code>(3).</p>
