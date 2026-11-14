---
title: "xmstringsegmentcreate(3)"
name: "xmstringsegmentcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringsegmentcreate/"
description: "XmStringSegmentCreate — A compound string function that creates a compound string"
---

<p><code>XmStringSegmentCreate</code> &#8212; A compound string function that creates a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringSegmentCreate</code>(
<code>char * text</code>,
<code>XmStringTag tag</code>,
<code>XmStringDirection direction</code>,
<code>Boolean separator</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It can be replaced by using a combination of <code>XmStringComponentCreate</code> and <code>XmStringConcat</code>. <code>XmStringSegmentCreate</code> is a high-level function that assembles a compound string consisting of a font list element tag, a direction component, a text component, and an optional separator component. </p>
<p> The function allocates space for the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a NULL-terminated string to be used as the text component of the compound string.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag component to be associated with the text. The value <code>XmFONTLIST_DEFAULT_TAG</code> is for compatibility with previous releases.</p>
<dt><i>direction</i></p>
<dd>Specifies the direction of the text.</p>
<dt><i>separator</i></p>
<dd>A value of False means the compound string does not have a separator at the end. A value of True, means a separator immediately follows the text component.</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
