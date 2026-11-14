---
title: "xtappgeterrordatabase(3)"
name: "xtappgeterrordatabase"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappgeterrordatabase/"
description: "XtAppGetErrorDatabase, XtAppGetErrorDatabaseText – obtain error database"
---

<p>XtAppGetErrorDatabase, XtAppGetErrorDatabaseText &#8211; obtain error database </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XrmDatabase *XtAppGetErrorDatabase(XtAppContext <i>app_context</i>);</p>
<dd>void XtAppGetErrorDatabaseText(XtAppContext <i>app_context</i>, const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, char *<i>buffer_return</i>, int <i>nbytes</i>, XrmDatabase <i>database</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>buffer_return</i></p>
<dd>Specifies the buffer into which the error message is to be returned.</p>
<dt><i>class</i></p>
<dd>Specifies the resource class of the error message.</p>
<dt><i>database</i></p>
<dd>Specifies the name of the alternative database that is to be used or NULL if the application&#8217;s database is to be used.</p>
<dt><i>defaultMsg</i></p>
<dd>Specifies the default message to use.</p>
<dt><i>name</i></p>
<dd>
<dt><i>type</i></p>
<dd>Specifies the name and type that are concatenated to form the resource name of the error message.</p>
<dt><i>nbytes</i></p>
<dd>Specifies the size of the buffer in bytes.</dl>
<h2>Description</h2>
<p>The <code>XtAppGetErrorDatabase</code> function returns the address of the error database. The Intrinsics do a lazy binding of the error database and do not merge in the database file until the first call to <code>XtAppGetErrorDatbaseText</code>. </p>
<p> The <code>XtAppGetErrorDatabaseText</code> returns the appropriate message from the error database or returns the specified default message if one is not found in the error database.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtapperror/">XtAppError</a>(3), <a href="/docs/linux/man/3-xtapperrormsg/">XtAppErrorMsg</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
