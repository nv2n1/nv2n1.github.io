---
title: "xmtextfieldsetmaxlength(3)"
name: "xmtextfieldsetmaxlength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldsetmaxlength/"
description: "XmTextFieldSetMaxLength — A TextField function that sets the value of the current maximum allowable length of a text string entered from the keyboard"
---

<p><code>XmTextFieldSetMaxLength</code> &#8212; A TextField function that sets the value of the current maximum allowable length of a text string entered from the keyboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetMaxLength</code>(
<code>Widget widget</code>,
<code>int max_length</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetMaxLength</code> sets the value of the current maximum allowable length of the text string in the TextField widget. The maximum allowable length prevents the user from entering a text string from the keyboard that is larger than this limit. Strings that are entered using the <code>XmNvalue</code> (or <code>XmNvalueWcs</code>) resource, or the <code>XmTextFieldSetString</code> (or <code>XmTextFieldSetStringWcs</code>) function ignore this resource.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>max_length</i></p>
<dd>Specifies the maximum allowable length of the text string</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetstring/">XmTextFieldSetString</a></code>(3), and <code><a href="/docs/linux/man/3-xmtextfieldsetstringwcs/">XmTextFieldSetStringWcs</a></code>(3).</p>
