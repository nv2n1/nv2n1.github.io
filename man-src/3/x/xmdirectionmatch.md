---
title: "xmdirectionmatch(3)"
name: "xmdirectionmatch"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdirectionmatch/"
description: "XmDirectionMatch — A function that checks for a specified direction component"
---

<p><code>XmDirectionMatch</code> &#8212; A function that checks for a specified direction component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
Boolean XmDirectionMatch (<i>d1, d2</i>)
 XmDirection <i>d1</i>;
 XmDirection <i>d2</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmDirectionMatch</code> compares two <code>XmDirection</code> values. The function returns a Boolean value depending on whether or not the two input values &quot;match.&quot; The simplest match is when <i>d1</i> and <i>d2</i> are identical. However, other matches are possible. <code>XmDirectionMatch</code> attempts to compare specified bits only; nonspecified bits automatically match. </p>
<p> For example, suppose that <i>d1</i> equals <code>XmTOP_TO_BOTTOM_RIGHT_TO_LEFT</code>. In this case, the function will return True if <i>d2</i> equals either <code>XmRIGHT_TO_LEFT</code> or <code>XmTOP_TO_BOTTOM</code>. However, the function will return False if <i>d2</i> equals <code>XmTOP_TO_BOTTOM_LEFT_TO_RIGHT</code>, <code>XmBOTTOM_TO_TOP_RIGHT_TO_LEFT</code>, or <code>XmBOTTOM_TO_TOP_LEFT_TO_RIGHT</code>. </p>
<p> Note that direction can be thought of as having three components, a horizontal component, a vertical component, and the precedence among them. This means that in addition to the previously mentioned directions, the function will still return False if <i>d1</i> equals <code>XmTOP_TO_BOTTOM_RIGHT_TO_LEFT</code> and <i>d2</i> equals <code>XmRIGHT_TO_LEFT_TOP_TO_BOTTOM</code>.</p>
<dl COMPACT>
<dt><i>d1</i></p>
<dd>Specifies an <code>XmDirection</code> value.</p>
<dt><i>d2</i></p>
<dd>Specifies an <code>XmDirection</code> value.</dl>
<h2>Return Values</h2>
<p>Returns True if <i>d1</i> &quot;matches&quot; <i>d2</i>; otherwise, returns False.</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectionmatchpartial/">XmDirectionMatchPartial</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectiontostringdirection/">XmDirectionToStringDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringdirectiontodirection/">XmStringDirectionToDirection</a></code>(3).</p>
