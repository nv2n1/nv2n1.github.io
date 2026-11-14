---
title: "xtvaappinitialize(3)"
name: "xtvaappinitialize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvaappinitialize/"
description: "XtAppInitialize, XtVaAppInitialize – initialize, open, or close a display"
---

<p>XtAppInitialize, XtVaAppInitialize &#8211; initialize, open, or close a display </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtAppInitialize(XtAppContext* <i>app_context_return</i>, const char *<i>application_class</i>, XrmOptionDescRec* <i>options</i>, Cardinal <i>num_options</i>, int *<i>argc_in_out</i>, char **<i>argv_in_out</i>, String *<i>fallback_resources</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>Widget XtVaAppInitialize(XtAppContext* <i>app_context_return</i>, const char *<i>application_class</i>, XrmOptionDescRec* <i>options</i>, Cardinal <i>num_options</i>, int *<i>argc_in_out</i>, char **<i>argv_in_out</i>, String *<i>fallback_resources</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context_return</i></p>
<dd>Specifies the application context.</p>
<dt><i>application_class</i></p>
<dd>Specifies the class name of this application, which usually is the generic name for all instances of this application.</p>
<dt><i>options</i></p>
<dd>Specifies how to parse the command line for any application-specific resources. The options argument is passed as a parameter to <code>XrmParseCommand</code>. For further information, see <i>Xlib &#8211; C Language X Interface</i>.</p>
<dt><i>num_options</i></p>
<dd>Specifies the number of entries in the options list.</p>
<dt><i>argc_in_out</i></p>
<dd>Specifies a pointer to the number of command line parameters.</p>
<dt><i>argv_in_out</i></p>
<dd>Specifies the command line parameters.</p>
<dt><i>fallback_resources</i></p>
<dd>Specifies resource values to be used if the application class resource file cannot be opened or read, or NULL.</p>
<dt><i>args</i></p>
<dd>Specifies the argument list to override any other resource specification for the created shell widget.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of entries in the argument list.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override any other resource specification for the created shell widget.</dl>
<h2>Description</h2>
<p>The <code>XtAppInitialize</code> function calls <code>XtToolkitInitialize</code> followed by <code>XtCreateApplicationContext</code>, then calls <code>XtOpenDisplay</code> with <i>display_string</i> NULL and <i>application_name</i> NULL, and finally calls <code>XtAppCreateShell</code> with <i>application_name</i> NULL, <i>widget_class</i> <code>applicationShellWidgetClass</code>, and the specified <i>args</i> and <i>num_args</i> and returns the created shell. The modified <i>argc</i> and <i>argv</i> returned by <code>XtDisplayInitialize</code> are returned in <i>argc_in_out</i> and <i>argv_in_out</i>. If <i>app_context_return</i> is not NULL, the created application context is also returned. If the display specified by the command line cannot be opened, an error message is issued and <code>XtAppInitialize</code> terminates the application. If <i>fallback_resources</i> is non-NULL, <code>XtAppSetFallbackResources</code> is called with the value prior to calling <code>XtOpenDisplay</code>. </p>
<p> XtAppInitialize and XtVaAppInitialize have been superceded by <code>XtOpenApplication</code> and <code>XtVaOpenApplication</code> respectively.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtopenapplication/">XtOpenApplication</a>(3), <a href="/docs/linux/man/3-xtvaopenapplication/">XtVaOpenApplication</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
