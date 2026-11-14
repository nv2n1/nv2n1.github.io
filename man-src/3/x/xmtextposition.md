---
title: "xmtextposition(3)"
name: "xmtextposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextposition/"
description: "XmTextPosition — Data type for a character position within a text string"
---

<p><code>XmTextPosition</code> &#8212; Data type for a character position within a text string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmTextPosition</code> is an integer data type that holds a character&#8217;s position within a text string for Text and TextField. </p>
<p> An <code>XmTextPosition</code> value conceptually points to the gap between two characters. For example, consider a text string consisting of <code>N</code> characters. A value of 0 refers to the position immediately prior to the first character. A value of 1 refers to the position in between the first and second characters. A value of <code>N</code> refers to the position immediately following the last character. Therefore, the text string of <code>N</code> characters actually contains <code>N + 1</code> positions.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
