---
title: "xmreptypegetid(3)"
name: "xmreptypegetid"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypegetid/"
description: "XmRepTypeGetId — A representation type manager function that retrieves the identification number of a representation type"
---

<p><code>XmRepTypeGetId</code> &#8212; A representation type manager function that retrieves the identification number of a representation type</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>XmRepTypeId XmRepTypeGetId</code>(
<code>String rep_type</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeGetId</code> searches the registration list for the specified representation type and returns the associated identification number.</p>
<dl COMPACT>
<dt><i>rep_type</i></p>
<dd>Specifies the representation type for which an identification number is requested</dl>
<h2>Return</h2>
<p>Returns the identification number of the specified representation type. If the representation type is not registered, the function returns <code>XmREP_TYPE_INVALID</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypegetregistered/">XmRepTypeGetRegistered</a></code>(3) and <code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3).</p>
