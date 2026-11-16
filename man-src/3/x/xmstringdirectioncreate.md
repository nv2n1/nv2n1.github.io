---
title: "xmstringdirectioncreate(3)"
name: "xmstringdirectioncreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringdirectioncreate/"
description: "XmStringDirectionCreate — A compound string function that creates a compound string"
---

<p><code>XmStringDirectionCreate</code> &#8212; A compound string function that creates a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringDirectionCreate</code>(
<code>XmStringDirection direction</code>);</pre>
<h2>Description</h2>
<p><code>XmStringDirectionCreate</code> creates a compound string with a single component, a direction with the given value. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>direction</i></dt>
<dd>Specifies the value of the direction component. The possible values are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmSTRING_DIRECTION_L_TO_R</code></dt>
<dd>Specifies left to right display.</dd>
<dt><code>XmSTRING_DIRECTION_R_TO_L</code></dt>
<dd>Specifies right to left display.</dd>
<dt><code>XmSTRING_DIRECTION_DEFAULT</code></dt>
<dd>Specifies that the display direction will be set by the widget in which the compound string is to be displayed.</dd></dl>
</dl>
</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
