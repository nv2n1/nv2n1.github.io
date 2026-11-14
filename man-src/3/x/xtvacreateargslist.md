---
title: "xtvacreateargslist(3)"
name: "xtvacreateargslist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvacreateargslist/"
description: "XtVaCreateArgsList – dynamically allocate a varargs list"
---

<p>XtVaCreateArgsList &#8211; dynamically allocate a varargs list </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtVarArgsList XtVaCreateArgsList(XtPointer <i>unused</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>unused</i></p>
<dd>Must be specified as NULL.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies a variable parameter list of resource name and value pairs.</dl>
<h2>Description</h2>
<p>The <code>XtVaCreateArgsList</code> function allocates memory and copies its arguments into a single list pointer, which may be used with <code>XtVaNestedList</code>. The end of both lists is identified by a <i>name</i> entry containing NULL. Any entries of type <code>XtVaTypedArg</code> are copied as specified without applying conversions. Data passed by reference (including Strings) are not copied, only the pointers themselves; the caller must ensure that the data remain valid for the lifetime of the created varargs list. The list should be freed using <code>XtFree</code> when no longer needed.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
