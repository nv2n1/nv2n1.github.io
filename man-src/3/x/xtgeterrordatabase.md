---
title: "xtgeterrordatabase(3)"
name: "xtgeterrordatabase"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgeterrordatabase/"
description: "XtGetErrorDatabase, XtGetErrorDatabaseText – obtain error database"
---

<p>XtGetErrorDatabase, XtGetErrorDatabaseText &#8211; obtain error database </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XrmDatabase *XtGetErrorDatabase(void);</p>
<dd>void XtGetErrorDatabaseText(const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, char *<i>buffer_return</i>, int <i>nbytes</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>buffer_return</i></p>
<dd>Specifies the buffer into which the error message is to be returned.</p>
<dt><i>class</i></p>
<dd>Specifies the resource class of the error message.</p>
<dt><i>default</i></p>
<dd>Specifies the default message to use.</p>
<dt><i>name</i></p>
<dd>
<dt><i>type</i></p>
<dd>Specifies the name and type that are concatenated to form the resource name of the error message.</p>
<dt><i>nbytes</i></p>
<dd>Specifies the size of the buffer in bytes.</dl>
<h2>Description</h2>
<p>The <code>XtGetErrorDatabase</code> function has been superceded by <code>XtAppGetErrorDatabase</code>. </p>
<p> The <code>XtGetErrorDatabaseText</code> function has been superceded by <code>XtAppGetErrorDatabaseText</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtappgeterrordatabase/">XtAppGetErrorDatabase</a></code>(3) <code><a href="/docs/linux/man/3-xtappgeterrordatabasetext/">XtAppGetErrorDatabaseText</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
