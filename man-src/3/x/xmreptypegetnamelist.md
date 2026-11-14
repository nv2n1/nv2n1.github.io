---
title: "xmreptypegetnamelist(3)"
name: "xmreptypegetnamelist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypegetnamelist/"
description: "XmRepTypeGetNameList — A representation type manager function that generates a list of values for a representation type"
---

<p><code>XmRepTypeGetNameList</code> &#8212; A representation type manager function that generates a list of values for a representation type</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>String * XmRepTypeGetNameList</code>(
<code>XmRepTypeId rep_type_id</code>,
<code>Boolean use_uppercase_format</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeGetNameList</code> generates a NULL-terminated list of the value names associated with the specified representation type. Each value name is a NULL-terminated string. This routine allocates memory for the returned data. The application must free this memory using <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>rep_type_id</i></p>
<dd>Specifies the identification number of the representation type.</p>
<dt><i>use_uppercase_format</i></p>
<dd>Specifies a Boolean value that controls the format of the name list. If the value is True, each value name is in uppercase characters prefixed by <code>Xm</code>; if it is False, the names are in lowercase characters.</dl>
<h2>Return</h2>
<p>Returns a pointer to an array of the value names.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypegetid/">XmRepTypeGetId</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetregistered/">XmRepTypeGetRegistered</a></code>(3), and <code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3).</p>
