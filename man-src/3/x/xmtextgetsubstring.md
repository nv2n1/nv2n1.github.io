---
title: "xmtextgetsubstring(3)"
name: "xmtextgetsubstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetsubstring/"
description: "XmTextGetSubstring — A Text function that retrieves a copy of a portion of the internal text buffer"
---

<p><code>XmTextGetSubstring</code> &#8212; A Text function that retrieves a copy of a portion of the internal text buffer</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>int XmTextGetSubstring</code>(
<code>Widget widget</code>,
<code>XmTextPosition start</code>,
<code>int num_chars</code>,
<code>int buffer_size</code>,
<code>char *buffer</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetSubstring</code> retrieves a copy of a portion of the internal text buffer of a Text widget. The function copies a specified number of characters from a given start position in the internal text buffer into a buffer provided by the application. A NULL terminator is placed at the end of the copied data. </p>
<p> The size of the required buffer depends on the maximum number of bytes per character (<code>MB_CUR_MAX</code>) for the current locale. <code>MB_CUR_MAX</code> is a macro defined in <code>stdlib.h</code>. The buffer should be large enough to contain the substring to be copied and a NULL terminator. Use the following equation to calculate the size of buffer the application should provide: </p>
<pre><i>buffer_size</i> = (<i>num_chars</i>* MB_CUR_MAX) + 1
(<code>void</code>)</pre>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Text widget ID.</dd>
<dt><i>start</i></dt>
<dd>Specifies the beginning character position from which the data will be retrieved. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dd>
<dt><i>num_chars</i></dt>
<dd>Specifies the number of characters to be copied into the provided buffer.</dd>
<dt><i>buffer_size</i></dt>
<dd>Specifies the size of the supplied buffer in bytes. This size should account for a NULL terminator.</dd>
<dt><i>buffer</i></dt>
<dd>Specifies the character buffer into which the internal text buffer will be copied.</dd></dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmCOPY_SUCCEEDED</code></dt>
<dd>The function was successful.</dd>
<dt><code>XmCOPY_FAILED</code></dt>
<dd>The function failed because it was unable to copy the specified number of characters into the buffer provided. The buffer size may be insufficient. The contents of <i>buffer</i> are undefined.</dd>
<dt><code>XmCOPY_TRUNCATED</code></dt>
<dd>The requested number of characters extended beyond the internal buffer. The function copied characters between <i>start</i> and the end of the widget&#8217;s buffer and terminated the string with a NULL terminator; fewer than <i>num_chars</i> characters were copied.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextgetsubstringwcs/">XmTextGetSubstringWcs</a></code>(3).</p>
