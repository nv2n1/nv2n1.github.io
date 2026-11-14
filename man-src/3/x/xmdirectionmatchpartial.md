---
title: "xmdirectionmatchpartial(3)"
name: "xmdirectionmatchpartial"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdirectionmatchpartial/"
description: "XmDirectionMatchPartial — A function that checks for a specified direction component"
---

<p><code>XmDirectionMatchPartial</code> &#8212; A function that checks for a specified direction component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
Boolean XmDirectionMatchPartial (<i>d1, d2, dmask</i>)
 XmDirection <i>d1</i>;
 XmDirection <i>d2</i>;
 XmDirection <i>dmask</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmDirectionMatchPartial</code> compares <i>d1</i> and <i>d2</i> along the direction component specified by <i>dmask</i>. For example, if <i>dmask</i> equals <code>XmVERTICAL_MASK</code>, then the function will compare only the vertical components of <i>d1</i> and <i>d2</i>.</p>
<dl COMPACT>
<dt><i>d1</i></p>
<dd>Specifies an <code>XmDirection</code> value to check.</p>
<dt><i>d2</i></p>
<dd>Specifies an <code>XmDirection</code> value to check.</p>
<dt><i>dmask</i></p>
<dd>Specifies the direction component along which <i>d1</i> and <i>d2</i> are to be checked. Appropriate values for <i>dmask</i> are <code>XmHORIZONTAL_MASK</code>, <code>XmVERTICAL_MASK</code>, and <code>XmPRECEDENCE_MASK</code>.</dl>
<h2>Return Values</h2>
<p>Returns True if the <i>d1</i> and <i>d2</i> match in the component specified by <i>dmask</i>; otherwise, returns False.</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectionmatch/">XmDirectionMatch</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectiontostringdirection/">XmDirectionToStringDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringdirectiontodirection/">XmStringDirectionToDirection</a></code>(3).</p>
