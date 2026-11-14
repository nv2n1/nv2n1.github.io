---
title: "xtsetarg(3)"
name: "xtsetarg"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetarg/"
description: "XtSetArg, XtMergeArgLists – set and merge ArgLists"
---

<p>XtSetArg, XtMergeArgLists &#8211; set and merge ArgLists </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>int XtSetArg(Arg <i>arg</i>, String <i>name</i>, XtArgVal <i>value</i>);</p>
<dd>ArgList XtMergeArgLists(ArgList <i>args1</i>, Cardinal <i>num_args1</i>, ArgList <i>args2</i>, Cardinal <i>num_args2</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>arg</i></p>
<dd>Specifies the name-value pair to set.</p>
<dt><i>args1</i></p>
<dd>Specifies the first <code>ArgList</code>.</p>
<dt><i>args2</i></p>
<dd>Specifies the second <code>ArgList</code>.</p>
<dt><i>num_args1</i></p>
<dd>Specifies the number of arguments in the first argument list.</p>
<dt><i>num_args2</i></p>
<dd>Specifies the number of arguments in the second argument list.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the resource.</p>
<dt><i>value</i></p>
<dd>Specifies the value of the resource if it will fit in an <code>XtArgVal</code> or the address.</dl>
<h2>Description</h2>
<p>The <code>XtSetArg</code> function is usually used in a highly stylized manner to minimize the probability of making a mistake; for example: </p>
<dl COMPACT>
<dd>
<pre>Arg args[20];
int n;
n = 0;
XtSetArg(args[n], XtNheight, 100); n++;
XtSetArg(args[n], XtNwidth, 200); n++;
XtSetValues(widget, args, n);</pre>
</dl>
<p> Alternatively, an application can statically declare the argument list and use <code>XtNumber</code>: </p>
<dl COMPACT>
<dd>
<pre>static Args args[] = {
 {XtNheight, (XtArgVal) 100},
 {XtNwidth, (XtArgVal) 200},
};
XtSetValues(Widget, args, XtNumber(args));</pre>
</dl>
<p> Note that you should not use auto-increment or auto-decrement within the first argument to <code>XtSetArg</code>. <code>XtSetArg</code> can be implemented as a macro that dereferences the first argument twice. </p>
<p> The <code>XtMergeArgLists</code> function allocates enough storage to hold the combined <code>ArgList</code> structures and copies them into it. Note that it does not check for duplicate entries. When it is no longer needed, free the returned storage by using <code>XtFree</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtoffset/">XtOffset</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
