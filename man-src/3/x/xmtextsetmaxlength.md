---
title: "xmtextsetmaxlength(3)"
name: "xmtextsetmaxlength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetmaxlength/"
description: "XmTextSetMaxLength — A Text function that sets the value of the current maximum allowable length of a text string entered from the keyboard"
---

<p><code>XmTextSetMaxLength</code> &#8212; A Text function that sets the value of the current maximum allowable length of a text string entered from the keyboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetMaxLength</code>(
<code>Widget widget</code>,
<code>int max_length</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetMaxLength</code> sets the value of the current maximum allowable length of the text string in the Text widget. The maximum allowable length prevents the user from entering a text string from the keyboard that is larger than this limit. Strings that are entered using the <code>XmNvalue</code> (or <code>XmNvalueWcs</code>) resource, or the <code>XmTextSetString</code> (or <code>XmTextSetStringWcs</code>) function ignore this resource.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>max_length</i></p>
<dd>Specifies the maximum allowable length of the text string</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetstring/">XmTextSetString</a></code>(3), and <code><a href="/docs/linux/man/3-xmtextsetstringwcs/">XmTextSetStringWcs</a></code>(3).</p>
