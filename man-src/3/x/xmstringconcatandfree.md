---
title: "xmstringconcatandfree(3)"
name: "xmstringconcatandfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringconcatandfree/"
description: "XmStringConcatAndFree — A compound string function that appends one string to another and frees the original strings"
---

<p><code>XmStringConcatAndFree</code> &#8212; A compound string function that appends one string to another and frees the original strings</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringConcatAndFree</code>(
<code>XmString s1</code>,
<code>XmString s2</code>);</pre>
<h2>Description</h2>
<p><code>XmStringConcatAndFree</code> copies <i>s2</i> to the end of <i>s1</i> and returns a copy of the resulting compound string. The original strings are freed. The function will allocate space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string to which a copy of <i>s2</i> is appended</p>
<dt><i>s2</i></p>
<dd>Specifies the compound string that is appended to the end of <i>s1</i></dl>
<p> The <code>XmStringConcatAndFree</code> function works like the <code>XmStringConcat</code> function, except that it frees the <i>s1</i> and <i>s2</i> strings, and is therefore more efficient. You should use <code>XmStringConcatAndFree</code> instead of <code>XmStringConcat</code> if you want <i>s1</i> and <i>s2</i> to be freed afterwards.</p>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringconcat/">XmStringConcat</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
