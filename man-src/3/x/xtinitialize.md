---
title: "xtinitialize(3)"
name: "xtinitialize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtinitialize/"
description: "XtInitialize – initialize"
---

<p>XtInitialize &#8211; initialize </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtInitialize(const char *<i>shell_name</i>, const char *<i>application_class</i>, XrmOptionDescRec* <i>options</i>, Cardinal <i>num_options</i>, int* <i>argc</i>, char** <i>argv</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>shell_name</i></p>
<dd>Specifies the name of the created shell widget.</p>
<dt><i>application_class</i></p>
<dd>Specifies the class name of this application, which usually is the generic name for all instances of this application.</p>
<dt><i>options</i></p>
<dd>Specifies how to parse the command line for any application-specific resources. The options argument is passed as a parameter to <code>XrmParseCommand</code>. For further information, see <i>Xlib &#8211; C Language X Interface</i>.</p>
<dt><i>num_options</i></p>
<dd>Specifies the number of entries in the options list.</p>
<dt><i>argc</i></p>
<dd>Specifies a pointer to the number of command line parameters.</p>
<dt><i>argv</i></p>
<dd>Specifies the command line parameters.</dl>
<h2>Description</h2>
<p><code>XtInitialize</code> calls <code>XtToolkitInitialize</code> followed by <code>XtOpenDisplay</code> with <i>display_string</i> NULL and <i>application_name</i> NULL, and finally calls <code>XtAppCreateShell</code> with <i>application_name</i> NULL, <i>widget_class</i> <code>applicationShellWidgetClass</code>, and the specified <i>args</i> and <i>num_args</i> and returns the created shell. The semantics of calling <code>XtInitialize</code> more than once are undefined. This routine has been replaced by <code>XtAppInitialize</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtappinitialize/">XtAppInitialize</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
