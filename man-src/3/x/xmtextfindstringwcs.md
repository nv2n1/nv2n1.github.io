---
title: "xmtextfindstringwcs(3)"
name: "xmtextfindstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfindstringwcs/"
description: "XmTextFindStringWcs — A Text function that finds the beginning position of a wide character text string"
---

<p><code>XmTextFindStringWcs</code> &#8212; A Text function that finds the beginning position of a wide character text string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextFindStringWcs</code>(
<code>Widget widget</code>,
<code>XmTextPosition start</code>,
<code>wchar_t *wcstring</code>,
<code>XmTextDirection direction</code>,
<code>XmTextPosition *position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFindStringWcs</code> locates the beginning position of a specified wide character text string. This routine searches forward or backward for the first occurrence of the string, starting from the given start position. If a match is found, the function returns the position of the first character of the string in <i>position</i>. If the match string begins at the current position, this routine returns the current position.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Text widget ID.</dd>
<dt><i>start</i></dt>
<dd>Specifies the character position from which the search proceeds. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dd>
<dt><i>wcstring</i></dt>
<dd>Specifies the wide character search string.</dd>
<dt><i>direction</i></dt>
<dd>Indicates the search direction. It is relative to the primary direction of the text. The possible values are</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmTEXT_FORWARD</code></dt>
<dd>The search proceeds toward the end of the buffer.</dd>
<dt><code>XmTEXT_BACKWARD</code></dt>
<dd>The search proceeds toward the beginning of the buffer.</dd></dl>
</dl>
<dt><i>position</i></dt>
<dd>Specifies the pointer in which the first character position of the string match is returned. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero). If the function returns False, this value is undefined.</dd></dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if a string match is found; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfindstring/">XmTextFindString</a></code>(3).</p>
