---
title: "xfindcontext(3)"
name: "xfindcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfindcontext/"
description: "XSaveContext, XFindContext, XDeleteContext, XUniqueContext – associative look-up routines"
---

<p>XSaveContext, XFindContext, XDeleteContext, XUniqueContext &#8211; associative look-up routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSaveContext(Display *<i>display</i>, XID <i>rid</i>, XContext <i>context</i>, XPointer <i>data</i>);</dd>
<dd>int XFindContext(Display *<i>display</i>, XID <i>rid</i>, XContext <i>context</i>, XPointer *<i>data_return</i>);</dd>
<dd>int XDeleteContext(Display *<i>display</i>, XID <i>rid</i>, XContext <i>context</i>);</dd></dl>
<p> XContext XUniqueContext(void);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>context</i></dt>
<dd>Specifies the context type to which the data belongs.</dd>
<dt><i>data</i></dt>
<dd>Specifies the data to be associated with the window and type.</dd>
<dt><i>data_return</i></dt>
<dd>Returns the data.</dd>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>rid</i></dt>
<dd>Specifies the resource ID with which the data is associated.</dd></dl>
<h2>Description</h2>
<p>If an entry with the specified resource ID and type already exists, <code>XSaveContext</code> overrides it with the specified context. The <code>XSaveContext</code> function returns a nonzero error code if an error has occurred and zero otherwise. Possible errors are <code>XCNOMEM</code> (out of memory). </p>
<p> Because it is a return value, the data is a pointer. The <code>XFindContext</code> function returns a nonzero error code if an error has occurred and zero otherwise. Possible errors are <code>XCNOENT</code> (context-not-found). </p>
<p> The <code>XDeleteContext</code> function deletes the entry for the given resource ID and type from the data structure. This function returns the same error codes that <code>XFindContext</code> returns if called with the same arguments. <code>XDeleteContext</code> does not free the data whose address was saved. </p>
<p> The <code>XUniqueContext</code> function creates a unique context type that may be used in subsequent calls to <code>XSaveContext</code>.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
