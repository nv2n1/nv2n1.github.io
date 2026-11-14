---
title: "xvacreatenestedlist(3)"
name: "xvacreatenestedlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvacreatenestedlist/"
description: "XVaCreateNestedList – allocate a nested variable argument list"
---

<p>XVaCreateNestedList &#8211; allocate a nested variable argument list </p>
<h2>Syntax</h2>
<p>typedef void * XVaNestedList;</p>
<dl COMPACT>
<dd>XVaNestedList XVaCreateNestedList(int <i>dummy</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dummy</i></p>
<dd>Specifies an unused argument (required by ANSI C).</p>
<dt>&#8230;</p>
<dd>Specifies the variable length argument list.</dl>
<h2>Description</h2>
<p>The <code>XVaCreateNestedList</code> function allocates memory and copies its arguments into a single list pointer, which may be used as a value for arguments requiring a list value. Any entries are copied as specified. Data passed by reference is not copied; the caller must ensure data remains valid for the lifetime of the nested list. The list should be freed using <code>XFree</code> when it is no longer needed.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
