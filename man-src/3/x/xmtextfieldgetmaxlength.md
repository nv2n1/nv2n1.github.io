---
title: "xmtextfieldgetmaxlength(3)"
name: "xmtextfieldgetmaxlength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetmaxlength/"
description: "XmTextFieldGetMaxLength — A TextField function that accesses the value of the current maximum allowable length of a text string entered from the keyboard"
---

<p><code>XmTextFieldGetMaxLength</code> &#8212; A TextField function that accesses the value of the current maximum allowable length of a text string entered from the keyboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>int XmTextFieldGetMaxLength</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetMaxLength</code> accesses the value of the current maximum allowable length of the text string in the TextField widget entered from the keyboard. The maximum allowable length prevents the user from entering a text string larger than this limit. Note that the maximum allowable length is the same as the value of the widget&#8217;s <code>XmNmaxLength</code> resource.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the integer value that indicates the string&#8217;s maximum allowable length that can be entered from the keyboard.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
