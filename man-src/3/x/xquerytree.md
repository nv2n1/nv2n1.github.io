---
title: "xquerytree(3)"
name: "xquerytree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xquerytree/"
description: "XQueryTree – query window tree information"
---

<p>XQueryTree &#8211; query window tree information </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XQueryTree(Display *<i>display</i>, Window <i>w</i>, Window *<i>root_return</i>, Window *<i>parent_return</i>, Window **<i>children_return</i>, unsigned int *<i>nchildren_return</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>children_return</i></dt>
<dd>Returns the list of children.</dd>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>nchildren_return</i></dt>
<dd>Returns the number of children.</dd>
<dt><i>parent_return</i></dt>
<dd>Returns the parent window.</dd>
<dt><i>root_return</i></dt>
<dd>Returns the root window.</dd>
<dt><i>w</i></dt>
<dd>Specifies the window whose list of children, root, parent, and number of children you want to obtain.</dd></dl>
<h2>Description</h2>
<p>The <code>XQueryTree</code> function returns the root ID, the parent window ID, a pointer to the list of children windows (NULL when there are no children), and the number of children in the list for the specified window. The children are listed in current stacking order, from bottom-most (first) to top-most (last). <code>XQueryTree</code> returns zero if it fails and nonzero if it succeeds. To free a non-NULL children list when it is no longer needed, use <code>XFree</code>. </p>
<p> <code>XQueryTree</code> can generate a <code>BadWindow</code> error.</p>
<h2>Bugs</h2>
<p>This really should return a screen *, not a root window ID.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></dt>
<dd>A value for a Window argument does not name a defined Window.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xgetwindowattributes/">XGetWindowAttributes</a>(3), <a href="/docs/linux/man/3-xquerypointer/">XQueryPointer</a>(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
