---
title: "xmtextfindstring(3)"
name: "xmtextfindstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfindstring/"
description: "XmTextFindString — A Text function that finds the beginning position of a text string"
---

<p><code>XmTextFindString</code> &#8212; A Text function that finds the beginning position of a text string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmTextFindString</code>(
<code>Widget widget</code>,
<code>XmTextPosition start</code>,
<code>char *string</code>,
<code>XmTextDirection direction</code>,
<code>XmTextPosition *position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFindString</code> locates the beginning position of a specified text string. This routine searches forward or backward for the first occurrence of the string starting from the given start position. If it finds a match, the function returns the position of the first character of the string in <i>position</i>. If the match string begins at the current position, this routine returns the current position.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Text widget ID.</dd>
<dt><i>start</i></dt>
<dd>Specifies the character position from which the search proceeds. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dd>
<dt><i>string</i></dt>
<dd>Specifies the search string.</dd>
<dt><i>direction</i></dt>
<dd>Indicates the search direction. It is relative to the primary direction of the text. The possible values are</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmTEXT_FORWARD</code></dt>
<dd>The search proceeds toward the end of the text buffer.</dd>
<dt><code>XmTEXT_BACKWARD</code></dt>
<dd>The search proceeds toward the beginning of the text buffer.</dd></dl>
</dl>
<dt><i>position</i></dt>
<dd>Specifies the pointer in which the first character position of the string match is returned. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero). If the function returns False, this value is undefined.</dd></dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if a string match is found; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfindstringwcs/">XmTextFindStringWcs</a></code>(3).</p>
